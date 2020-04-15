
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt


np.random.seed(123)

## Run kNN, and return the accuracy as a percentage.
def kNN(s, k):
    train = s.sample(frac=.7)
    test = s.drop(train.index)

    knn = KNeighborsClassifier(n_neighbors=k)
    ohe = OneHotEncoder()
    one_hotted_features = ohe.fit_transform(train.drop(['type'], axis=1))
    knn.fit(one_hotted_features, train.type)
    knn_predictions = knn.predict(
        ohe.fit_transform(test.drop(['type'], axis=1)))
    return (knn_predictions == test.type).sum() / len(test) * 100


s = pd.read_csv("security_cam.csv")

ks = np.array([])
performances = np.array([])
for k in range(1,30,2):
    print("k={}".format(k))
    for i in range(10):
        ks = np.append(ks, k)
        performances = np.append(performances, kNN(s, k))
results = pd.DataFrame({'k':ks, 'performance':performances})
agg_results = results.groupby('k').performance.mean()
agg_results.plot(kind='line', color='red',ylim=(70,100), xlim=(0,30))
plt.xticks(range(1,30,2))
plt.title("Performance vs. $k$")
plt.ylabel("% accuracy")
[ plt.axvline(x=i, linestyle="dotted", color="gray") for i in range(1,30,2) ]
plt.show()
plt.savefig("varying_k.png")


