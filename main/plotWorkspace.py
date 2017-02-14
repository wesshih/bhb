import util
import bhb
import matplotlib.pyplot as plt
import numpy as np
import pysynphot as S

bhbs = np.array(bhb.load('BHB_DATA_P.txt'))
plt.figure(figsize=(20,10))

'''
# gray mapping lat vs long
fil_bhbs = [b for b in bhbs if b.dif_gr < 1]

print 'bhbs: ' + `len(bhbs)`
print 'fil:  ' + `len(fil_bhbs)`

xs = [b.glon for b in fil_bhbs]
ys = [b.glat for b in fil_bhbs]

difs = np.array([b.dif_gr for b in fil_bhbs])


dif_min = np.amin(difs)
dif_max = np.amax(difs)

print dif_min
print dif_max

colors = []
for d in difs:
	colors.append(((d + abs(dif_min))*1.0)/(abs(dif_min)+dif_max))

print colors[101:120]


plt.scatter(xs,ys,c=difs)
plt.gray()
plt.show()
'''


# spectra plotting
index = 0

for i in range(len(bhbs)):
	if bhbs[i].dif_gr < 0:
		if abs(bhbs[i].obs_gr) > 0.1 and i != 5:
			print 'i: ' + `i`

			index = i
			break


b0 = bhbs[index]
print b0.data
print b0.data[27]
print b0.data[28]
print 'teff: ' + `b0.teff`
print 'feh: ' + `b0.feh`
print 'logg: ' + `b0.logg`

print b0.obs_gr
print b0.gen_gr


s1 = S.Icat('phoenix',b0.teff,b0.feh,b0.logg)
s2 = S.Icat('ck04models',b0.teff,b0.feh,b0.logg)
s3 = S.Icat('k93models',b0.teff,b0.feh,b0.logg)
# s3 = S.Icat('k93models',7800,0,4.3)


plt.subplot(211).plot(s1.wave,s1.flux,c='b')
plt.subplot(211).set_xlim(3500,9000)
# plt.subplot(211).set_ylim(ymin=10000000)

plt.subplot(212).plot(s2.wave,s2.flux,c='r')
plt.subplot(212).plot(s3.wave,s3.flux,c='g')
plt.subplot(212).set_xlim(3500,9000)
# plt.subplot(212).set_ylim(ymin=10000000)
# plt.xlim(1000,6000)
# plt.ylim(ymin=1)
plt.show()

'''

theta = np.linspace(0,np.pi/12,50,endpoint=True)


ax = plt.subplot(111,projection='polar')
ax.plot(theta,[0.75]*len(theta),c='b')
ax.plot(theta,[0.9]*len(theta),c='b')
ax.fill_between(theta,0,0.5,color='#348ABD')

ax.set_rmax(1)
plt.show()
'''

print 'done'
