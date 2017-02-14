from astropy.io import fits

data = fits.open('combined.fits')[1].data

f = open('StarParams.txt','w')

star = data[0]
cols = data.columns.names

for c in cols:
  f.write(c + ':' + str(star[c]) + '\n')

f.close()
