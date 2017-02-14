from astropy.io import fits
import matplotlib.pyplot as plt

data = fits.open('combined.fits')[1].data

tmp_dat = data['spp.TEFFANNRR']
tmp_dat_ind = data['spp.TEFFANNRRIND']
g_dat = data['spp.LOGGANNRR']
g_dat_ind = data['spp.LOGGANNRRIND']
fe_dat = data['spp.FEHANNRR']
fe_dat_ind = data['spp.FEHANNRRIND']
dist = data['d']

tmps = [e for e in tmp_dat if e > 0]
fil_tmps = [e[0] for e in zip(tmp_dat,tmp_dat_ind) if e[1]==1]

gs = [e for e in g_dat if e > -9999]
fil_gs = [e[0] for e in zip(g_dat,g_dat_ind) if e[1]==1]

fes = [e for e in fe_dat if e > -9999]
fil_fes = [e[0] for e in zip(fe_dat,fe_dat_ind) if e[1]==2]

fes_dist = [(e[0],e[2]) for e in zip(fe_dat,fe_dat_ind,dist) if e[1] == 2]
fedist_fe,fedist_dist = zip(*fes_dist)

print len(fes)
print len(fil_fes)

plotSize = 410

plt.figure(figsize = (16,12))

ax1 = plt.subplot(plotSize + 1)
ax1.hist(tmps,50)
ax1.hist(fil_tmps,50)
ax1.set_xlabel('Teff ANNRR')
ax1.set_ylabel('Count')

ax2 = plt.subplot(plotSize + 2)
ax2.hist(gs,bins=50)
ax2.hist(fil_gs,bins=50)
ax2.set_xlabel('LogG ANNRR')
ax2.set_ylabel('Count')

ax3 = plt.subplot(plotSize + 3)
ax3.hist(fes,bins=50)
ax3.hist(fil_fes,bins=50)
ax3.set_xlabel('LogG ANNRR')
ax3.set_ylabel('Count')

ax4 = plt.subplot(plotSize + 4)
ax4.scatter(fedist_dist,fedist_fe)
ax4.set_ylabel('Fe/H')
ax4.set_xlabel('dist')

plt.show()

#print data['spec.ra'][:10]
