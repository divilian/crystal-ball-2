
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt


np.random.seed(123)

s = pd.read_csv("security_cam.csv")


def get_sample(s):
    train = s.sample(frac=.7)
    test = s.drop(train.index)
    return [ train, test ]



# Naive Bayes.
def naive_bayes(train, test):
    naive_bayes = CategoricalNB()
    oe = OrdinalEncoder()
    naive_bayes.fit(
        oe.fit_transform(train.drop(['type'], axis=1)),
        train.type)
    nb_predictions = naive_bayes.predict(
        oe.fit_transform(test.drop(['type'], axis=1)))
    return test[nb_predictions != test.type]


## kNN.
def kNN(train, test, k):
    knn = KNeighborsClassifier(n_neighbors=k)
    ohe = OneHotEncoder()
    one_hotted_features = ohe.fit_transform(train.drop(['type'], axis=1))
    knn.fit(one_hotted_features, train.type)
    knn_predictions = knn.predict(
        ohe.fit_transform(test.drop(['type'], axis=1)))
    return test[knn_predictions != test.type]


train, test = get_sample(s)
nb_guessed_wrong = naive_bayes(train, test)
knn_guessed_wrong = kNN(train, test, 3)
print("Naive Bayes got {:.2f}% correct.".format(
    100 - len(nb_guessed_wrong)/len(test)*100))
print("3-NN got {:.2f}% correct.".format(
    100 - len(knn_guessed_wrong)/len(test)*100))


print("kNN got these wrong:")
print(knn_guessed_wrong[~knn_guessed_wrong.isin(nb_guessed_wrong.index)])
print("\nNB got these wrong:")
print(nb_guessed_wrong[~nb_guessed_wrong.isin(knn_guessed_wrong.index)])


nb_num_wrong = np.array(
    [ len(naive_bayes(*get_sample(s))) for _ in range(200) ])
knn_num_wrong = np.array(
    [ len(kNN(*get_sample(s),3)) for _ in range(200) ])
num_test_pts = len(get_sample(s)[1])
nb_accuracy = (num_test_pts - nb_num_wrong) / (num_test_pts) * 100
knn_accuracy = (num_test_pts - knn_num_wrong) / (num_test_pts) * 100

results = pd.DataFrame({'Naive Bayes':nb_accuracy, '3-NN':knn_accuracy})
results_l = pd.melt(results, [], var_name='classifier', value_name='accuracy')
facet = sns.FacetGrid(results_l, col='classifier')
facet.map(plt.hist, 'accuracy', bins=20)
plt.savefig("nb_knn_comparison.png")




