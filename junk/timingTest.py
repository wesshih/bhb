import sqlcl as s
import time

curT = lambda: int(round(time.time() * 1000))

times1 = []
times2 = []

num = 30

for i in range(num):
  print "starting test " + `i`

  t1 = curT()
  r1 = s.query("SELECT objID, ra, dec  FROM PhotoPrimary WHERE ((ra BETWEEN 331.04711618888882 AND 331.04767158888887) AND (dec BETWEEN 6.2921503555555551 AND 6.2927057555555548))").read()
  t11 = curT()
  times1.append(t11-t1)
  
  t2 = curT()
  r2 = s.query("SELECT p.objid, p.ra, p.dec FROM fGetNearbyObjEq(331.047393889,6.29242805556,0.02) n, PhotoPrimary p WHERE n.objID=p.objID").read()
  t22 = curT()
  times2.append(t22-t2)
  
avg1 = sum(times1)/num
avg2 = sum(times2)/num

print "Results for 1"
print times1
print "average: " + `avg1`
print '\n'
print "Results for 2"
print times2
print "average: " + `avg2`
