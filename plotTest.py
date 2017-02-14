import matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

start = 0
end = 50
part = False

#data = fits.open('combined_7_11.fits')[1].data
data = fits.open('combined.fits')[1].data

ras = []
decs = []
unra = []
undec = []

for d in (data[start:end] if part else data):
  if d['spec.ra'] != -9999:
    # this bhb was actually found in query
    ra,dec = d['spec.ra'],d['spec.dec']
    unra.append(d['spec.ra'])
    undec.append(d['spec.dec'])
    if ra > 180: ra -= 360
    ras.append(ra)
    decs.append(dec)

print ras[:10]


plt.figure(figsize = (16,12))
#ax = plt.subplot(211,projection='mollweide',axisbg='lightcyan')
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=2,projection='mollweide',axisbg='black')
#ax1.scatter(np.radians(ras),np.radians(decs),marker='.',c='red')
ax1.scatter(np.radians(ras),np.radians(decs),marker=matplotlib.markers.MarkerStyle(marker='o',fillstyle='full'),c='red',edgecolor='black',s=25)
ax1.tick_params(labelsize=15,labelcolor='white') #,direction='in')

ax2 = plt.subplot2grid((3,3),(2,0),colspan=3,axisbg='white')
ax2.plot(unra,undec,'ro')
ax2.set_xlim([0,360])
ax2.set_ylim([-90,90])
ax2.set_xlabel('RA')
ax2.xaxis.label.set_fontsize(10)
#for tick in ax2.xaxis.get_major_ticks():
  #tick.label.set_fontsize(15)
#ax2.xaxis.get_major_ticks().label.set_fontsize(8)
ax2.set_ylabel('DEC')
ax2.yaxis.label.set_fontsize(10)
#plt.tick_params(labelsize=20)
ax2.tick_params(labelsize=15)
plt.show()
