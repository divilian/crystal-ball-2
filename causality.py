
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

np.set_printoptions(precision=3)

N = 50000

# Case 1:
region = np.random.choice(['Asian','non-Asian'],p=[.4,.6],size=N)
chopsticks = np.random.choice(['yes','no'],p=[.3,.7],size=N)
VG = np.random.choice(['good','bad'],p=[.2,.8],size=N)

## Case 2 (Michael):
#region = np.random.choice(['Asian','non-Asian'],p=[.4,.6],size=N)
#chopsticks = np.where(region=='Asian',
#    np.random.choice(['yes','no'],p=[.8,.2],size=N),
#    np.random.choice(['yes','no'],p=[.1,.9],size=N))
#VG = np.where(chopsticks=='yes',
#    np.random.choice(['good','bad'],p=[.6,.4],size=N),
#    np.random.choice(['good','bad'],p=[.1,.9],size=N))
#
## Case 3 (Stephen):
#region = np.random.choice(['Asian','non-Asian'],p=[.4,.6],size=N)
#chopsticks = np.where(region=='Asian',
#    np.random.choice(['yes','no'],p=[.8,.2],size=N),
#    np.random.choice(['yes','no'],p=[.1,.9],size=N))
#VG = np.where(region=='Asian',
#    np.random.choice(['good','bad'],p=[.4,.6],size=N),
#    np.random.choice(['good','bad'],p=[.15,.85],size=N))

data = pd.DataFrame({'region':region,'chopsticks':chopsticks,'VG':VG})
print(data)

print("\nVG and chopsticks absolutely independent?")
pval = scipy.stats.chi2_contingency(pd.crosstab(data.chopsticks, data.VG))[1]
print(f"p-val = {pval:.3f} {'(yes, independent)' if pval > .05 else 'NO'}")

asians = data[data.region == "Asian"]
nonAsians = data[data.region != "Asian"]
choppers = data[data.chopsticks == "yes"]
nonChoppers = data[data.chopsticks != "yes"]

print("\nIs Michael right?")
print("VG and region independent given chopsticks?")
print("    in other words, P(VG|chop) = P(VG|Asian,chop)?")
pval = scipy.stats.chi2_contingency(pd.crosstab(choppers.region,choppers.VG))[1]
print(f"p-val = {pval:.3f} {'(yes, independent)' if pval > .05 else 'NO'}")
pval = scipy.stats.chi2_contingency(pd.crosstab(nonChoppers.region,nonChoppers.VG))[1]
print(f"p-val = {pval:.3f} {'(yes, independent)' if pval > .05 else 'NO'}")

print("P(VG,Asian|chop) ~= P(VG|chop) x P(Asian|chop)?")
p_vg_asian_g_chop = (
    len(data[(data.VG=='good')&(data.region=='Asian')&(data.chopsticks=='yes')])
/ len(data[data.chopsticks=='yes']))
p_vg_g_chop = (len(data[(data.VG=='good')&(data.chopsticks=='yes')]) /
    len(data[data.chopsticks=='yes']))
p_asian_g_chop = (len(data[(data.region=='Asian')&(data.chopsticks=='yes')]) /
    len(data[data.chopsticks=='yes']))
print(f"{p_vg_asian_g_chop:.3f} ~= {p_vg_g_chop:.3f} * {p_asian_g_chop:3f} = "
    f"{p_vg_g_chop * p_asian_g_chop:.3f}?")

print("\nIs Stephen right?")
print("VG and chopsticks independent given region?")
print("    in other words, P(VG|Asian) = P(VG|chop,Asian)?")
pval = scipy.stats.chi2_contingency(pd.crosstab(asians.chopsticks,asians.VG))[1]
print(f"p-val = {pval:.3f} {'(yes, independent)' if pval > .05 else 'NO'}")
pval = scipy.stats.chi2_contingency(pd.crosstab(nonAsians.chopsticks,nonAsians.VG))[1]
print(f"p-val = {pval:.3f} {'(yes, independent)' if pval > .05 else 'NO'}")

print("P(VG,chop|Asian) ~= P(VG|Asian) x P(chop|Asian)?")
p_vg_chop_g_asian = (
    len(data[(data.VG=='good')&(data.region=='Asian')&(data.chopsticks=='yes')])
/ len(data[data.region=='Asian']))
p_vg_g_asian = (len(data[(data.VG=='good')&(data.region=='Asian')]) /
    len(data[data.region=='Asian']))
p_chop_g_asian = (len(data[(data.region=='Asian')&(data.chopsticks=='yes')]) /
    len(data[data.region=='Asian']))
print(f"{p_vg_chop_g_asian:.3f} ~= {p_vg_g_asian:.3f} * {p_chop_g_asian:3f} = "
    f"{p_vg_g_asian * p_chop_g_asian:.3f}?")
