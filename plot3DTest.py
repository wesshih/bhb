from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from astropy.io import fits

data = fits.open('combined.fits')[1].data
sx = []
sy = []
sz = []

for i in range(3000):
  sx.append(data[i]['x'])
  sy.append(data[i]['y'])
  sz.append(data[i]['z'])

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#x = [1,2,3,4,5,6,7,8,9,10]
#y = [5,6,7,8,1,2,4,3,9,0]
#z = [2,2,2,5,0,14,3,8,9,10]

ax.scatter(sx,sy,sz,c='r',marker='o')
#ax.plot(sx,sy,sz)

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_zlabel('z label')

plt.show()
