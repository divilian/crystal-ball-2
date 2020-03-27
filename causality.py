
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

# Case 1:
region = np.random.choice(['Asian','non-Asian'],p=[.4,.6],size=10000)
chopsticks = np.random.choice(['yes','no'],p=[.3,.7],size=10000)
VG = np.random.choice(['good','bad'],p=[.2,.8],size=10000)

# Case 2 (Michael):
region = np.random.choice(['Asian','non-Asian'],p=[.4,.6],size=10000)
chopsticks = np.where(region=='Asian',
    np.random.choice(['yes','no'],p=[.8,.2],size=10000),
    np.random.choice(['yes','no'],p=[.1,.9],size=10000))
VG = np.where(chopsticks=='yes',
    np.random.choice(['good','bad'],p=[.5,.5],size=10000),
    np.random.choice(['good','bad'],p=[.1,.9],size=10000))

# Case 3 (Stephen):
region = np.random.choice(['Asian','non-Asian'],p=[.4,.6],size=10000)
chopsticks = np.where(region=='Asian',
    np.random.choice(['yes','no'],p=[.8,.2],size=10000),
    np.random.choice(['yes','no'],p=[.1,.9],size=10000))
VG = np.where(region=='Asian',
    np.random.choice(['good','bad'],p=[.4,.6],size=10000),
    np.random.choice(['good','bad'],p=[.15,.85],size=10000))

data = pd.DataFrame({'region':region,'chopsticks':chopsticks,'VG':VG})
print(data)

print(scipy.stats.chi2_contingency(pd.crosstab(data.chopsticks, data.VG))[1])

asians = data[data.region == "Asian"]
nonAsians = data[data.region != "Asian"]
choppers = data[data.chopsticks == "yes"]
nonChoppers = data[data.chopsticks != "yes"]

print("VG and region independent given chopsticks?")
print(scipy.stats.chi2_contingency(pd.crosstab(choppers.region, choppers.VG))[1])
print(scipy.stats.chi2_contingency(pd.crosstab(nonChoppers.region, nonChoppers.VG))[1])
print("VG and chopsticks independent given region?")
print(scipy.stats.chi2_contingency(pd.crosstab(asians.chopsticks, asians.VG))[1])
print(scipy.stats.chi2_contingency(pd.crosstab(nonAsians.chopsticks, nonAsians.VG))[1])
