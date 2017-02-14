import util
import bhb
import matplotlib.pyplot as plt
import numpy as np
import sys

# this is a small program that quickly creates plots
# it can do simple plots such as dif_gr vs d.
# it is unable to do more complex plots like the 'dust free' plots, which require better filtering
# this simply plots all the data, and possibly restricts the range


print 'Matplotlib loaded, starting graphing process'

x_var = None
y_var = None
x_min = None
x_max = None
y_min = None
y_max = None

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


#now we should have the varialbes, and potentially the ranges.

# load the BHBs
bhbs = np.array(bhb.load('BHB_DATA.txt'))


xs = [b.__dict__[x_var] for b in bhbs]
ys = [b.__dict__[y_var] for b in bhbs]

plt.scatter(xs,ys)
plt.xlabel(x_var)
plt.ylabel(y_var)
if x_min is not None and x_max is not None:
	plt.xlim(x_min, x_max)
if y_min is not None and y_max is not None:
	plt.ylim(y_min, y_max)

namex = x_var + ('['+`x_min`+','+`x_max`+']' if x_min is not None and x_max is not None else '') 
namey = y_var + ('['+`y_min`+','+`y_max`+']' if y_min is not None and y_max is not None else '')
name = namex + '_VS_' + namey + '.png'
print name

plt.savefig('plots/' + name)

#plt.show()
