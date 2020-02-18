import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

actors = pd.read_csv('actors.csv')
actors = actors.drop(['year'],axis=1)
movies = pd.read_csv('movies.csv')

children = pd.read_csv('children.csv')
costumes = pd.read_csv('costumes.csv')
accessories = pd.read_csv('accessories.csv')



am = pd.merge(actors,movies,left_on='film',right_on='title')
print(am)

actors = pd.read_csv('actors.csv')   # Reload file to get birth year column
am = pd.merge(actors,movies,left_on='film',right_on='title')
print(am)    # Shows rename "year_x" and "year_y"
c = list(am.columns)
c[3] = 'birth year'
c[6] = 'release'
am.columns = c
print(am)

am = pd.merge(actors,movies,left_on='film',right_on='title',how='left')
print(am)

am = pd.merge(actors,movies,left_on='film',right_on='title',how='right')
print(am)

am = pd.merge(actors,movies,left_on='film',right_on='title',how='outer')
print(am)


print(children)
print(costumes)
children_costumes = pd.merge(children,costumes,on="costume")
print(children_costumes)
children_costumes = pd.merge(children,costumes,on="costume",how="left")
print(children_costumes)
print("Shopping list:")
print(pd.merge(children,costumes).accessory.value_counts())
print("Dangerous:")
print(children_costumes[(children_costumes.age < 10) &
(children_costumes.accessory=="wand")])
full = pd.merge(children_costumes, accessories, on="accessory")
print("These kids will cost ${}.".format(full.cost.sum()))
