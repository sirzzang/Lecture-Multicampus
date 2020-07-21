# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:16:42 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import confusion_matrix


# load data
iris = load_iris()

# split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# 4 models: KNN, Decision Tree, SVM, logistic regression
# each model with optimal option
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
dt = DecisionTreeClassifier(criterion='gini', max_depth=8)
svm = SVC(kernel='rbf', gamma=0.1, C=1.0, probability=True)
lr = LogisticRegression(max_iter=500)

# Ensemble with 4 models
base_model = [('knn', knn),
              ('decision_tree', dt),
              ('svm_rbf', svm),
              ('logistic_regression', lr)]
ensemble = VotingClassifier(estimators=base_model, voting='soft')

# train models and check result
ensemble.fit(X_train, y_train)

# check accuracy
print('')
print('Train Acc = %.2f' % ensemble.score(X_train, y_train))
print('Test Acc = %.2f' % ensemble.score(X_test, y_test))
print('')

# confusion matrix(row: actual, col: predict)
y_pred= ensemble.predict(X_test)
print('')
print('====== Confusion Matrix ======')
print(confusion_matrix(y_test, y_pred))