
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
import io

it = pd.read_csv(io.StringIO('''
gender,hair
male,blonde
male,blonde
male,blonde
male,blonde
male,blonde
male,blonde
male,blonde
male,blonde
male,blonde
male,blonde
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,brunette
male,red
male,red
male,bald
male,bald
male,bald
male,bald
male,bald
male,bald
male,bald
male,bald
male,bald
male,bald
male,bald
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,blonde
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,brunette
female,red
female,red
female,red
female,red
female,red
other,brunette
other,brunette
other,bald
'''))

c = pd.crosstab(it.gender, it.hair)
c = np.round(c / np.sum(c.sum()),3)
print(c)

c = pd.crosstab(it.gender, it.hair, margins=True)
c = np.round(c / c.loc['All']['All'], 3)
print(c)

#it.index = ['blonde','brunette','red','bald']
#it = np.round(it / np.sum(it.sum()),3)

