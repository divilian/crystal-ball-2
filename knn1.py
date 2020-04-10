
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
import io

pts = pd.read_csv(io.StringIO('''
cc_debt,num_yrs,default
28000,1,yes
13000,.5,yes
1000,1.5,no
21000,2,yes
5000,2.5,no
4000,3.1,yes
25500,3.2,yes
24000,4.1,no
14000,4.5,no
2000,5.3,no
25500,5.9,no
20000,6.1,no
6000,7,no
7500,3.2,maybe
'''))
defaulters = pts[pts.default=='yes']
repayers = pts[pts.default=='no']
notsures = pts[pts.default=='maybe']
a = plt.scatter(defaulters.num_yrs, defaulters.cc_debt, color="red", marker="X",
    s=80)
b = plt.scatter(repayers.num_yrs, repayers.cc_debt, color="green", marker="P",
    s=80)
plt.scatter(notsures.num_yrs, notsures.cc_debt, color="blue", marker="$?$",
    s=115)
plt.xlabel('Number of years at present job')
plt.ylabel('Credit card debt ($)')
plt.legend([a,b],["defaulted","repaid"])
plt.show()
plt.savefig("bank_training.png")


def plot_line(x1, y1, x2, y2):
    slope = (y1 - y2) / (x1 - x2)
    yint = - (x2 * slope) + y2
    xpts = np.arange(x1,x2,.01)
    plt.plot(xpts,slope*xpts+yint,linestyle="--",color="grey")

plt.figure()
a = plt.scatter(defaulters.num_yrs, defaulters.cc_debt, color="red", marker="X",
    s=80)
b = plt.scatter(repayers.num_yrs, repayers.cc_debt, color="green", marker="P",
    s=80)
plt.scatter(notsures.num_yrs, notsures.cc_debt, color="blue", marker="$?$",
    s=115)

plot_line(3.1,4000,3.2,7000)
plt.xlabel('Number of years at present job')
plt.ylabel('Credit card debt ($)')
plt.title('1-NN')
plt.legend([a,b],["defaulted","repaid"])
plt.show()
plt.savefig("bank_training_1nn.png")

plt.figure()
a = plt.scatter(defaulters.num_yrs, defaulters.cc_debt, color="red", marker="X",
    s=80)
b = plt.scatter(repayers.num_yrs, repayers.cc_debt, color="green", marker="P",
    s=80)
plt.scatter(notsures.num_yrs, notsures.cc_debt, color="blue", marker="$?$",
    s=115)

plot_line(3.1,4000,3.2,7000)
plot_line(2.5,5000,3.2,7000)
plot_line(3.2,7000,4.5,14000)
plt.xlabel('Number of years at present job')
plt.ylabel('Credit card debt ($)')
plt.title('3-NN')
plt.legend([a,b],["defaulted","repaid"])
plt.show()
plt.savefig("bank_training_3nn.png")

pts_dist = np.empty(len(pts))
def dist(x,y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
for i in range(len(pts_dist)):
    pts_dist[i] = dist((pts.iloc[i].cc_debt, pts.iloc[i].num_yrs),
        (pts.iloc[-1].cc_debt, pts.iloc[-1].num_yrs))
pts['dist'] = pts_dist

def zscores(arr):
    return (arr - arr.mean()) / arr.std()

plt.figure()
pts.cc_debt = zscores(pts.cc_debt)
pts.num_yrs = zscores(pts.num_yrs)
defaulters = pts[pts.default=='yes']
repayers = pts[pts.default=='no']
notsures = pts[pts.default=='maybe']
a = plt.scatter(defaulters.num_yrs, defaulters.cc_debt, color="red", marker="X",
    s=80)
b = plt.scatter(repayers.num_yrs, repayers.cc_debt, color="green", marker="P",
    s=80)
plt.scatter(notsures.num_yrs, notsures.cc_debt, color="blue", marker="$?$",
    s=115)

#plot_line(3.1,4000,3.2,7000)
#plot_line(2.5,5000,3.2,7000)
#plot_line(3.2,7000,4.5,14000)
plt.xlabel('Z-score -- Job seniority')
plt.ylabel('Z score -- Credit card debt')
plt.title('Z-score normalized data')
plt.legend([a,b],["defaulted","repaid"])
plt.show()
plt.savefig("bank_training_zscore.png")

def dist(x,y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


for row in pts.itertuples():
    if row.default != 'maybe':
        print("mystery man is {} from ({},{})".format(
            dist((3.2,7500),(row.num_yrs,row.cc_debt)),
            row.num_yrs,row.cc_debt))
