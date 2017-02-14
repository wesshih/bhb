import pysynphot as S
from astropy.io import fits
import numpy as np
import os
import matplotlib.pyplot as plt

vega_file = os.path.join(os.environ['PYSYN_CDBS'],'calspec','bd29d2091_stis_003.fits')

vega = S.FileSpectrum(vega_file)
vega.convert('flam')

obs1 = S.Observation(vega, S.ObsBandpass('sdss,g'))
obs2 = S.Observation(vega, S.ObsBandpass('sdss,r'))
gr = obs1.effstim('abmag') - obs2.effstim('abmag')

vega2 = S.Icat('phoenix', 5800, 0.02, 1.44) # this is actually the sun

#vega2 = S.Icat('phoenix', 5800, -2.0, 4.1)
obs3 = S.Observation(vega2, S.ObsBandpass('sdss,g'))
obs4 = S.Observation(vega2, S.ObsBandpass('sdss,r'))
gr2 = obs3.effstim('abmag') - obs4.effstim('abmag')

print('the g-r color of Vega is: ' + `gr`)
print('the g-r color of Vega2 is: ' + `gr2`)

v1_norm = vega.renorm(1, 'abmag', S.ObsBandpass('sdss,u'))
v2_norm = vega2.renorm(1, 'abmag', S.ObsBandpass('sdss,u'))


#plt.plot(vega.wave, vega.flux,'r')
#plt.plot(vega2.wave, vega2.flux,'b')
plt.plot(v1_norm.wave, v1_norm.flux,'r',label='v1_norm')
plt.plot(v2_norm.wave, v2_norm.flux,'b',label='v2_norm')
plt.xlim(0,10000)
plt.legend(loc='best')
plt.show()
