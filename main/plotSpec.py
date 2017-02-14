import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np
import pysynphot as S
import bhb
import math

# data = fits.open('models/phoenix/phoenixm00/phoenixm00_7600.fits')[1].data
# w = np.array(data['WAVELENGTH'])
# f = np.array(data['g30'])

# sp = S.ArraySpectrum(w,f,name='MySource')

# sp2 = S.Icat('phoenix',7600,0,3.0)
# sp3 = S.Icat('phoenix',7500,0,3.0)

# plt.subplot(311).plot(sp.wave,sp.flux,c='b',alpha=0.75)
# plt.subplot(312).plot(sp2.wave,sp2.flux,c='b',alpha=0.75)
# plt.subplot(313).plot(sp3.wave,sp3.flux,c='b',alpha=0.75)
# plt.subplot(311).set_xlim(2000,12000)
# plt.subplot(312).set_xlim(2000,12000)
# plt.subplot(313).set_xlim(2000,12000)
# plt.show()

plt.figure(figsize=(10,10))

data = fits.open('models/phoenix/phoenixm15/phoenixm15_8200.fits')[1].data
w = np.array(data['WAVELENGTH'])
f1 = np.array(data['g30'])
f2 = np.array(data['g35'])

IDs = [1237678845037641777,1237662301908172849,1237662301907714150,
       1237662301370712106,1237662474232135716]

bhbs = bhb.load('BHB_DATA_P.txt')
bs = [b for b in bhbs if b.objID in IDs]
print len(bs)
colors = ['b','r','g','cyan','brown']


# plt.subplot(211).plot(w,f1,c='gray',alpha=0.5)
# plt.subplot(211).plot(w,f2,c='black',alpha=0.5)

for i in range(len(bs)):
	b = bs[i]
	s = S.Icat('phoenix',b.teff,b.feh,b.logg)
	# plt.subplot(111).plot(s.wave, s.flux,c='b',alpha=0.6)
	s1 = S.Icat('ck04models',b.teff,b.feh,b.logg)
	# plt.subplot(111).plot(s1.wave, s1.flux,c='r',alpha=0.6)
	s2 = S.Icat('k93models',b.teff,b.feh,b.logg)
	# plt.subplot(111).plot(s2.wave, s2.flux,c='g',alpha=0.6)

# plt.subplot(212).plot(w,f1,c='blue',alpha=0.5)
# plt.subplot(212).plot(w,f2,c='red',alpha=0.5)

plt.subplot(111).set_xlim(3000,9500)
# plt.subplot(212).set_xlim(1000,10000)

hdu1 = fits.open('models/bhb1_actual.fits')
data1 = hdu1[1].data
c0 = hdu1[0].header['COEFF0']
c1 = hdu1[0].header['COEFF1']
stepa = (9221.467-3802.769)/len(data1)
xsa = [3802.769 + i*stepa for i in range(len(data1))]
ysa = [y * 1000000 for y in data1['flux']]

xsa2 = [10**(c0 + c1*i) for i in range(len(data1['flux']))]
ysa2 = [y * (10**6) for y in data1['flux']]

# plt.subplot(212).plot(xsa,ysa,c='b',alpha=0.75)
# plt.subplot(212).plot(xsa2,ysa2,c='r',alpha=0.75)
plt.subplot(111).plot(xsa2,ysa2,c='gray',alpha=0.75)


datac = fits.open('models/t08250_g+3.0_m13p04_hr.fits')[0].data
stepc = (9000.0-2500.0)/len(datac)
print len(datac)
print stepc
xsc = [2500.0+i*stepc for i in range(len(datac))]
ysc = [y * 1 /1 for y in datac]
plt.subplot(111).plot(xsc,ysc,c='orange',alpha=0.5)

sp = S.ArraySpectrum(np.array(xsc),np.array(ysc))
g = S.Observation(sp, S.ObsBandpass('sdss,g'))
r = S.Observation(sp, S.ObsBandpass('sdss,r'))
gr = g.effstim('abmag') - r.effstim('abmag')


datac2 = fits.open('models/t08250_g+3.0_m13p04_sed.fits')[0].data
stepc2 = (1000000 - 1300.0)/len(datac2)
xsc2 = np.array([13+i*stepc2 for i in range(len(datac2))])
ysc2 = np.array(datac2)
res = 8 * (10 ** -4)
ws = [1300]
for i in range(len(datac2)-1):
	ws.append(math.pow(10,res + math.log10(ws[-1])))

print ws[:10]
print ws[len(ws)-10:]
print len(ws)
print len(ysc2)



sp2 = S.ArraySpectrum(np.array(ws),ysc2)
g2 = S.Observation(sp2, S.ObsBandpass('sdss,g'))
r2 = S.Observation(sp2, S.ObsBandpass('sdss,r'))
gr2 = g2.effstim('abmag') - r2.effstim('abmag')

obs = bs[2].obs_gr
gen = bs[2].gen_gr

print 'obs: ' + `obs`
print 'gen: ' + `gen`
print 'coelho1: ' + `gr`
print 'coelho2: ' + `gr2`
print 'dif1: ' + `gen - obs`
print 'dif2: ' + `gr - obs`
print 'dif3: ' + `gr2 - obs`

plt.subplot(111).plot(sp.wave,sp.flux,c='g',alpha=0.5)
plt.subplot(111).plot(sp2.wave,sp2.flux,c='r',alpha=0.5)
# plt.subplot(212).set_xlim(1000,10000)

for bb in bs:
	print bb.dif_gr

plt.show()