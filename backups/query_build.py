from astropy.io import fits
import sqlcl
import sys
import time


#determines if point b is in square region of 2*size on a side centered at point a
def isInRegion(ra, dec, ra_center, dec_center, size): 
  if (ra < ra_center + size) and (ra > ra_center - size):
    if (dec < dec_center + size) and (dec > dec_center - size):
      return True
  return False

def makeSingleQ(data, start, stop, size, fields):
  #print 'Making Single Query that starts at '+`start`+' and stops at '+`stop`
  query = 'SELECT ' + reduce(lambda x,y: str(x) + ', ' + str(y),fields) + ' FROM specObj WHERE'
  needOR = False # Need to add ORs for multiple BHBs after the first entry
  for d in data[start : stop]:
    (ra,dec) = map(lambda x,y: (x[0]+y[0],x[1]+y[1]),[[d['RAJ2000']]*2,[d['DEJ2000']]*2],[[-1*size,size]]*2)
    if needOR: query += ' OR '
    else: needOR = True # will need it if there are any addition elems to add
    query += '((ra BETWEEN '+`ra[0]`+' AND '+`ra[1]`+') AND (dec BETWEEN '+`dec[0]`+' AND '+`dec[1]`+'))'
  return query

    # discarded lines from the function above
    #ra = map(lambda x,y: x + y, (d['RAJ2000'], d['RAJ2000']), (-1 * size, size))
    #dec = map(lambda x,y: x + y, (d['DEJ2000'], d['DEJ2000']), (-1 * size, size))


def makeQArray(data, start, stop, step, size, fields):
  queries = []
  cur = start
  while cur < stop:
    if (cur-start)%100==0: print 'Starting Query number '+`cur-start`+' of '+`stop-start`
    if stop - cur < step: step = stop - cur # on the last on, and step won't be filled fully
    queries.append(makeSingleQ(data, cur, cur + step, size, fields))
    cur += step
  return queries

def saveQueries(filename, queries): # writes 1 query per line
  print 'Saving queries to ' + filename + '.txt'
  f = open(filename + '.txt', 'w')
  for q in queries:
    f.write(str(q) + '\n')
  f.close()

def executeQ(query,res): # returns a tuple of (results, modified) 
  lines = sqlcl.query(query).readlines()
  if lines[0][:-1] != '#Table1': # check if the query came back correctly
    print 'INCORRECT FORMAT RETURNED, returning previous results list'
    return (res, False)
  else:
    for l in lines[2:]:
      s = l[:-1].split(',')
      # NOTE: this line is heavily dependant on what we query, and in what order
      val = [float(s[0]),float(s[1]),int(s[2]),int(s[3]),float(s[4]),int(s[5]),float(s[6]),float(s[7]),float(s[8]),float(s[9])]
      res.append(val)
  return (res, True)

def saveResults(filename, results, fields):
  print 'Saving the Query Results to ' + filename + '.txt'
  f = open(filename+'.txt','w')
  f.write('[' + reduce(lambda x,y: str(x) + ', ' + str(y), fields) + ']\n')
  for r in results:
    f.write(str(r) + '\n')
  f.close()


# this function used to be much longer and annoying. if this ends up being broken, find old version in safe_place
# returns a tuple of arrays, where each array is ordered like data and will be a column
def matchEntries(data, results, region):

  # NOTE: in both arr_tup and val_tup, the names like arr_sID and bID are unnecessary,
  # but are being kept around for the time being to maintain clarity

  arr_tup = (arr_sID, arr_bID, arr_eBV, arr_eTEff, arr_eLogG, arr_eFeH, arr_eZ, arr_eZErr) = tuple([[] for i in range(8)])
  count = 0

  for d in data: # for each data entry look for an entry in result
    # set the default values --> use -9999 as it is sufficiently different from any regular value for all fields
    val_tup = (sID, bID, eBV, eTEff, eLogG, eFeH, eZ, eZErr) = tuple([-9999 for i in range(8)])
    #if count == 25: print val_tup #just to double check stuff

    for r in results:
      if isInRegion(r[0],r[1],d['RAJ2000'],d['DEJ2000'],region):
        # then these two points are the same

        val_tup = (r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9])
	#if count == 25: print val_tup
	results.remove(r)
	break

    map(lambda a,b: a.append(b), arr_tup,val_tup) # appends the values in val_tup to the arrays in arr_tup (may be -9999)
    
    #if count == 25: print arr_tup
    if count%1000==0: print 'on data elem' + `count` # like a progress bar
    count += 1

  print 'Finished matching entries' 
  return arr_tup

def curT():
  return int(round(time.time()))

def main():
  # open the fits file
  hdus = fits.open('bhbcatlog.fit')
  data = hdus[1].data

  # Define some variables that will be useful
  saveQ = True
  saveR = True
  execQ = True

  # these are the defaults, but will be changed if there are cmd args
  start = 0
  stop = data.size
  step = 10
  region_size = 0.0002777 # half square width in degrees

  if len(sys.argv) > 1: # cmd args present (should be in form start stop step)
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    step = int(sys.argv[3])
    print 'cmd start: ' +`start`+', stop: '+`stop`+', step: '+`step`
  
  # in theory there would be a better way to specify these values, and I'm sure there is a way to get the type
  # of the field without having to resort to just matching. for now though, it stays
  fields = ['ra','dec','specObjID','bestObjID','elodieBV','elodieTEff','elodieLogG','elodieFeH','elodieZ','elodieZErr']
  formats = [float,float,int,int,float,int,float,float,float,float]

  t1 = curT()
  queries = makeQArray(data, start, stop, step, region_size, fields)
  t2 = curT()
  print 'Time to make queries: '+`t2-t1`+' seconds'

  if saveQ:
    saveQueries('saved_queries', queries)

  results = []

  t3 = curT()
  #for i in range(len(queries)):
  for q in queries:
    if queries.index(q)%10 == 0: print 'Executing Query '+`queries.index(q)`+' of '+`len(queries)`
    results, modified = executeQ(q,results)
    if not modified:
      print 'Query could not be executed correctly'
  t4 = curT()
  print 'Time to execute all queries: '+`t4-t3`+' seconds'

  if saveR:
    saveResults('saved_results', results, fields)

  t5 = curT()
  res_tup = matchEntries(data,results,region_size)
  t6 = curT()
  print 'Time to match entries: '+`t6-t5`+' seconds'

  print len(res_tup[0])

  hdus.close()
  print 'done'

if __name__ == '__main__':
  main()
