
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.neighbors import KNeighborsClassifier

np.random.seed(125)

s = pd.read_csv("security_cam.csv")


def get_sample(s):
    train = s.sample(frac=.7)
    test = s.drop(train.index)

    train_features = train.drop(['type'],axis=1)
    train_label = train.type.values
    test_features = test.drop(['type'],axis=1)
    test_label = test.type.values

    return [ train_features, train_label, test_features, test_label ]


# Naive Bayes.
def naive_bayes(s):
    train_features, train_label, test_features, test_label = get_sample(s)
    naive_bayes = CategoricalNB()
    oe = OrdinalEncoder()
    naive_bayes.fit(oe.fit_transform(train_features), train_label)
    nb_predictions = naive_bayes.predict(oe.fit_transform(test_features))
    return test_features[nb_predictions != test_label]


## kNN.
def kNN(s):
    train_features, train_label, test_features, test_label = get_sample(s)
    knn = KNeighborsClassifier(n_neighbors=3)
    ohe = OneHotEncoder()
    knn.fit(ohe.fit_transform(train_features), train_label)
    knn_predictions = knn.predict(ohe.fit_transform(test_features))
    return test_features[knn_predictions != test_label]


print("Naive Bayes got {:.2f}% correct.".format(
    100 - len(naive_bayes(s))/(len(s)*.3)*100))
print("kNN(3) got {:.2f}% correct.".format(
    100 - len(kNN(s))/(len(s)*.3)*100))


nb_correct = [ len(naive_bayes(s)) for _ in range(100) ]
knn_correct = [ len(kNN(s)) for _ in range(100) ]

## Which?
#nb_right = []
#knn_right = []
#for i in range(len(nb_predictions)):
#    if nb_predictions[i] == test.type.iloc[i] != knn_predictions[i]:
#        nb_right.append(i)
#    if nb_predictions[i] != test.type.iloc[i] == knn_predictions[i]:
#        knn_right.append(i)
#
#nb_right_examples = test.iloc[nb_right]
#knn_right_examples = test.iloc[knn_right]
#
#
#print("kNN got these wrong:")
#print(nb_right_examples)
#print("\nNB got these wrong:")
#print(knn_right_examples)


