from astropy.io import fits
import matplotlib.pyplot as plt


data = fits.open('combined.fits')[1].data

left, width = 0, 20
botom, height = -90, 10

r = data['s.ra'][0:10]
d = data['s.dec'][0:10]

plt.plot(r,d)
plt.show()
