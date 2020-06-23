# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:54:42 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix

# load data
iris = load_iris()

# split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# SVM model
svm = SVC(kernel='rbf', gamma=0.1, C=1.0, probability=True) # probability?
adaboost = AdaBoostClassifier(base_estimator=svm, n_estimators=100)
adaboost.fit(X_train, y_train)

# accuracies
print('')
print('Train Acc = %.2f' % adaboost.score(X_train, y_train))
print('Test Acc = %.2f' % adaboost.score(X_test, y_test))

# confusion matrix
y_pred = adaboost.predict(X_test)
print('')
print('====== Confusion Matrix ======')
print(confusion_matrix(y_test, y_pred))
print('====== Report ======')
print(classification_report(y_test, y_pred, target_names=iris['target_names']))