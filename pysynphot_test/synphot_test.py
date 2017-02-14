import matplotlib.pyplot as plt
import numpy as np
import pysynphot as S
from astropy.io import fits

data = fits.open('../combined.fits')[1].data
index = 3345
temp = data['spp.TEFFANNRR'][index]
logg = data['spp.LOGGANNRR'][index]
feh = data['spp.FEHANNRR'][index]

if False:
  for i in range(10):
    temp = data['spp.TEFFANNRR'][index+i]
    logg = data['spp.LOGGANNRR'][index+i]
    feh = data['spp.FEHANNRR'][index+i]
    sp = S.Icat('phoenix',temp,feh,logg)
    sp_norm = sp.renorm(1, 'abmag', S.ObsBandpass('sdss,u'))
    plt.plot(sp.wave,sp.flux,label="BHB "+`index+i`)
else:  
  sun = S.Icat('phoenix',6000,-1.2,1.45)
  norm_u = sun.renorm(1, 'abmag', S.ObsBandpass('sdss,u'))
  norm_g = sun.renorm(1, 'abmag', S.ObsBandpass('sdss,g'))
  norm_r = sun.renorm(1, 'abmag', S.ObsBandpass('sdss,r'))
  norm_i = sun.renorm(1, 'abmag', S.ObsBandpass('sdss,i'))
  norm_z = sun.renorm(1, 'abmag', S.ObsBandpass('sdss,z'))
  
  
  #plt.plot(sun.wave, sun.flux, 'purple', label='u')
  plt.plot(norm_u.wave, norm_u.flux, 'purple', label='u')
  plt.plot(norm_g.wave, norm_g.flux, 'green', label='g')
  plt.plot(norm_r.wave, norm_r.flux, 'red', label='r')
  plt.plot(norm_i.wave, norm_i.flux, 'blue', label='i')
  plt.plot(norm_z.wave, norm_z.flux, 'orange', label='z')

plt.xlim(3000,10000)
plt.xlabel('Angstroms')
plt.ylabel('flam')
plt.legend(loc='best')
plt.show()

