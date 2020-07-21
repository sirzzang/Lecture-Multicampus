# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:16:41 2020

@author: sir95
"""


# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix
import numpy as np


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

# Ensemble with 4 models: cumulate bagging results
prob = np.zeros((y_test.shape[0], iris.target_names.shape[0])) # 각각의 시험 데이터가 해당 클래스일 확률 누적
base_model = [knn, dt, svm, lr]
for model in base_model:
    bag = BaggingClassifier(base_estimator=model, n_estimators=100, bootstrap=True)
    bag.fit(X_train, y_train)
    
    prob += bag.predict_proba(X_test) # 중요: 누적하는 부분!

# 확률의 누적합이 가장 큰 클래스를 찾아 정확도 측정
y_pred = np.argmax(prob, axis=1) # 열 방향으로 argmax
accuracy = (y_test == y_pred).mean()
print('')
print('Test Acc = %.2f' % accuracy)

# confusion matrix
print('')
print('====== Confusion Matrix ======')
print(confusion_matrix(y_test, y_pred))