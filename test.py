class Test:
  def __init__(self, data, fromFits):
    if fromFits:
      self.x = 0
      self.y = 0
      self.z = 0
      self.t = None
    else:
      self.__dict__ = data
      if not 't' in data:
        self.t = None

  def addVar(self, val):
    self.val = val


t1 = Test(None,True)
print t1.__dict__
print t1.t
print '-----------------'

d2 = {'x':1,'y':2,'z':3}
t2 = Test(d2,False)
print t2.__dict__
print t2.t
print '-----------------'

d3 = {'x':2,'y':3,'z':4,'t':10}
t3 = Test(d3,False)
print t3.__dict__
print t3.t
print '-----------------'

t3.test = 'wow'
print t3.test


print t1.__dict__
print t2.__dict__
print t3.__dict__

t2.addVar('hello')

print t2.__dict__
print t2.val
