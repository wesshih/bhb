from Tkinter import *
from old_plotter import Plotter


class PlotWindow:
  def __init__(self,root):
    self.root = root
    self.x_var = None
    self.x_min = None
    self.x_max = None
    self.y_var = []
    self.y_min = None
    self.y_max = None

    # Make checkbuttons
    self.y_en = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
    self.y_en[0].set(True) # default with 1 selected
    for i in range(len(self.y_en)):
      c = Checkbutton(self.root, text='',variable=self.y_en[i]).grid(row=i+1,column=0)

    self.rangex = IntVar()
    Checkbutton(self.root, text='x range',variable=self.rangex).grid(row=0,column=3)
    self.rangey = IntVar()
    Checkbutton(self.root, text='y range',variable=self.rangey).grid(row=1,column=3)

    # Make Labels
    label_text = ['x var','y var','y1 var','y2 var','y3 var','y4 var']
    for i in range(len(label_text)):
      Label(self.root,text=label_text[i]).grid(row=i,column=1)

    Label(self.root, text='min').grid(row=0,column=4)
    Label(self.root, text='max').grid(row=0,column=6)
    Label(self.root, text='min').grid(row=1,column=4)
    Label(self.root, text='max').grid(row=1,column=6)

    # Make Entry Boxes
    self.vars = []
    for i in range(len(label_text)):
      self.vars.append(Entry(self.root))
      self.vars[i].grid(row=i,column=2)

    self.ex_min = Entry(self.root,width=10)
    self.ex_min.grid(row=0,column=5)
    self.ex_max = Entry(self.root,width=20)
    self.ex_max.grid(row=0,column=7)
    self.ey_min = Entry(self.root)
    self.ey_min.grid(row=1,column=5)
    self.ey_max = Entry(self.root)
    self.ey_max.grid(row=1,column=7)
    
    # checkbox for save option
    self.savePlot = BooleanVar()
    Checkbutton(self.root, text='Save Plot', variable=self.savePlot).grid(row=6, column=5)

    # checkbox for trend option
    self.showTrend = BooleanVar()
    Checkbutton(self.root, text='Show Trend Line', variable=self.showTrend).grid(row=6, column=8)

    # Buttons
    self.b_show = Button(self.root, text='Make Plot',command=lambda: self.getValues(self.savePlot.get(),self.showTrend.get())).grid(row=6,column=6)
    #self.b_save = Button(self.root, text='Save Plot',command=lambda:self.getValues(save=True)).grid(row=4,column=5)
    self.b_exit = Button(self.root, text='Exit',command=self.root.destroy).grid(row=7,column=7)

    # constraint stuff con = constraint
    self.con1 = IntVar()
    Checkbutton(self.root, variable=self.con1).grid(row=3, column=4)
    self.con1_var = Entry(self.root)
    self.con1_var.grid(row=3,column=5)
    self.con1_min = Entry(self.root)
    self.con1_min.grid(row=3,column=6)
    self.con1_max = Entry(self.root)
    self.con1_max.grid(row=3,column=7)

    self.con2 = IntVar()
    Checkbutton(self.root, variable=self.con2).grid(row=4, column=4)
    self.con2_var = Entry(self.root)
    self.con2_var.grid(row=4,column=5)
    self.con2_min = Entry(self.root)
    self.con2_min.grid(row=4,column=6)
    self.con2_max = Entry(self.root)
    self.con2_max.grid(row=4,column=7)

    self.con3 = IntVar()
    Checkbutton(self.root, variable=self.con3).grid(row=5, column=4)
    self.con3_var = Entry(self.root)
    self.con3_var.grid(row=5,column=5)
    self.con3_min = Entry(self.root)
    self.con3_min.grid(row=5,column=6)
    self.con3_max = Entry(self.root)
    self.con3_max.grid(row=5,column=7)

  def getValues(self,save=False,trend=False):
    print 'save: ' + `save`
    print 'TEST CLICK'
    self.x_var = self.vars[0].get()
    self.y_var = [] # reset the y var list
    for i in range(len(self.y_en)):
      if self.y_en[i].get() == 1:
        print 'got a 1, adding to vars'
        self.y_var.append(self.vars[i+1].get())

    if self.rangex.get() == 1:
      self.x_min = float(self.ex_min.get())
      self.x_max = float(self.ex_max.get())
    else:
      self.x_min = None
      self.x_max = None

    if self.rangey.get() == 1:
      self.y_min = float(self.ey_min.get())
      self.y_max = float(self.ey_max.get())
    else:
      self.y_min = None
      self.y_max = None

    cc = []
    if self.con1.get() == 1:
      cc.append((self.con1_var.get(),float(self.con1_min.get()),float(self.con1_max.get())))
    if self.con2.get() == 1:
      cc.append((self.con2_var.get(),float(self.con2_min.get()),float(self.con2_max.get())))
    if self.con3.get() == 1:
      cc.append((self.con3_var.get(),float(self.con3_min.get()),float(self.con3_max.get())))


    test_plotter = Plotter(self.x_var,self.y_var,self.x_min,self.x_max,self.y_min,self.y_max,cc)
    test_plotter.plot(save,trend)

    '''
    if save:
      test_plotter.savePlot()
    else:
      print 'You pushed save plot, but surprise! it always saves...'
      test_plotter.plot()
    '''



if __name__ == '__main__':
  root = Tk()
  pw = PlotWindow(root)
  root.mainloop()




