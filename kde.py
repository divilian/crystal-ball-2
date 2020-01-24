import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

heights = np.array([
    5*12 + 1,
    5*12 + 2,
    5*12 + 4,
    5*12 + 4,
    5*12 + 4,
    5*12 + 5,
    5*12 + 5,
    5*12 + 5,
    5*12 + 5,
    5*12 + 5,
    5*12 + 7,
    5*12 + 7,
    5*12 + 7,
    5*12 + 8,
    5*12 + 8,
    5*12 + 9,
    5*12 + 10,
    5*12 + 11,
    6*12 + 0,
    6*12 + 0,
    6*12 + 1,
    6*12 + 1,
    6*12 + 6,
])

#plt.figure()
#plt.gca().set_xlabel("height in inches")
#plt.gca().set_ylabel("number of students")
#pd.Series(heights).hist(bins=np.arange(4*12+0,6*12+8), color="darkgreen")
#plt.savefig("kdehist.png")

# lil Gaussian curve
#plt.figure()
#x_lil = np.arange(0,20,.1)
#y = scipy.stats.norm.pdf(x_lil,10,3)
#plt.abline(
#plt.axis("off")
#plt.plot(x_lil,y)
#plt.savefig("lilGaussian.png")


fig, ax = plt.subplots(2,2,figsize=(10,8))
#fig.figure(figsize=(10,15))
x_vals = np.arange(4*12,7*12,.1)
bws = [1, .5, .3, .1]
coords = [ (x,y) for x in [0,1] for y in [0,1] ]
kdes = [ scipy.stats.gaussian_kde(heights,bw_method=bw) for bw in bws ]
for kde,coord,bw in zip(kdes,coords,bws):
    ax[coord].plot(x_vals,kde(x_vals))
    ax[coord].title.set_text("Bandwidth: {}".format(bw))
plt.savefig("kdes.png")
