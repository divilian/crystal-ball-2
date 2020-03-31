
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns


df = pd.read_csv("security_cam.csv")

probs = {}
features = df.columns[0:len(df.columns)-1]
target = df.columns[len(df.columns)-1]

for label in df[target].drop_duplicates():
    probs[label] = len(df[df[target] == label])/len(df)
    for feature in features:
        for value in df[feature].drop_duplicates():
            probs[value+"|"+label] = (
                len(df[(df[target] == label) & (df[feature] == value)]) / 
                    len(df[df[target] == label]))

def predict(values):

    # Compute one score for each target label.
    scores = []

    # Keep track of the highest score, and its label, as we go.
    top_score = 0
    top_label = ""

    for label in df[target].drop_duplicates():
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
