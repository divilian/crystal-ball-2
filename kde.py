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

plt.figure()
plt.gca().set_xlabel("height in inches")
plt.gca().set_ylabel("number of students")
pd.Series(heights).hist(bins=np.arange(4*12+0,6*12+8), color="darkgreen")
plt.savefig("kdehist.png")
