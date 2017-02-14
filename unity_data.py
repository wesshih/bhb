from astropy.io import fits

data = fits.open('pysynphot_test/sightline.fits')[1].data
f = open('UnityData_sightline.txt','w')

f.write(reduce(lambda x,y: x+','+y,data.columns.names)+'\n')

for d in data:
  f.write(reduce(lambda x,y: x+','+str(y),d[1:],str(d[0]))+'\n')
#for d in data:
#  f.write(str(list(d))[1:-1] +'\n')

print 'done.'
