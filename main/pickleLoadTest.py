from Tkinter import Tk
from tkFileDialog import askopenfilename
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pickle

Tk().withdraw()
filename = askopenfilename()
print filename
ax = pickle.load(file(filename))

#ax = pickle.load(file("plots/d_vs_['teff'].pickle"))

plt.show()