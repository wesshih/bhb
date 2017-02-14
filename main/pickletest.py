import matplotlib.pyplot as plt
import pickle

ax = plt.subplot(111)

plt.scatter([1,2,3],[4,5,6],color=['r','b','g'])

pickle.dump(ax, file('pickletest.pickle','w'))
plt.show()