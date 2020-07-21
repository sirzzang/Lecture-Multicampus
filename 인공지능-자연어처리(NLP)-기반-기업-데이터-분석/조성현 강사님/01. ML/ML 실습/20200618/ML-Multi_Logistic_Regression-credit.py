# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:37:14 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# load data
iris = load_iris()

# split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# train model
model = LogisticRegression()
model.fit(X_train, y_train)

# calculate accuracies
print(f"Train Accuracy: {model.score(X_train, y_train)}")
print(F"Test Accuracy: {model.score(X_test, y_test)}")

# check model
print(f"Model Coefficients: {model.coef_}")
print(f"Model Bias: {model.intercept_}")

# predict data manually
sample_data = X_test[10] # reshape 필요 없음.
sample_data_pred_manual = np.dot(model.coef_, sample_data) + model.intercept_
sample_data_pred_res = np.exp(sample_data_pred_manual)
sample_data_pred_res
res_manual = np.argmax(sample_data_pred_res)
res_manual

# predict random data with scikit-learn
sample_pred = model.predict_proba(sample_data.reshape(1, -1))
res_sklearn = np.argmax(sample_pred)
res_sklearn
