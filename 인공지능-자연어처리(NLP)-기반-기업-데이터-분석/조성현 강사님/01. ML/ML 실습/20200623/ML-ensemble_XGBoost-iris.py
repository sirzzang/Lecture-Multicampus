# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:35:44 2020

@author: sir95
"""


# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np

# load data
iris = load_iris()

# split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# XGBoostClassifier
# 데이터를 XGBoost의 데이터 형태로 변환
X_train_xgb = xgb.DMatrix(X_train, label=y_train) # ?
print(X_train_xgb)
X_test_xgb = xgb.DMatrix(X_test, label=y_test)
print(X_test_xgb)

# model parameters
param = {
    'eta': 0.3,
    'max_depth': 3, 
    'objective': 'multi:softprob', # softmax
    'num_class': 3
    }

model = xgb.train(params=param, dtrain=X_train_xgb, num_boost_round=20)

# accuracies
y_pred_train = model.predict(X_train_xgb)
y_pred_train = np.argmax(y_pred_train, axis=1)
train_accuracy = (y_pred_train == y_train).mean()
y_pred_test = model.predict(X_test_xgb)
y_pred_test = np.argmax(y_pred_test, axis=1)
test_accuracy = (y_pred_test == y_test).mean()
print('')
print('Train Acc = %.2f' % train_accuracy)
print('Test Acc = %.2f' % test_accuracy)