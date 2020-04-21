import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

eggs = []
bacon = []
bananas = []
pizza = []
coffee = []

for i in range(2000):
    eggs.append(np.random.choice([1,0],p=[.7,.3]))
    bacon.append(np.random.choice([1,0],p=[.1,.9]))
    bananas.append(np.random.choice([1,0],p=[.6,.4]))
    pizza.append(np.random.choice([1,0],p=[.8,.2]))
    coffee.append(np.random.choice([1,0],p=[.3,.7]))

for i in range(1000):
    eggs.append(1)
    bacon.append(1)
    bananas.append(np.random.choice([1,0],p=[.6,.4]))
    pizza.append(np.random.choice([1,0],p=[.8,.2]))
    coffee.append(np.random.choice([1,0],p=[.3,.7]))

transactions = pd.DataFrame({
    'eggs':eggs,
    'bacon':bacon,
    'bananas':bananas,
    'pizza':pizza,
    'coffee':coffee})

transactions = transactions.sample(frac=1)

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

itemsets = apriori(transactions, min_support=0.1, use_colnames=True)
print(itemsets.sort_values('support',ascending=False).head(10))
print()
rules = association_rules(itemsets)
print(rules.sort_values('confidence',ascending=False).head(10))
