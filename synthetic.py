
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

plt.figure()
fig, ax = plt.subplots(2,1,figsize=(10,5))
x_vals = np.arange(-10,80,.1)
y = scipy.stats.norm.pdf(x_vals,65,4)
ax[0].plot(x_vals,y)
y = scipy.stats.uniform.pdf(x_vals,0,60)
ax[1].plot(x_vals,y)

ax[0].get_yaxis().set_visible(False)
ax[1].get_yaxis().set_visible(False)

plt.savefig("distributions.png")

