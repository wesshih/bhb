from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import util
from scipy import stats
import numpy as np

data = fits.open('Sightline.fits')[1].data
#data = fits.open('../combined.fits')[1].data

mask = data['spp.TEFFANNRR'] > 0
fil_data = data[mask][:1000]

delta = []
deltar = []
dist = []

pos_data = [[],[],[]]

print 'beginning...'
for i in range(fil_data.size):
  if i % 100 == 0:
    print `i` + '/' + `fil_data.size`
  bhb = fil_data[i]
  #util.print_bhb(bhb,i)
  (o,r,g) = util.compare_color(bhb)
  if g-o <= 1: # 0.75:
    delta.append(g-o)
    deltar.append(g-r)
    dist.append(bhb['d'])
  if g-o > 0:
    pos_data[0].append(bhb['spp.TEFFANNRR'])
    pos_data[1].append(bhb['spp.LOGGANNRR'])
    pos_data[2].append(bhb['spp.FEHANNRR'])

f = open('Sightline.txt','w')
for i in range(len(dist)):
  f.write(`dist[i]`+','+`delta[i]`+'\n')
f.close()

print 'doing stats'
m, b, r, p, err = stats.linregress(dist,deltar)
print 'm: ' + `m`
print 'b: ' + `b`
print 'r: ' + `r`
print 'p: ' + `p`
print 'err: ' + `err`

print '------------------------------'
print 'averages of population'
print 'avg teff: ' + `np.mean(fil_data['spp.TEFFANNRR'])`
print 'avg logg: ' + `np.mean(fil_data['spp.LOGGANNRR'])`
print 'avg fe/h: ' + `np.mean(fil_data['spp.FEHANNRR'])`
print ' '
print 'average of bhb with delta_g-r > 0'
print 'avg teff: ' + `np.mean(pos_data[0])`
print 'avg logg: ' + `np.mean(pos_data[1])`
print 'avg fe/h: ' + `np.mean(pos_data[2])`
print 'num of bhbs: ' + `len(pos_data[0])`


linePlot = plt.plot([min(dist),max(dist)],[min(dist)*m + b, max(dist)*m +b],label=`b`)

plt.scatter(dist,delta,marker='o',color='red')
#plt.scatter(dist,deltar,marker='o',color='blue')

#plt.legend(handles=[linePlot], loc=1)
plt.legend()


#linePlot.text(0.05, 0.95, 'hello',verticalalignment='top')

plt.show()


print 'done.'

'''
bhb = data[1045]
util.print_bhb(bhb,1045)
(o,r,g) = util.compare_color(bhb)
print `o-g`
'''
