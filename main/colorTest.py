import bhb
import numpy as np
import matplotlib.pyplot as plt

bhb_p = np.array(bhb.load('BHB_DATA_P.txt'))
bhb_ck = np.array(bhb.load('BHB_DATA_CK.txt'))
bhb_k = np.array(bhb.load('BHB_DATA_K.txt'))

plt.figure(figsize=(20,10))

'''
# ---------------------------------------------------
xs11 = [b.obs_ug for b in bhb_p]
ys11 = [b.obs_gr for b in bhb_p]

plt.subplot(321).scatter(xs11,ys11)
plt.subplot(321).set_xlim(0.8,1.5)
plt.subplot(321).set_ylim(-0.5,0.5)

xs12 = [b.gen_ug for b in bhb_p]
ys12 = [b.gen_gr for b in bhb_p]

plt.subplot(322).scatter(xs12,ys12)
plt.subplot(322).set_xlim(0.8,1.5)
plt.subplot(322).set_ylim(-0.5,0.5)

# ---------------------------------------------------
xs21 = [b.obs_ug for b in bhb_ck]
ys21 = [b.obs_gr for b in bhb_ck]

plt.subplot(323).scatter(xs21,ys21)
plt.subplot(323).set_xlim(0.8,1.5)
plt.subplot(323).set_ylim(-0.5,0.5)

xs22 = [b.gen_ug for b in bhb_ck]
ys22 = [b.gen_gr for b in bhb_ck]

plt.subplot(324).scatter(xs22,ys22)
plt.subplot(324).set_xlim(0.8,1.5)
plt.subplot(324).set_ylim(-0.5,0.5)

# ---------------------------------------------------
xs31 = [b.obs_ug for b in bhb_k]
ys31 = [b.obs_gr for b in bhb_k]

plt.subplot(325).scatter(xs31,ys31)
plt.subplot(325).set_xlim(0.8,1.5)
plt.subplot(325).set_ylim(-0.5,0.5)

xs32 = [b.gen_ug for b in bhb_k]
ys32 = [b.gen_gr for b in bhb_k]

plt.subplot(326).scatter(xs32,ys32)
plt.subplot(326).set_xlim(0.8,1.5)
plt.subplot(326).set_ylim(-0.5,0.5)

'''
xs = range(len(bhb_p))
ys11 = [b.gen_ug for b in bhb_p]
ys12 = [b.gen_gr for b in bhb_p]
ys13 = [b.gen_ri for b in bhb_p]
ys14 = [b.gen_iz for b in bhb_p]

ys21 = [b.gen_ug for b in bhb_ck]
ys22 = [b.gen_gr for b in bhb_ck]
ys23 = [b.gen_ri for b in bhb_ck]
ys24 = [b.gen_iz for b in bhb_ck]

ys31 = [b.gen_ug for b in bhb_k]
ys32 = [b.gen_gr for b in bhb_k]
ys33 = [b.gen_ri for b in bhb_k]
ys34 = [b.gen_iz for b in bhb_k]


plt.subplot(221).scatter(xs,ys11,c='b')
plt.subplot(221).scatter(xs,ys21,c='g')
plt.subplot(221).scatter(xs,ys31,c='r')
plt.subplot(221).set_ylabel('u-g')

plt.subplot(222).scatter(xs,ys12,c='b')
plt.subplot(222).scatter(xs,ys22,c='g')
plt.subplot(222).scatter(xs,ys32,c='r')
plt.subplot(222).set_ylabel('g-r')

plt.subplot(223).scatter(xs,ys13,c='b')
plt.subplot(223).scatter(xs,ys23,c='g')
plt.subplot(223).scatter(xs,ys33,c='r')
plt.subplot(223).set_ylabel('r-i')

plt.subplot(224).scatter(xs,ys14,c='b')
plt.subplot(224).scatter(xs,ys24,c='g')
plt.subplot(224).scatter(xs,ys34,c='r')
plt.subplot(224).set_ylabel('i-z')


plt.show()