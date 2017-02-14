from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math

#np.random.seed(12345678)

const = 20
x = const * np.random.random(20)
y = const * np.random.random(20)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

print 'slope: ' + `slope`
print 'inter: ' + `intercept`
print 'r_val: ' + `r_value`
print 'p_val: ' + `p_value`
print 'st_er: ' + `std_err`

print 'r_squ: ' + `r_value**2`

max_x = int(math.ceil(max(x)))
lin_xs = np.linspace(min(x),max(x),2)
print max_x
line = map(lambda x: x * slope + intercept, lin_xs)

plt.scatter(x,y)
plt.plot(lin_xs,line)
plt.show()
