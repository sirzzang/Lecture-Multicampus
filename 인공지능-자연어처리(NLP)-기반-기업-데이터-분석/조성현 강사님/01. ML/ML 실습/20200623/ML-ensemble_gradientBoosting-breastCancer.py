# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:13:07 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier


# load data
cancer = load_breast_cancer()

# split data
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2)

# gradient boosting classifier
gboost = GradientBoostingClassifier(loss='deviance',
                                    learning_rate=0.1,
                                    n_estimators=100,
                                    max_depth=3)
gboost.fit(X_train, y_train)

# accuracies
y_pred_train = gboost.predict(X_train)
train_accuracy = (y_pred_train == y_train).mean()
y_pred_test = gboost.predict(X_test)
test_accuracy = (y_pred_test == y_test).mean()
print('')
print('Train Acc = %.2f' % train_accuracy)
print('Test Acc = %.2f' % test_accuracy)