import util
import bhb
import matplotlib.pyplot as plt
import numpy as np
import sys
import pickle

# this is a small program that quickly creates plots
# it can do simple plots such as dif_gr vs d.
# it is unable to do more complex plots like the 'dust free' plots, which require better filtering
# this simply plots all the data, and possibly restricts the range


print 'Matplotlib loaded, starting graphing process'

# one x variable of course
x_var = None
x_min = None
x_max = None

# support more than 1 y variable
num_y = 0
y_var = []
y_min = None
y_max = None

x_var = raw_input('x variable: ')
if int(raw_input('define x range? ')) == 1:
	x_min = float(raw_input('x min: '))
	x_max = float(raw_input('x max: '))

num_y = int(raw_input('number of y variables: '))

while num_y > 5:
	print 'only 5 y variables supported try again'
	num_y = int(raw_input('number of y variables: '))

for i in range(num_y):
	y_var.append(raw_input('y'+`i`+' var: '))

#y_var = raw_input('y variable: ')
if int(raw_input('define y range? ')) == 1:
	y_min = float(raw_input('y min: '))
	y_max = float(raw_input('y max: '))

'''
# check cmd line arguments
if len(sys.argv) < 5:
	print 'Error: incorrect arguments. Please give at least x and y vars, and x and y indicators'
	quit()
else:
	(x_var,y_var) = sys.argv[1:3]
	if int(sys.argv[3]) != 0:
		# x range specified
		x_min = int(sys.argv[5])
		x_max = int(sys.argv[6])
		if int(sys.argv[4]) != 0:
			# both x and y ranges specified
			y_min = int(sys.argv[7])
			y_max = int(sys.argv[8])
	elif int(sys.argv[4]) != 0:
		# x range is 0, but y range is not. so y range arg 5,6
		y_min = int(sys.argv[5])
		y_max = int(sys.argv[6])
'''

#now we should have the varialbes, and potentially the ranges.

# load the BHBs
bhbs = np.array(bhb.load('BHB_DATA.txt'))


xs = [b.__dict__[x_var] for b in bhbs]
ys = []
for i in range(num_y):
	ys.append([b.__dict__[y_var[i]] for b in bhbs])
#ys = [b.__dict__[y_var] for b in bhbs]


#ys2 = [y - 100 for y in ys]
'''
sub1 = plt.subplot(211)
sub1.scatter(xs,ys)
sub1.set_xlabel(x_var)
sub1.set_ylabel(y_var)

sub2 = plt.subplot(212)
sub2.scatter(xs,ys,color='blue')
sub2.set_xlabel(x_var)
sub2.set_ylabel(y_var)
sub2.scatter(xs,ys2,color='red')
#sub2.set_xlim(0,10)
#sub2.set_ylim(0,10)

'''
colors = ['blue','red','green','cyan','yellow']

ax = plt.subplot(111)

for i in range(num_y):
	plt.scatter(xs,ys[i],marker='o',color=colors[i],edgecolor='black',alpha='0.5',label=y_var[i])

#plt.scatter(xs,ys,marker='o',edgecolor='black',alpha=0.5)
#plt.scatter(xs,ys2,marker='o',color=red,edgecolor='black',alpha=0.5)
plt.xlabel(x_var)
plt.ylabel(y_var)
if x_min is not None and x_max is not None:
	plt.xlim(x_min, x_max)
if y_min is not None and y_max is not None:
	plt.ylim(y_min, y_max)

plt.legend()

namex = x_var + ('['+`x_min`+','+`x_max`+']' if x_min is not None and x_max is not None else '') 
namey = `y_var` + ('['+`y_min`+','+`y_max`+']' if y_min is not None and y_max is not None else '')
name = 'plots/' + namex + '_VS_' + namey
print name

plt.savefig(name + '.png')

pickle.dump(ax, file(name + '.pickle','w'))

plt.show()