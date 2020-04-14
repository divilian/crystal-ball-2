
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
import io

NUM = 1000
default = np.random.choice(['yes','no'], p=[.3,.7], size=NUM)
default[0] = 'yes'    # force markers to be how I want them in the plot
cc_debt = np.where(default == 'yes',
    np.random.normal(12000,4000,NUM).clip(0,40000).astype(int),
    np.random.normal(7000,3000,NUM).clip(0,40000).astype(int))
num_yrs = np.where(default == 'yes',
    np.random.uniform(0,10,NUM).round(1),
    np.random.uniform(2,12,NUM).round(1))
bank = pd.DataFrame({'cc_debt':cc_debt, 'num_yrs':num_yrs,
    'default':default})[['cc_debt','num_yrs','default']]

defaulters = bank[bank.default=='yes']
repayers = bank[bank.default=='no']
notsures = bank[bank.default=='maybe']
a = plt.scatter(defaulters.num_yrs, defaulters.cc_debt, color="red", marker="X",
    s=40)
b = plt.scatter(repayers.num_yrs, repayers.cc_debt, color="green", marker="P",
    s=30)
plt.xlabel('Number of years at present job')
plt.ylabel('Credit card debt ($)')
plt.legend([a,b],["defaulted","repaid"])
#plt.show()
#plt.savefig("synthesized_bank.png")

def zscores(arr):
    return (arr - arr.mean()) / arr.std()

cc_debt_mean = bank.cc_debt.mean()
cc_debt_std = bank.cc_debt.std()
num_yrs_mean = bank.num_yrs.mean()
num_yrs_std = bank.num_yrs.std()

bank.cc_debt = zscores(bank.cc_debt)
bank.num_yrs = zscores(bank.num_yrs)

def dist(x,y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def predict(cc_debt, num_yrs, k):
    bank['dists'] = dist([bank.cc_debt, bank.num_yrs],
        [(cc_debt - cc_debt_mean) / cc_debt_std,
        (num_yrs - num_yrs_mean) / num_yrs_std])
    k_closest_pts = bank.sort_values('dists').iloc[0:k]
    return k_closest_pts.default.value_counts().index[0]


train = bank.sample(frac=.7)
test = bank.drop(train.index)

num_correct = 0
for i in range(len(test)):
    row = test.iloc[i]
    p = predict(row['cc_debt'], row['num_yrs'], 3)
    if p == row['default']:
        num_correct += 1
print("We got {}% correct on the test data.".format(num_correct/len(test)*100))



#pts_dist = np.empty(len(pts))
#
#for i in range(len(pts_dist)):
#    pts_dist[i] = dist((pts.iloc[i].cc_debt, pts.iloc[i].num_yrs),
#        (pts.iloc[-1].cc_debt, pts.iloc[-1].num_yrs))
#pts['dist'] = pts_dist

#plt.figure()
#pts.cc_debt = zscores(pts.cc_debt)
#pts.num_yrs = zscores(pts.num_yrs)
#defaulters = pts[pts.default=='yes']
#repayers = pts[pts.default=='no']
#notsures = pts[pts.default=='maybe']
#a = plt.scatter(defaulters.num_yrs, defaulters.cc_debt, color="red", marker="X",
#    s=80)
#b = plt.scatter(repayers.num_yrs, repayers.cc_debt, color="green", marker="P",
#    s=80)
#plt.scatter(notsures.num_yrs, notsures.cc_debt, color="blue", marker="$?$",
#    s=115)
#
##plot_line(3.1,4000,3.2,7000)
##plot_line(2.5,5000,3.2,7000)
##plot_line(3.2,7000,4.5,14000)
#plt.xlabel('Z-score -- Job seniority')
#plt.ylabel('Z score -- Credit card debt')
#plt.title('Z-score normalized data')
#plt.legend([a,b],["defaulted","repaid"])
#plt.show()
#plt.savefig("bank_training_zscore.png")
#
#def dist(x,y):
#    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
#
#
#for row in pts.itertuples():
#    if row.default != 'maybe':
#        print("mystery man is {} from ({},{})".format(
#            dist((3.2,7500),(row.num_yrs,row.cc_debt)),
#            row.num_yrs,row.cc_debt))
