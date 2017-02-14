import util
import bhb
import matplotlib.pyplot as plt
import numpy as np


print 'Matplotlib loaded, starting graphing process'

# going to filter out the only 'dust free' bhbs
# then plot g-r vs dist

bhbs = np.array(bhb.load('BHB_DATA.txt'))

dust_free = [b for b in bhbs if (b.obs_gr - b.red_gr) < 0.05]
dust_free2 = np.array([b for b in bhbs if (b.obs_gr - b.red_gr) < 0.05])
print len(dust_free)
print len(dust_free2)
print dust_free[:10]
print dust_free2[:10]
close_bhb = [b for b in dust_free if b.d < 10]
print len(close_bhb)
close_bhb2 = [b for b in bhbs if b.d < 10]
print len(close_bhb2)

dist = np.array([b.d for b in bhbs])
print 'mean dist:' + `np.mean(dist)`

plt.figure(figsize=(16,12))

plt.subplot(421).scatter([b.d for b in close_bhb], [(b.gen_gr - b.obs_gr) for b in close_bhb],color='blue')
plt.subplot(422).scatter([b.d for b in close_bhb2], [(b.gen_gr - b.obs_gr) for b in close_bhb2],color='red')

plt.subplot(423).scatter([b.feh for b in close_bhb], [(b.gen_gr - b.obs_gr) for b in close_bhb],color='blue')
plt.subplot(424).scatter([b.feh for b in close_bhb2], [(b.gen_gr - b.obs_gr) for b in close_bhb2],color='red')

plt.subplot(425).scatter([b.logg for b in close_bhb], [(b.gen_gr - b.obs_gr) for b in close_bhb], color='blue')
plt.subplot(426).scatter([b.logg for b in close_bhb2], [(b.gen_gr - b.obs_gr) for b in close_bhb2], color='red')

plt.subplot(427).scatter([b.teff for b in close_bhb], [(b.gen_gr - b.obs_gr) for b in close_bhb], color = 'blue')
plt.subplot(428).scatter([b.teff for b in close_bhb2], [(b.gen_gr - b.obs_gr) for b in close_bhb2], color = 'red')


#p2 = plt.subplot(223)
#p2.scatter([b.d for b in dust_free2], [(b.gen_gr - b.red_gr) for b in dust_free2])
#plt.subplot(224).scatter([b.feh for b in dust_free2], [(b.gen_gr - b.red_gr) for b in dust_free2])

print 'Now saving plot'
plt.savefig('simpleGraph.png')

plt.show()
