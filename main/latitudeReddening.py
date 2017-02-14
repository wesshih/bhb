import bhb
import matplotlib.pyplot as plt
import numpy as np

class Stat:
	def __init__(self, data):
		self.mean = np.mean(data)
		self.std = np.std(data)
		self.median = np.median(data)
		self.lst = [self.mean,self.std,self.median]
		

def findStats(bhb):
	obs = []
	red = []
	gen = []
	for b in bhb:
		obs.append(b.obs_gr)
		red.append(b.red_gr)
		gen.append(b.gen_gr)
	obsStat = Stat(np.array(obs))
	redStat = Stat(np.array(red))
	genStat = Stat(np.array(gen))
	return (obsStat,redStat,genStat)

def makeColors(data, stat):
	# the data is an array with the 6 latitude statistics
	# stat specifies which stat we want to use
	arr = np.array([])
	for d in data:
		arr = np.append(arr,d.lst[stat])
	grayscale = map(lambda x,y: (x+y[0])/(y[1]+y[0]), arr, [(abs(np.amin(arr)),np.amax(arr))]*len(arr))
	colors = [(g,0.33,1-g) for g in grayscale]
	return colors



bhbs = bhb.load('BHB_DATA_P.txt')

bhbs = [b for b in bhbs if abs(b.obs_gr) < 2]


b1 = [b for b in bhbs if b.glat >= 0 and b.glat < 15]
b2 = [b for b in bhbs if b.glat >= 15 and b.glat < 30]
b3 = [b for b in bhbs if b.glat >= 30 and b.glat < 45]
b4 = [b for b in bhbs if b.glat >= 45 and b.glat < 60]
b5 = [b for b in bhbs if b.glat >= 60 and b.glat < 75]
b6 = [b for b in bhbs if b.glat >= 75 and b.glat < 90]

o1,r1,g1 = findStats(b1)
o2,r2,g2 = findStats(b2)
o3,r3,g3 = findStats(b3)
o4,r4,g4 = findStats(b4)
o5,r5,g5 = findStats(b5)
o6,r6,g6 = findStats(b6)

obs = [o1,o2,o3,o4,o5,o6]
red = [r1,r2,r3,r4,r5,r6]
gen = [g1,g2,g3,g4,g5,g6]

plt.figure(figsize=(12,12))

'''
plt.subplot(331).bar([0,15,30,45,60,75],[o1.mean,o2.mean,o3.mean,o4.mean,o5.mean,o6.mean],color='b',width=15)
plt.subplot(332).bar([0,15,30,45,60,75],[o1.std,o2.std,o3.std,o4.std,o5.std,o6.std],color='r',width=15)
plt.subplot(333).bar([0,15,30,45,60,75],[o1.median,o2.median,o3.median,o4.median,o5.median,o6.median],color='g',width=15)

plt.subplot(334).bar([0,15,30,45,60,75],[r1.mean,r2.mean,r3.mean,r4.mean,r5.mean,r6.mean],color='b',width=15)
plt.subplot(335).bar([0,15,30,45,60,75],[r1.std,r2.std,r3.std,r4.std,r5.std,r6.std],color='r',width=15)
plt.subplot(336).bar([0,15,30,45,60,75],[r1.median,r2.median,r3.median,r4.median,r5.median,r6.median],color='g',width=15)

plt.subplot(337).bar([0,15,30,45,60,75],[g1.mean,g2.mean,g3.mean,g4.mean,g5.mean,g6.mean],color='b',width=15)
plt.subplot(338).bar([0,15,30,45,60,75],[g1.std,g2.std,g3.std,g4.std,g5.std,g6.std],color='r',width=15)
plt.subplot(339).bar([0,15,30,45,60,75],[g1.median,g2.median,g3.median,g4.median,g5.median,g6.median],color='g',width=15)
'''
# means = np.array([])
# for o in obs:
# 	means = np.append(means, o.mean)

# grayscale = map(lambda x,y: (x+y[0])/(y[1]+y[0]), means, [(abs(np.amin(means)),np.amax(means))]*len(means))
# colors = [(g,0.33,1-g) for g in grayscale]

color_avgObs = makeColors(obs,0)
# color_stdObs = makeColors(obs,1)
# color_medObs = makeColors(obs,2)
color_avgRed = makeColors(red,0)
color_avgGen = makeColors(gen,0)


theta = np.linspace(0,np.pi/2,6,endpoint=True)
r = [0.75]*len(theta)


ax1= plt.subplot(221,projection='polar')
ax2= plt.subplot(222,projection='polar')
ax3= plt.subplot(223,projection='polar')

for i in range(len(theta)):
	ax1.plot([theta[i],theta[i]],[0,0.75],color='black')
	if i < len(theta)-1:
		ax1.plot([theta[i],theta[i+1]],[0.75,0.75],color='black')
		ax1.fill_between(theta[i:i+2],[0.75,0.75],color=color_avgObs[i])

for i in range(len(theta)):
	ax2.plot([theta[i],theta[i]],[0,0.75],color='black')
	if i < len(theta)-1:
		ax2.plot([theta[i],theta[i+1]],[0.75,0.75],color='black')
		ax2.fill_between(theta[i:i+2],[0.75,0.75],color=color_avgRed[i%6])

for i in range(len(theta)):
	ax3.plot([theta[i],theta[i]],[0,0.75],color='black')
	if i < len(theta)-1:
		ax3.plot([theta[i],theta[i+1]],[0.75,0.75],color='black')
		ax3.fill_between(theta[i:i+2],[0.75,0.75],color=color_avgGen[i%6])

# for i in range(3*len(theta)/4,len(theta)):
# 	ax.plot([theta[i],theta[i]],[0,0.75],color='black')
# 	if i < len(theta)-1:
# 		ax.plot([theta[i],theta[i+1]],[0.75,0.75],color='black')
# 		ax.fill_between(theta[i:i+2],[0.75,0.75],color=color_avgObs[i%6])
# 	else:
# 		print 'here yo: ' + `i`
# 		print theta[i]



		# ax.plot([theta[i],theta[i+1]],[0.5,0.5],color='black')
		# ax.fill_between(theta[i:i+2],[0.5,0.5],color=color_medObs[i])
		# ax.plot([theta[i],theta[i+1]],[1,1],color='black')
		# ax.fill_between(theta[i:i+2],[1,1],color=color_stdObs[i])

ax1.set_rmax(1)
ax2.set_rmax(1)
ax3.set_rmax(1)
ax1.set_axis_bgcolor('gray')
ax2.set_axis_bgcolor('gray')
ax3.set_axis_bgcolor('gray')
ax1.set_xlabel('avgObs')
ax2.set_xlabel('avgRed')
ax3.set_xlabel('avgGen')
plt.show()