# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:27:25 2020

@author: sir95
"""


# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


# load data
iris = load_iris()

# split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# train GaussianNB model
model_GNB = GaussianNB()
model_GNB.fit(X_train, y_train)

# calculate accuracies
print(f"Train Accuracy: {model_GNB.score(X_train, y_train)}")
print(f"Test Accuracy: {model_GNB.score(X_test, y_test)}")

# check classes
print(f"num. of classes: {model_GNB.class_count_})")

# check avg, std
print(f"average: {model_GNB.theta_}")
print(f"std: {model_GNB.sigma_}")
