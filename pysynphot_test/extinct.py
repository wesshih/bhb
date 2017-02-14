from astropy.io import fits
import pysynphot as S
import matplotlib.pyplot as plt
import numpy as np

def cal_color(sp):
  obs_g = S.Observation(sp, S.ObsBandpass('sdss,g'))
  obs_r = S.Observation(sp, S.ObsBandpass('sdss,r'))
  return obs_g.effstim('abmag') - obs_r.effstim('abmag')


data = fits.open('../combined.fits')[1].data
names = data.columns.names

#filter out any elements that dont have good indicators
print 'before'
dat_fil = [dict(zip(names, list(e))) for e in data if e['spp.TEFFANNRRIND']==1 and e['spp.LOGGANNRRIND']==1 and e['spp.FEHANNRRIND']==2]
#dat_fil = np.array(dat_fil_ar)
print 'after'
num = 10
index = 2234

i_gr = []
o_gr = []
dis = []

print 'here'

for i in range(num):
  print i
  sp = S.Icat('phoenix', dat_fil[index+i]['spp.TEFFANNRR'],dat_fil[index+i]['spp.FEHANNRR'],dat_fil[index+i]['spp.LOGGANNRR'])
  i_gr.append(cal_color(sp))
  o_gr.append(dat_fil[index+i]['photo.g'] - dat_fil[index+i]['photo.r'])
  dis.append(dat_fil[index+i]['d'])

dif = map(lambda x,y: x-y, i_gr, o_gr)

print(i_gr)
print(o_gr)
print(dif)
print(dis)
