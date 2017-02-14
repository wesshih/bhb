from Tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as pyplot
import bhb
import numpy as np
import sys
import pickle


class Plotter:
  def __init__(self, xData, yData):
    (self.xName, self.xMin, sel.xMax) = xData
    (self.yNames, self.yMin, sel.yMax) = yData

    self.bhbs = np.array(bhb.load('BHB_DATA.txt'))
    self.xVals = [b.__dict__[self.xName] for b in self.bhbs]
    self.yVals = []
    for i in range(len(yNames)):
      self.yVals.append([b.__dict__[self.yNames[i]] for b in self.bhbs])
    self.colors = ['b','r','g','c','y']
    self.markers = ['o','+','^','s','t']

  def createPlot(self, show=True, save=False):
    plt.figure()
    for i in range(len(self.yVals)):
      plt.scatter(self.xVals, self.yVals[i], marker=self.markers[i],
                  color=self.colors[i], edgecolor='black', alpha='0.5',
                  label=self.yNames[i])
      plt.xlabel(self.xName)
      plt.ylabel(self.yNames)
      if self.xMin is not None and self.xMax is not None:
        plt.xlim(self.xMin, self.xMax)
      if self.yMin is not None and self.yMax is not None:
        plt.ylim(self.yMin, self.yMax)
      plt.legend()

      if save:
        print 'Saving this plot.... or I will be eventually'

      if show:
        print 'Showing this plot'
        plt.show()



class PlotterGui:
  def __init__(self, root):
    self.root = root
    (self.xName, self.xMin, self.xMax) = (None, None, None)
    (self.yNames, self.yMin, self.yMax) = ([], None, None)

  def makeForm(self):
    




