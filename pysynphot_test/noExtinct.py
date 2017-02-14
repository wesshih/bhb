import matplotlib as plt
from astropy.io import fits
import util
import numpy as np

data = util.getCombined()

# looking for bhb with spec.g roughly equal to spec.dered_g

mask = data['spp.TEFFANNRR'] > 0
fil_data = data[mask]

bhbs = []

num = fil_data.size

for i in range(num):
  g = fil_data[i]['photo.g']
  r = fil_data[i]['photo.r']
  dg = fil_data[i]['photo.dered_g']
  dr = fil_data[i]['photo.dered_r']
  g_r = g-r
  dg_r = dg-dr

  delg = g - dg
  delr = r - dr
  delg_r = g_r - dg_r

  if delg < 0.05 and fil_data[i]['d'] < 10:
    print 'delg: ' + `delg`
    print '-->  delr: ' + `delr`
    print '-->  delg_r: ' + `delg_r`
    print '-->  dist: ' + `fil_data[i]['d']`
    print '-->  logg: ' + `fil_data[i]['spp.LOGGANNRR']`
    print '-->  fe/h: ' + `fil_data[i]['spp.FEHANNRR']`
    print '-->  teff: ' + `fil_data[i]['spp.TEFFANNRR']`

    logg = fil_data[i]['spp.LOGGANNRR']
    feh = fil_data[i]['spp.FEHANNRR']
    teff = fil_data[i]['spp.TEFFANNRR']

    #gen_g,gen_r = util.cal_color(teff,feh,logg)
    #gen_gr = gen_g - gen_r
    #print '-->  gen_g: ' + `gen_g`
    #print '-->  gen_r: ' + `gen_r`
    gen_gr = util.cal_color(teff,feh,logg)
    print '-->  gen_gr: ' + `gen_gr`
    print '-->  g_r: ' + `g_r`
    print '-->  dg_r: ' + `dg_r`
    print '-->  del_gen: ' + `gen_gr - g_r`

    bhbs.append(fil_data[i])
print ' '
print 'num of bhbs: ' + `len(bhbs)`
print '--------------------------'

print 'averages of population'
print 'avg teff: ' + `np.mean(fil_data['spp.TEFFANNRR'])`
print 'avg logg: ' + `np.mean(fil_data['spp.LOGGANNRR'])`
print 'avg fe/h: ' + `np.mean(fil_data['spp.FEHANNRR'])`


bhb_t = []
bhb_g = []
bhb_f = []
for b in bhbs:
  bhb_t.append(b['spp.TEFFANNRR'])
  bhb_g.append(b['spp.LOGGANNRR'])
  bhb_f.append(b['spp.FEHANNRR'])

print '***********'
print 'averages of subset'
print 'teff: ' + `np.mean(bhb_t)`
print 'logg: ' + `np.mean(bhb_g)`
print 'fe/h: ' + `np.mean(bhb_f)`



