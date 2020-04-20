import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

from sklearn.preprocessing import OneHotEncoder
from sklearn.naive_bayes import CategoricalNB
from pandas.api.types import is_numeric_dtype

w = pd.read_csv("security_cam2.csv")
train = w.sample(frac=.7)
test = w.drop(train.index)

# Given a DataFrame and a set of column headings to include, return a NumPy
# matrix with all these features prepared and concatenated. "Prepared" means:
# (1) for categorical variables, one-hot them, and (2) for numeric variables,
# compute their Z-scores.
def prepare_this_puppy(df, include):
    ohe = OneHotEncoder(sparse=False)
    prepared_features = []
    for feature in include:
        if is_numeric_dtype(df[feature].dtype):
            thing = df[feature]-df[feature].mean()/df[feature].std()
            prepared_features.append(np.array([thing.values]).transpose())
        else:
            prepared_features.append(ohe.fit_transform(
                df[feature].values.reshape(-1,1)))
    return np.concatenate(prepared_features, axis=1)

feature_sets = [ 'lightsaber,face,height,demeanor',
                 'lightsaber,face,height',
                 'lightsaber,face,demeanor',
                 'lightsaber,face',
                 'lightsaber,height,demeanor',
                 'lightsaber,height',
                 'lightsaber,demeanor',
                 'lightsaber',
                 'face,height,demeanor',
                 'face,height',
                 'face,demeanor',
                 'face',
                 'height,demeanor',
                 'height',
                 'demeanor' ]
scores = pd.Series()

for feature_set in feature_sets:
    train_features = prepare_this_puppy(train,feature_set.split(","))
    test_features = prepare_this_puppy(test,feature_set.split(","))
    naive_bayes = CategoricalNB()
    naive_bayes.fit(train_features,train.type.values)
    nb_predictions = naive_bayes.predict(test_features)
    scores[feature_set] = round(
        sum(nb_predictions == test.type)/len(test)*100,2)

scores = scores.sort_values(ascending=False)[:10]
for feature_set, score in scores.items():
    print("{}: {:.2f}".format(feature_set,score))
