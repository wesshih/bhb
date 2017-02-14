from astropy.io import fits
import numpy as np

hdus = fits.open('bhbcatlog.fit')

data = hdus[1].data

print type(data)

oldCol = data.columns

ar1 = []
ar2 = []
for i in range(len(data)):
  ar1.append(i)
  ar2.append(float(i) + 0.3)

cols = [fits.Column(name='AR1',format='I',array=ar1), fits.Column(name='AR2', format='D',array=ar2)]
newCol = fits.ColDefs(cols)

newHDU = fits.BinTableHDU.from_columns(oldCol + newCol)
newHDU.writeto('combined.fits')
#newHDU.close()

#col = fits.Column(name='BLAH',format='I', array=np.array(ar))
#print col
#print "\n"
#
#data.columns.add_col(col)
#
#print data.columns
#
#hdus[1].update()
#
#print data[2]
#print data.field('RAJ2000')
##data.setfield('BLAH',int(69))
#print data[2]['BLAH']

#hdus.writeto('modified.fits')

hdus.close()
