
from statsmodels.nonparametric.smoothers_lowess import lowess
import numpy as np
import matplotlib.pyplot as plt

# Data set #1: Completely random Stephen Craziness.
x = np.random.uniform(0,100,100)
x.sort()
y = np.where(x > 40, 4*x - .2 * x**2 + .001 * x**3 + np.random.normal(0,300,100), x + .1*(x-5)**3 + np.random.normal(0,300,100))

# Data set #2: A quadratic function with high noise. (Comment out the next
# three lines if you'd like to use data set #1, above, instead.)
x = np.random.uniform(0,100,1000)
x.sort()    # So we can do line plots.
y = -5 * x**2 + 400*x - 39 + np.random.normal(0,10000,1000)

m, b = np.polyfit(x, y, 1)
a1, a2, a3 = np.polyfit(x, y, 2)

l = lowess(y,x,frac=1/3)
l2 = lowess(y,x, frac=1/10)
l3 = lowess(y,x,frac=1)
plt.scatter(x,y,marker=".")
plt.plot(x, m*x + b,color="green",linewidth=1,label="least-sq line")
plt.plot(x, a1*x**2 + a2*x + a3,color="purple",linewidth=1,label="least-sq quadratic")
plt.plot(l[:,0],l[:,1],'--',color="red",linewidth=2,label="LOESS α=⅓")
plt.plot(l2[:,0],l2[:,1],color="red",linewidth=2,label="LOESS α=⅒")
plt.plot(l3[:,0],l3[:,1],color="black",linewidth=3,label="LOESS α=1")
plt.legend()
plt.show()
