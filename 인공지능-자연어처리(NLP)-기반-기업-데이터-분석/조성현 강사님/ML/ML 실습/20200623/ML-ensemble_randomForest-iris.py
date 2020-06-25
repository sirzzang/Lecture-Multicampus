# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:36:07 2020

@author: sir95
"""


# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np


# load data
iris = load_iris()

# split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# ensemble : random forest
rf = RandomForestClassifier(max_depth=5, n_estimators=100)
rf.fit(X_train, y_train)

# check accuracies
print('')
print('Train Acc = %.2f' % rf.score(X_train, y_train))
print('Test Acc = %.2f' % rf.score(X_test, y_test))

# confusion matrix
y_pred = rf.predict(X_test)
print('')
print('====== Confusion Matrix ======')
print(confusion_matrix(y_test, y_pred))
print('')
print('====== Report ======')
print(classification_report(y_test, y_pred, target_names=iris['target_names']))

# subtree accuracies
print('')
print('====== Subtree별 시험 데이터 정확도 ========')
# print(len(rf.estimators_))
for i in range(len(rf.estimators_)):
    subTree = rf.estimators_[i]
    print(f"subtree ({i+1}) 정확도: {subTree.score(X_test, y_test)}")

# classification report 해석
label = np.vstack([y_test, y_pred]).T # 실제 라벨과 예측 라벨

# precision: 예측 라벨이 n인 것 중 실제 라벨이 n인 것의 비율.
def precision(n):
    y = label[label[:, 1] == n] # pred가 n인 데이터
    match = y[y[:, 0] == y[:, 1]] # test와 pred가 같은 데이터
    return match.shape[0] / y.shape[0]
print('')
print('====== PRECISION ======')
print('class 0 precision: %.2f' % precision(0))
print('class 1 precision: %.2f' % precision(1))
print('class 2 precision: %.2f' % precision(2))

# recall: 실제 라벨이 n인 것 중 예측 라벨이 n인 것의 비율.
def recall(n):
    y = label[label[:, 0] == n]
    match = y[y[:, 0] == y[:, 1]]
    return match.shape[0] / y.shape[0]
print('')
print('====== RECALL ======')
print('class 0 recall: %.2f' % recall(0))
print('class 1 recall: %.2f' % recall(1))
print('class 2 recall: %.2f' % recall(2))

# f1 score: precision과 recall의 조화평균.
def f1_score(n):
    p = precision(n)
    r = recall(n)
    return 2*p*r / (p+r)
print('')
print('====== F1 SCORE ======')
print('class 0 f1 score: %.2f' % f1_score(0))
print('class 1 f1 score: %.2f' % f1_score(1))
print('class 2 f1 score: %.2f' % f1_score(2))
    