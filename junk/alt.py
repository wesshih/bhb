from astropy.io import fits
import sqlcl as sql
import sys
import time

curT = lambda: int(round(time.time()))

region = 0.0002777 # half square width in degrees

hdus = fits.open('bhbcatlog.fit')
data = hdus[1].data

size = 500 #data.size
executeQuery = True

res = []

t1 = curT()

for i in range(size):
  if i % 10 == 0:
    print "on iteration " + `i`
  ra = data[i]['RAJ2000']
  dec = data[i]['DEJ2000']
  query = "SELECT p.objID, p.ra, p.dec\nFROM PhotoPrimary p, fGetNearbyObjEq("+`ra`+","+`dec`+",0.02) n \nWHERE p.objID=n.objID"

  #f1 = open("altQ/qText"+`i`+".txt", "w+")
  #f1.write(query)
  #f1.close()

  if executeQuery:
    lines = sql.query(query).readlines()
    if lines[0][0:-1] != "#Table1":
      print "INCORRECT FORMAT RETURNED"
    else:
      for line in lines[2:]:
        splitLine = line[:-1].split(',')
        res.append([int(splitLine[0]),float(splitLine[1]),float(splitLine[2])])

t2 = curT()

f2 = open("altQ/results.txt", "w+")
f2.write("[objID, ra, dec]\n")
for r in res:
  f2.write(str(r)+'\n')
f2.close()

print "execution time: " + `t2 - t1`

print "finished"
hdus.close()
