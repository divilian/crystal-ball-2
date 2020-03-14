
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns


the_tables = pd.read_html("http://stephendavies.org/allAboutStephen.html")
areas = the_tables[0]
areas.columns = ['pic','role','description','adjectives','allocation']
areas = areas[['role','adjectives','allocation']]


#%%

roles = np.array([], dtype=object)
adjs = np.array([], dtype=object)

for row in areas.itertuples():
    for adjective in row.adjectives.split():
        roles = np.append(roles, row.role)
        adjs = np.append(adjs, adjective)

adjectives_df = pd.DataFrame({'role':roles, 'adjective':adjs})
print(adjectives_df)

areas = areas[['role','allocation']]
print(areas)

#%%

percentages = np.array([], dtype=int)

for row in areas.itertuples():
    percentages = np.append(percentages,
        int(row.allocation.split("%")[0]))

areas.allocation = percentages

df = pd.merge(areas, adjectives_df)
print(df)

print(df.adjective.value_counts())
perc_of_time = df.groupby('adjective').allocation.sum()
print(perc_of_time.sort_values(ascending=False))
perc_of_time.plot(kind='bar')
plt.savefig('adjectives.png', bbox_inches='tight')
#plt.margins(y=100)

