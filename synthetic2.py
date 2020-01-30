
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

np.random.seed(13)

heights = np.random.normal(65, 8, 100)
sat_scores = np.random.normal(1000, 350, 100)

#plt.figure()
#plt.scatter(heights, sat_scores)
#plt.xlabel("height (in)")
#plt.ylabel("SAT score")
#plt.ylim(sat_scores.min()-20, sat_scores.max()+20)
#plt.axhline(y=400, color='r', linestyle='--')
#plt.axhline(y=1600, color='r', linestyle='--')
#plt.savefig("uncorrscatter.png")
#plt.figure()
#plt.scatter(heights, sat_scores.clip(400,1600))
#plt.xlabel("height (in)")
#plt.ylabel("SAT score")
#plt.ylim(sat_scores.min()-20, sat_scores.max()+20)
#plt.axhline(y=400, color='r', linestyle='--')
#plt.axhline(y=1600, color='r', linestyle='--')
#plt.savefig("uncorrscatterclip.png")

print(scipy.stats.pearsonr(heights,sat_scores))

print("min: {:.2f}, max: {:.2f}".format(sat_scores.min(), sat_scores.max()))


weights_lbs = np.random.normal(150, 30, 100)
weights_kg = weights_lbs / 2.2
#plt.figure()
#plt.scatter(weights_kg, weights_lbs)
#plt.xlabel("weight (kg)")
#plt.ylabel("weight (lbs)")
#plt.savefig("compcorrscatter.png")

print(scipy.stats.pearsonr(weights_lbs,weights_kg))


#plt.figure()
num_hrs = np.random.normal(50,20,200).clip(0,500)
score = num_hrs * .333 + 26.667 + np.random.normal(0,10,200)
#plt.xlabel("# hours practice")
#plt.ylabel("score (millions)")
#plt.title(r"$\sigma = $10 million")
#plt.scatter(num_hrs,score, color="teal")
#plt.savefig("ddr1.png")
#plt.figure()
score = num_hrs * .333 + 26.667 + np.random.normal(0,3,200)
#plt.xlabel("# hours practice")
#plt.ylabel("score (millions)")
#plt.title(r"$\sigma = $3 million")
#plt.scatter(num_hrs,score, color="teal")
#plt.savefig("ddr2.png")



party = np.random.choice(['Democrat','Republican'], p=[.54,.46], size=2000)
superbowl = np.random.choice(['Chiefs','49ers'], p=[.58,.42], size=2000)
print(pd.crosstab(superbowl, party, margins=True))
print(scipy.stats.chi2_contingency(pd.crosstab(superbowl, party)))
plt.figure()
sns.heatmap(pd.crosstab(superbowl, party))
plt.savefig("party_sup_heat_no_bounds.png")
plt.figure()
sns.heatmap(pd.crosstab(superbowl,party), vmin=0, vmax=2000)
plt.savefig("party_sup_heat.png")

party_color = np.where(party=='Democrat','blue','red')
print(party)
print(party_color)
print(pd.crosstab(party, party_color, margins=True))
print(scipy.stats.chi2_contingency(pd.crosstab(party, party_color)))
plt.figure()
sns.heatmap(pd.crosstab(party,party_color), vmin=0, vmax=2000)
plt.savefig("party_color_heat.png")

gun_owner = np.where(party=='Democrat',
    np.random.choice(['gun','no gun'],p=[.2,.8],size=2000),
    np.random.choice(['gun','no gun'],p=[.44,.56],size=2000))
print(pd.crosstab(party, gun_owner, margins=True))
print(scipy.stats.chi2_contingency(pd.crosstab(party, gun_owner)))
plt.figure()
sns.heatmap(pd.crosstab(party,gun_owner), vmin=0, vmax=2000)
plt.savefig("party_gun_heat.png")
