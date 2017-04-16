# this file will test some of the balmer values
# it will test both the g-r color prediction against the observed -> not reported in sppParams just sanity
# it will also test the temp estimates using balmer against the HA24 and HD24 estimates in sppParams
# finally it will try and do some of the ANNSR or ANNRR estimation to see if obs vs estimated

import bhb
import matplotlib.pyplot as plt

bhbs = bhb.load('BHB_DATA_022317_1.txt')
bhbs = [b for b in bhbs if b.ha24_cont > -9999 and b.hd24_cont > -9999 and b.teff_ha24 > 0 and b.teff_hd24 > 0]

ha_gr = []
hd_gr = []
ha_teff = []
hd_teff = []
ha_gr_side = []
hd_gr_side = []
ha_teff_side = []
hd_teff_side = []

for b in bhbs:
	ha_gr.append(0.818 - 0.092*b.ha24_cont)
	hd_gr.append(0.469 - 0.058*b.hd24_cont)
	ha_teff.append(4133+371*b.ha24_cont)
	hd_teff.append(5449+206*b.hd24_cont)

	ha_gr_side.append(0.818 - 0.092*b.ha24_side)
	hd_gr_side.append(0.469 - 0.058*b.hd24_side)
	ha_teff_side.append(4133+371*b.ha24_side)
	hd_teff_side.append(5449+206*b.hd24_side)

xs_gr = [b.obs_gr for b in bhbs]
xs_teff_ha = [b.teff_ha24 for b in bhbs]
xs_teff_hd = [b.teff_hd24 for b in bhbs]

plt.figure(figsize=(10,10))


plt.subplot(311).scatter(xs_gr,ha_gr,c='b',alpha=0.75)
plt.subplot(311).scatter(xs_gr,hd_gr,c='r',alpha=0.75)
plt.subplot(311).scatter(xs_gr,xs_gr,c='g',alpha=0.5)
plt.subplot(312).scatter(xs_teff_ha,ha_teff,c='b',alpha=0.5)
plt.subplot(312).scatter(xs_teff_ha,ha_teff_side,c='r',alpha=0.5)
plt.subplot(312).scatter(xs_teff_ha,xs_teff_ha,c='g',alpha=0.4)
plt.subplot(313).scatter(xs_teff_hd,hd_teff,c='b',alpha=0.5)
plt.subplot(313).scatter(xs_teff_hd,hd_teff_side,c='r',alpha=0.5)
plt.subplot(313).scatter(xs_teff_hd,xs_teff_hd,c='g',alpha=0.4)
plt.show()