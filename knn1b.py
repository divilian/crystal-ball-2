
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
import io

df = pd.read_csv(io.StringIO('''
age,IQ,sport
37,101,football
41,121,baseball
19,87,football
22,117,lacrosse
'''))

print(df.sport)


from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()
sport_onehot = lb.fit_transform(df.sport)
print(sport_onehot)
df['baseball'] = sport_onehot[:,0]
df['football'] = sport_onehot[:,1]
df['lacrosse'] = sport_onehot[:,2]
df = df.drop('sport',axis=1)

print(df)
