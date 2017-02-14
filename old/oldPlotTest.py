import matplotlib.pyplot as plt
from astropy.io import fits

h = fits.open('combined.fits')
d = h[1].data

r1 = d['RAJ2000'][0:100]
d1 = d['DEJ2000'][0:100]
r2 = d['ra'][0:100]
d2 = d['dec'][0:100]
r3 = r2-r1
d3 = d2-d1

print r1[0:10]
print r2[0:10]
print r3[0:10]

plt.figure(1)
plt.subplot(211)
p = plt.plot(range(len(r3)), abs(r3), 'bs', range(len(d3)), abs(d3), 'ro')

plt.subplot(212)
plt.plot(r1,d1,'ro',r2,d2,'bs')
plt.show()

