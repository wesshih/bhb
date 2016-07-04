from astropy.io import fits
import sqlcl
import sys
import time

# Global parameters for things like Debug and Timing output
debug = False
timing = True
verbose = False
showProg = True

#determines if point b is in square region of 2*size on a side centered at point a
def isInRegion(ra, dec, ra_center, dec_center, size): 
  if (ra < ra_center + size) and (ra > ra_center - size):
    if (dec < dec_center + size) and (dec > dec_center - size):
      return True
  return False

def makeSingleQ(data, start, stop, size, fields):
  if debug: print 'Making Single Query that starts at '+`start`+' and stops at '+`stop`
  query = 'SELECT ' + reduce(lambda x,y: str(x) + ', ' + str(y),fields) + ' FROM specObj WHERE'
  needOR = False # Need to add ORs for multiple BHBs after the first entry
  for d in data[start : stop]:
    ra = (d['RAJ2000']-size,d['RAJ2000']+size)
    dec = (d['DEJ2000']-size,d['DEJ2000']+size)
    if needOR: query += ' OR '
    else: needOR = True # will need it if there are any addition elems to add
    query += '((ra BETWEEN '+`ra[0]`+' AND '+`ra[1]`+') AND (dec BETWEEN '+`dec[0]`+' AND '+`dec[1]`+'))'
  return query

    # discarded lines from the function above
    # this next line is soo unnecessarily complicated. keep it here for now because its funny
    #(ra,dec) = map(lambda x,y: (x[0]+y[0],x[1]+y[1]),[[d['RAJ2000']]*2,[d['DEJ2000']]*2],[[-1*size,size]]*2)
    #ra = map(lambda x,y: x + y, (d['RAJ2000'], d['RAJ2000']), (-1 * size, size))
    #dec = map(lambda x,y: x + y, (d['DEJ2000'], d['DEJ2000']), (-1 * size, size))


def makeQArray(data, start, stop, step, size, fields):
  queries = []
  cur = start
  while cur < stop:
    #if showProg and (cur-start)%100==0: print 'Starting Query number '+`cur-start`+' of '+`stop-start`
    if showProg: printNL('\rCreating Queries...\t%.2f%%'%(((cur-start)*100.0)/(stop-start)))
    if stop - cur < step: step = stop - cur # on the last on, and step won't be filled fully
    queries.append(makeSingleQ(data, cur, cur + step, size, fields))
    cur += step
  return queries

def saveQueries(filename, queries): # writes 1 query per line
  if verbose: print 'Saving queries to ' + filename + '.txt'
  f = open(filename + '.txt', 'w')
  for q in queries:
    f.write(str(q) + '\n')
  f.close()

def executeQ(query,res,formats): # returns a tuple of (results, modified) 
  lines = sqlcl.query(query).readlines()
  if lines[0][:-1] != '#Table1': # check if the query came back correctly
    print 'INCORRECT FORMAT RETURNED, returning previous results list'
    return (res, False)
  else:
    for l in lines[2:]:
      s = l[:-1].split(',')
      # NOTE: the formats array must exactly match the format of the returned data
      val = map(lambda x,y: x(y), formats, s)
      res.append(val)
  return (res, True)

def saveResults(filename, results, fields):
  if verbose: print 'Saving the Query Results to ' + filename + '.txt'
  f = open(filename+'.txt','w')
  f.write('[' + reduce(lambda x,y: str(x) + ', ' + str(y), fields) + ']\n')
  for r in results:
    f.write(str(r) + '\n')
  f.close()


