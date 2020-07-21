# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:24:01 2020

@author: sir95
"""

# module import
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB
import numpy as np

# load data
income = pd.read_csv('./dataset/income.csv', index_col=False)
income.info()
income.columns

# handle categorical variables
cat_features = ['workclass', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country','income']
for c in cat_features:
    income[c] = pd.Categorical(income[c]).codes

# prepare dataset
data = np.array(income)
X_data = data[:, :-1]
y_data = data[:, -1]


# split dataset
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)

# train MultinomialNB : categorical features
cat_N = [1,3,4,5,6,7,9] # categorical feature orders
X_train_cat, X_test_cat = X_train[:, cat_N], X_test[:, cat_N] # categorical features
model_MNB = MultinomialNB(alpha=1.0) # laplace Smoothing
model_MNB.fit(X_train_cat, y_train)

# train GaussianNB : numeric features
gau_N = [0,2,8]
X_train_gau, X_test_gau = X_train[:, gau_N], X_test[:, gau_N]
model_GNB = GaussianNB()
model_GNB.fit(X_train_gau, y_train)

# calculate test accuracy: separate according to cat/gau.
test_prob_cat = model_MNB.predict_proba(X_test_cat)
test_prob_gau = model_GNB.predict_proba(X_test_gau)

# calculate total accuracy
total_prob = np.multiply(test_prob_cat, test_prob_gau)
total_pred = np.argmax(total_prob, axis=1)
total_acc = (total_pred == y_test).mean()
print(f"Test Accuracy: {total_acc * 100}%")
