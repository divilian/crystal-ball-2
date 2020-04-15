
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt


np.random.seed(123)

# Run Naive Bayes, and return the accuracy as a percentage.
def naive_bayes(s):
    train = s.sample(frac=.7)
    test = s.drop(train.index)

    naive_bayes = CategoricalNB()
    oe = OrdinalEncoder()
    converted_features = oe.fit_transform(train.drop(['type'], axis=1))
    naive_bayes.fit(converted_features, train.type)
    nb_predictions = naive_bayes.predict(
        oe.fit_transform(test.drop(['type'], axis=1)))
    return (nb_predictions == test.type).sum() / len(test) * 100


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

nb_performances = np.empty(200)
for i in range(200):
    nb_performances[i] = naive_bayes(s)

knn_performances = np.empty(200)
for i in range(200):
    knn_performances[i] = kNN(s, 3)

results = pd.DataFrame({'Naive Bayes':nb_performances, '3-NN':knn_performances})
results_l = pd.melt(results, [], var_name='classifier', value_name='accuracy')
facet = sns.FacetGrid(results_l, col='classifier', hue='classifier',
    palette={'Naive Bayes':'blue', '3-NN':'red'})
facet.map(plt.hist, 'accuracy', bins=20)
plt.savefig("nb_knn_comparison.png")

print("Naive Bayes: mean accuracy {:.2f}%.".format(nb_performances.mean()))
print("3-NN: mean accuracy {:.2f}%.".format(knn_performances.mean()))

print("Naive Bayes: standard deviation {:.2f}.".format(nb_performances.std()))
print("3-NN: standard deviation {:.2f}.".format(knn_performances.std()))


