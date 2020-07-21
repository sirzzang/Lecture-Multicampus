# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:44:55 2020

@author: sir95
"""

# module import
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np


# change work path
os.getcwd()
os.chdir('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습')
os.getcwd()

# load data
iris = load_iris()

# split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25)
print(f"train input: {X_train.shape}\n train label: {y_train.shape}\n \
      test input: {X_test.shape}\n test label: {y_test.shape}")

# train model, controlling regularization coef.
train_acc_list, test_acc_list = [], []
c_range = np.arange(0.001, 1.0, 0.002) # c 범위 설정
for c in c_range:
    model= LogisticRegression(penalty='l2', C=c, max_iter=1000) # c 조정, max_iter 조정해야 함.
    model.fit(X_train, y_train)
    
    train_pred = model.predict(X_train)
    train_acc_list.append((train_pred==y_train).mean())
    
    test_pred = model.predict(X_test)
    test_acc_list.append((test_pred==y_test).mean())
    
# plot accuracies
plt.figure(figsize=(8,5))
plt.plot(c_range, train_acc_list, label='Train Acc')
plt.plot(c_range, test_acc_list, label='Test Acc')
plt.title('C vs. Accuracy')
plt.xlabel('C')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()
    