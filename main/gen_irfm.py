import bhb
import numpy as np
import matplotlib.pyplot as plt

# attempt to generate the IRFM temp estimates using both obs_dered g-r and ha24 g-r.
# won't be perfect because I won't be using the minimization function. at least not yet
# start by coding the equation



def calcTeff(x, feh, logg):
	# from http://www.sdss.org/dr12/spectro/sspp_irfm/
	# Teff, IRFM = 5040/(a0 + a1*X + a2*X^2 + a3*X^3 + a4*X*[Fe/H] + a5*[Fe/H] + a6*[Fe/H]^2),
	# where, X is g-i and a0=0.6787, a1=0.3116, a2=0.0573, a3=-0.0406, a4=-0.0163, a5=-0.0021, and a6=-0.0003 for log g >= 3.7
	# while a0=0.6919, a1=0.3091, a2=0.0688, a3=-0.0428, a4=-0.0078, a5=-0.0086, and a6=-0.0042 for log g < 3.7.
	
	a_low  = [0.6919, 0.3091, 0.0688, -0.0428, -0.0078, -0.0086, -0.0042] # log g < 3.7
	a_high = [0.6787, 0.3116, 0.0573, -0.0406, -0.0163, -0.0021, -0.0003] # log g >= 3.7

	if logg < 3.7:
		a = a_low
	else:
		a = a_high

	return 5040/(a[0] + a[1]*x + a[2]*(x**2) + a[3]*(x**3) + a[4]*x*feh + a[5]*feh + a[6]*(feh**2))



bhbs = bhb.load('BHB_DATA_022317.txt')

# filter out bhbs that have bad values
print len(bhbs)
bhbs = np.array([b for b in bhbs if b.logg_ngs1 != -9999 and b.feh_ngs1 != -9999 and b.teff_irfm != -9999 and b.logg_irfm != -9999 and b.feh_irfm != -9999])
print len(bhbs)

useDered = False

t1 = []
t2 = []
t3 = []


for b in bhbs:
	g_i = b.g - b.i if not useDered else b.dered_g - b.dered_i
	g_r = b.g - b.r if not useDered else b.dered_g - b.dered_r
	if True: #g_r > -0.3:
		t1.append(calcTeff(g_i, b.feh_ngs1, b.logg_ngs1))
		t2.append(calcTeff(g_i, b.feh_irfm, b.logg_irfm))
		t3.append(b.teff_irfm)

xs = range(len(t1))
print len(t1)

print 'teff_1 min: ' + `min(t1)`
print 'teff_2 min: ' + `min(t2)`
print 'teff_3 min: ' + `min(t3)`
print '-----------------'

print 'teff_1 max: ' + `max(t1)`
print 'teff_2 max: ' + `max(t2)`
print 'teff_3 max: ' + `max(t3)`
print '-----------------'

print 'teff_1 mean: ' + `np.mean(t1)`
print 'teff_2 mean: ' + `np.mean(t2)`
print 'teff_3 mean: ' + `np.mean(t3)`
print '-----------------'

low1 = np.where(np.array(t1) < 5000)[0]
low2 = np.where(np.array(t2) < 5000)[0]

print len(low1)
print len(low2)

print [t for t in np.array(t1)[low1]]

print [b.logg_ngs1 for b in bhbs[low1]]
print [b.feh_ngs1 for b in bhbs[low1]]
print [b.logg_irfm for b in bhbs[low1]]
print [b.feh_irfm for b in bhbs[low1]]


y_labels = ['teff_1','teff_2','teff_irfm']

plt.figure(figsize=(10,10))
plt.subplot(311).scatter(xs, t1, c='b', alpha=0.5)
plt.subplot(312).scatter(xs, t2, c='r', alpha=0.5)
plt.subplot(313).scatter(xs, t3, c='g', alpha=0.5)
for i in range(3):
	plt.subplot(311+i).set_ylim(6500,10500)
	plt.subplot(311+i).set_ylabel(y_labels[i])
plt.show()



