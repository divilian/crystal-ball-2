
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

contribs = pd.read_csv("contribs.csv")

print(contribs.Date.head())

contribs.Date = pd.to_datetime(contribs.Date)

print(contribs.Date.head())

#contribs = pd.read_csv("contribs.csv", parse_dates=['Date'])
#
#contribs.Amt = contribs.Amt.str[1:].astype(int)
#
#print(contribs.Date.head())
#print(contribs.Amt.head())
#
#print(contribs.sort_values(['Date']))
#print(contribs[contribs.Date < dt.date(year=2016, month=11, day=8)])
#contribs.Date.hist(bins=50)
##contribs['after_election'] = contribs.realdate > election_date
##contribs.boxplot("amount",by=["Party","after_election"])

some_strings = pd.Series(["March 8, 1917", "4-July-1776",
    "5/5/1789", "Jan. 5 2011"])
some_actual_dates = pd.to_datetime(some_strings)
print(some_actual_dates)

blah = pd.Series(["11.12.13"])
print(pd.to_datetime(blah))
