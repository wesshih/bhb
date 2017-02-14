import matplotlib.pyplot as plt
import bhb

unfil_bhbs = bhb.load('BHB_DATA_P_irfm.txt')
print(len(unfil_bhbs))
bhbs = [b for b in unfil_bhbs if b.feh_annsr > -100 and b.feh_ngs1 > -100 and b.feh_irfm > -100]
print(len(bhbs))

xs = range(len(bhbs))
teff_annrr = [b.teff for b in bhbs]
teff_annsr = [b.teff_annsr for b in bhbs]
teff_ngs1 = [b.teff_ngs1 for b in bhbs]
teff_irfm = [b.teff_irfm for b in bhbs]

logg_annrr = [b.logg for b in bhbs]
logg_annsr = [b.logg_annsr for b in bhbs]
logg_ngs1 = [b.logg_ngs1 for b in bhbs]
logg_irfm = [b.logg_irfm for b in bhbs]

feh_annrr = [b.feh for b in bhbs]
feh_annsr = [b.feh_annsr for b in bhbs]
feh_ngs1 = [b.feh_ngs1 for b in bhbs]
feh_irfm = [b.feh_irfm for b in bhbs]

size = (10,10)

plt.figure(1,figsize=size)
plt.subplot(221).scatter(xs,teff_annrr,c='b',alpha=0.65)
plt.subplot(221).set_xlabel('annrr')
plt.subplot(222).scatter(xs,teff_annsr,c='r',alpha=0.65)
plt.subplot(222).set_xlabel('annsr')
plt.subplot(223).scatter(xs,teff_ngs1,c='g',alpha=0.65)
plt.subplot(223).set_xlabel('ngs1')
plt.subplot(224).scatter(xs,teff_irfm,c='cyan',alpha=0.65)
plt.subplot(224).set_xlabel('irfm')
for i in range(4):
	plt.subplot(221+i).set_ylabel('teff')
	plt.subplot(221+i).set_ylim(7000,10000)


plt.figure(2,figsize=size)
plt.subplot(221).scatter(xs,logg_annrr,c='b',alpha=0.65)
plt.subplot(221).set_xlabel('annrr')
plt.subplot(222).scatter(xs,logg_annsr,c='r',alpha=0.65)
plt.subplot(222).set_xlabel('annsr')
plt.subplot(223).scatter(xs,logg_ngs1,c='g',alpha=0.65)
plt.subplot(223).set_xlabel('ngs1')
plt.subplot(224).scatter(xs,logg_irfm,c='cyan',alpha=0.65)
plt.subplot(224).set_xlabel('irfm')
for i in range(4):
	plt.subplot(221+i).set_ylabel('logg')
	plt.subplot(221+i).set_ylim(1,5)

plt.figure(3,figsize=size)
plt.subplot(221).scatter(xs,feh_annrr,c='b',alpha=0.65)
plt.subplot(221).set_xlabel('annrr')
plt.subplot(222).scatter(xs,feh_annsr,c='r',alpha=0.65)
plt.subplot(222).set_xlabel('annsr')
plt.subplot(223).scatter(xs,feh_ngs1,c='g',alpha=0.65)
plt.subplot(223).set_xlabel('ngs1')
plt.subplot(224).scatter(xs,feh_irfm,c='cyan',alpha=0.65)
plt.subplot(224).set_xlabel('irfm')
for i in range(4):
	plt.subplot(221+i).set_ylabel('feh')
	plt.subplot(221+i).set_ylim(-5,1)

plt.show()