
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

contribs = pd.read_csv("contribs.csv")

print(contribs.Date.head())
print(contribs.Amt.head())

contribs = pd.read_csv("contribs.csv", parse_dates=['Date'])

contribs.Amt = contribs.Amt.str[1:].astype(int)

print(contribs.Date.head())
print(contribs.Amt.head())

print(contribs.sort_values(['Date']))
print(contribs[contribs.Date < dt.date(year=2016, month=11, day=8)])
contribs.Date.hist(bins=50)
#contribs['after_election'] = contribs.realdate > election_date
#contribs.boxplot("amount",by=["Party","after_election"])
