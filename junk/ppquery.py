from astropy.io import fits
import sqlcl as sql
import sys
import time

curT = lambda: int(round(time.time()))

region = 0.0002777 # half square width in degrees

printQueries = True
printResults = True
executeQuery = True

hdus = fits.open('bhbcatlog.fit')
data = hdus[1].data

res = []
count = 0 # from
size = data.size # to
queryLimit = 10 # step

if len(sys.argv) > 1:
  count = int(sys.argv[1])
  size = int(sys.argv[2])
  queryLimit = int(sys.argv[3])

t1 = curT()

while count < size:
  print "Progress: " + `count` + "/" + `size`
  query = "SELECT objID, ra, dec\nFROM PhotoPrimary\nWHERE"
  needOR = False #Need to add ORs for multiple BHBss
  if size - count < queryLimit:
    queryLimit = size - count
  for i in range(count, count + queryLimit):
    ra = data[i]['RAJ2000']
    dec = data[i]['DEJ2000']
    if needOR:
      query = query + "\nOR"
    else:
      needOR = True
    query = query + " ((ra BETWEEN " + `ra - region` + " AND " + `ra + region` + ") AND (dec BETWEEN " + `dec - region` + " AND " + `dec + region` + "))"
  if printQueries:
    f1 = open("queryText/ppqueryText"+`count`+".txt", "w")
    f1.write(query)
    f1.close()
    print "written " + `count`

  if executeQuery:
    lines = sql.query(query).readlines()
    #res = []
    if lines[0][0:-1] != "#Table1":
      print "INCORRECT FORMAT RETURNED"
    else:
      extra = False
      if len(lines[2:]) > queryLimit:
        print "this query has extras"
        extra = True
      for line in lines[2:]:
        splitLine = line[:-1].split(',')
	arr = [int(splitLine[0]),float(splitLine[1]),float(splitLine[2])]
	if extra:
	  arr.append("-----")
        res.append(arr)
      if extra:
        extra = False
      #f2 = open("queryRes/queryRes"+`count`+".txt", "w+")
      #f2.write("[objID, ra, dec]\n")
      #for r in res:
      #  f2.write(str(r)+'\n')
      #f2.write(str(res))
      #f2.close()

    #print "e " + `count`

  count = count + queryLimit

t2 = curT()

if printResults:
  f2 = open("queryRes/ppresults.txt",'w')
  f2.write("[objID, ra, dec]\n")
  for r in res:
    f2.write(str(r)+'\n')
  f2.close()
  print "r " + `count`

print "execution time: " + `t2 - t1`

hdus.close()
print "finished"
