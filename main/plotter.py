import util
import bhb
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import sys
import pickle
from scipy import stats

class Plotter:
  def __init__(self,x_var,y_var,x_min,x_max,y_min,y_max,cc=None):
    self.x_var = x_var
    self.x_min = x_min
    self.x_max = x_max

    self.y_var = y_var
    self.y_min = y_min
    self.y_max = y_max

    temp_bhbs = bhb.load('BHB_DATA_022317.txt')
    if cc is not None:
        for c in cc:
            var = c[0]
            var_min = c[1]
            var_max = c[2]
            temp_bhbs = [b for b in temp_bhbs if b.__dict__[var] > var_min and b.__dict__[var] < var_max]
    self.bhbs = np.array(temp_bhbs)

    if x_var == 'number':
        self.xs = range(len(self.bhbs))
    else:
        self.xs = [b.__dict__[self.x_var] for b in self.bhbs]
    self.ys = []
    for i in range(len(y_var)):
        self.ys.append([b.__dict__[self.y_var[i]] for b in self.bhbs])

    self.colors = ['b','r','g','c','y']

    # hacky stuff to make name for saving plot
    # please ignore extra long lines
    nameX = self.x_var + ('['+`self.x_min`+','+`self.x_max`+']' if self.x_min is not None and self.x_max is not None else '')
    nameY = `self.y_var` + ('['+`self.y_min`+','+`self.y_max`+']' if self.y_min is not None and self.y_max is not None else '')
    self.name = 'plots/' + nameX + '_VS_' + nameY

  def plot(self,save=False,trend=False):
    plt.figure()
    plotObject = plt.subplot(111)
    for i in range(len(self.y_var)):
        m,b,r,p,err = stats.linregress(self.xs,self.ys[i])
        print 'm: ' + `m`
        print 'b: ' + `b`
        print 'r: ' + `r`
        print 'p: ' + `p`
        print 'err: ' + `err`
        plt.scatter(self.xs,self.ys[i],marker='o',color=self.colors[i],edgecolor='black',alpha='0.5',label=self.y_var[i])
        if trend:
            plt.plot([min(self.xs),max(self.xs)],[min(self.xs)*m + b, max(self.xs)*m + b],color=self.colors[i],label='slope: '+`m`)
    plt.xlabel(self.x_var)
    plt.ylabel(self.y_var)
    if self.x_min is not None and self.x_max is not None:
    	plt.xlim(self.x_min, self.x_max)
    if self.y_min is not None and self.y_max is not None:
    	plt.ylim(self.y_min, self.y_max)
    plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

    # save plot always for now
    if save:
        plt.savefig(self.name + '.png')
        pickle.dump(plotObject, file(self.name + '.pickle','w'))

    plt.show()
