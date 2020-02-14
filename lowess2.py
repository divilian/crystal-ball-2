
import statsmodels.nonparametric.smoothers_lowess
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0,100,100)
x.sort()    # So we can do line plots.
y = np.where(x > 40, 4*x - .2 * x**2 + .001 * x**3 + np.random.normal(0,200,100),
    x + .1*(x-5)**3 + np.random.normal(0,200,100))
#y = 4*x - .2 * x**2 + np.random.normal(0,120,100)

m, b = np.polyfit(x, y, 1)
a1, a2, a3 = np.polyfit(x, y, 2)

lowess = statsmodels.nonparametric.smoothers_lowess.lowess(y,x,frac=1/3)
lowess2 = statsmodels.nonparametric.smoothers_lowess.lowess(y,x,frac=1/10)
lowess3 = statsmodels.nonparametric.smoothers_lowess.lowess(y,x,frac=1)
plt.scatter(x,y)
plt.plot(x, m*x + b,color="green",linewidth=1,label="least-sq line")
plt.plot(x, a1*x**2 + a2*x + a3,color="purple",linewidth=1,
    label="least-sq quadratic")
plt.plot(lowess[:,0],lowess[:,1],'--',color="red",linewidth=2,
    label="LOESS α=⅓")
plt.plot(lowess2[:,0],lowess2[:,1],color="red",linewidth=2,
    label="LOESS α=⅒")
plt.plot(lowess3[:,0],lowess3[:,1],color="black",linewidth=3,
    label="LOESS α=1")
plt.legend()
plt.show()