# this function used to be much longer and annoying. if this ends up being broken, find old version in safe_place
# returns a tuple of arrays, where each array is ordered like data and will be a column
def matchEntries(data, results, region):

  numFields = len(results[0])

  # NOTE: in both arr_tup and val_tup, the names like arr_sID and bID are unnecessary,
  # but are being kept around for the time being to maintain clarity
  #arr_tup = (arr_ra, arr_dec, arr_sID, arr_bID, arr_eBV, arr_eTEff, arr_eLogG, arr_eFeH, arr_eZ, arr_eZErr) = tuple([[] for i in range(11)])
  arr_tup = tuple([[] for i in range(numFields)])
  count = 0

  for d in data: # for each data entry look for an entry in result
    if showProg: printNL('\rMatching Entries...\t%.2f%%'%((count*100.0)/len(data)))
    # set the default values --> use -9999 as it is sufficiently different from any regular value for all fields
    #val_tup = (ra, dec, sID, bID, eBV, eTEff, eLogG, eFeH, eZ, eZErr) = tuple([-9999 for i in range(11)])
    val_tup = tuple([-9999 for i in range(numFields)])
    #if count == 25: print val_tup #just to double check stuff

    for r in results:
      if isInRegion(r[0],r[1],d['RAJ2000'],d['DEJ2000'],region):
        # then these two points are the same

        val_tup = r[0:numFields] #(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10])
	#if count == 25: print val_tup
	results.remove(r)
	break

    map(lambda a,b: a.append(b), arr_tup,val_tup) # appends the values in val_tup to the arrays in arr_tup (may be -9999)
    
    count += 1

  return arr_tup

# for now it will always overwrite a fits file of the same name (if it exists)
def makeNewFits(filename, data, fields, formats, arr_tup):
  # first lets convert the formats to the nedded 'I' or 'D' or whatever
  # really simple for now, i can expand on this if i need to
  # NOTE: for now only can deal with ints and doubles, and makes everything else into 30-char string
  fmts = map(lambda x: 'D' if x == float else ('K' if x == int else '30A'), formats)

  newCols = []

  # now construct the new columns
  for i in range(len(fields)):
    col = fits.Column(name=fields[i], format=fmts[i], array=arr_tup[i])
    newCols.append(col)

  newColDefs = fits.ColDefs(newCols)

  oldCols = data.columns

  newHDU = fits.BinTableHDU.from_columns(oldCols + newColDefs)
  newHDU.writeto(filename+'.fits',clobber=True)
  

def curT():
  return int(round(time.time()))

# prints to the console without new line
def printNL(message):
  sys.stdout.write(message)
  sys.stdout.flush()

def main():
  t_top = curT() #this is the time at the very top

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
    if debug: print 'cmd line args. start: ' +`start`+', stop: '+`stop`+', step: '+`step`
  
  # in theory there would be a better way to specify these values, and I'm sure there is a way to get the type
  # of the field without having to resort to just matching. for now though, it stays
  fields = ['ra','dec','specObjID','bestObjID','elodieBV','elodieTEff','elodieLogG','elodieFeH','elodieZ','elodieZErr', 'elodieObject','elodieSpType','elodieFileName']
  formats = [float,float,int,int,float,int,float,float,float,float,str,str,str]

  printNL('Creating Queries...')
  t_start = curT()
  queries = makeQArray(data, start, stop, step, region_size, fields)
  t_end = curT()
  printNL('\rCreating Queries...\tdone' + (', in '+`t_end-t_start`+' seconds.\n' if timing else '.\n'))

  if saveQ:
    saveQueries('saved_queries', queries)

  printNL('Executing Queries...')
  t_start = curT()
  results = []
  for q in queries:
    if showProg and queries.index(q)%1 == 0:
      printNL('\rExecuting Queries...\t%.2f%%'%((queries.index(q)*100.0)/len(queries)))
    results, modified = executeQ(q,results,formats)
    if not modified:
      printNL('\nQuery '+`queries.index(q)`+' could not be executed correctly')
  t_end = curT()
  printNL('\rExecuting Queries...\tdone' + (', in '+`t_end-t_start`+' seconds.\n' if timing else '.\n'))

  if saveR:
    saveResults('saved_results', results, fields)

  printNL('Matching Entries...')
  t_start = curT()
  res_tup = matchEntries(data,results,region_size)
  t_end = curT()
  printNL('\rMatching Entries\tdone' + (', in '+`t_end-t_start`+' seconds.\n' if timing else '.\n'))

  printNL('Creating New Fits...')
  t_start = curT()
  makeNewFits('combined',data,fields,formats,res_tup)
  t_end = curT()
  printNL('\tdone' + (', in '+`t_end-t_start`+' seconds.\n' if timing else '.\n'))

  hdus.close()

  t_bot = curT() # this is the time at the very bottom
  printNL('Finished execution without error' + (' in '+`t_bot-t_top`+' seconds.\n' if timing else '\n'))

if __name__ == '__main__':
  main()
