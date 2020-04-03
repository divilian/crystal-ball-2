
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns


t = pd.read_csv("security_cam.csv")

probs = {}
features = t.columns[0:len(t.columns)-1]
target = t.columns[len(t.columns)-1]

for label in t[target].drop_duplicates():
    probs[label] = len(t[t[target] == label])/len(t)
    for feature in features:
        for value in t[feature].drop_duplicates():
            probs[value+"|"+label] = (
                len(t[(t[target] == label) & (t[feature] == value)]) / 
                    len(t[t[target] == label]))

def predict(values):

    # Compute one score for each target label.
    scores = []

    # Keep track of the highest score, and its label, as we go.
    top_score = 0
    top_label = ""

    for label in t[target].drop_duplicates():
        score = probs[label]                   # Start with the prior
        for value in values:
            score *= probs[value+"|"+label]    # Multiply in conditionals
        scores.append(score)

        # If the score we just computed is the highest so far, we have a
        # new most-likely label.
        if score > top_score:
            top_score = score
            top_label = label

    return [ top_label, top_score / sum(scores) ]
