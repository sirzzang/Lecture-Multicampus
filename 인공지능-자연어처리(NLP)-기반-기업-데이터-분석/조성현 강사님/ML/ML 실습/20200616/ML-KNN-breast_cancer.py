# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:40:27 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# load data
breast = load_breast_cancer()
dir(breast)
print(breast.feature_names)

# split data
X_train, X_test, y_train, y_test = train_test_split(breast.data, breast.target, test_size=0.2)

# train model
knn_clf = KNeighborsClassifier(n_neighbors=9, p=2, metric='minkowski') # 나머지는 default setting
knn_clf.fit(X_train, y_train)

# calculate train set accuracy
y_train_pred = knn_clf.predict(X_train)
train_acc = (y_train_pred == y_train).mean()
print(f"train set accuracy: {train_acc*100}%")

# calculate test set accuracy
y_test_pred = knn_clf.predict(X_test)
test_acc = (y_test_pred == y_test).mean()
print(f"test set accuracy: {test_acc*100}%")

# control num of neighbors
train_acc_list, test_acc_list = [], []
for i in range(1, 51):
    knn_model = KNeighborsClassifier(n_neighbors=i, p=2, metric='minkowski')
    knn_model.fit(X_train, y_train)
    
    y_train_pred = knn_model.predict(X_train)
    train_acc = (y_train_pred == y_train).mean()
    train_acc_list.append(train_acc)
    print(f"{i} neighbors train set accuracy: {train_acc*100}%")
    
    y_test_pred = knn_model.predict(X_test)
    test_acc = (y_test_pred == y_test).mean()
    test_acc_list.append(test_acc)
    print(f"{i} neighbors test set accuracy: {test_acc*100}%")
    
# plot accuracies
iter_ranges = np.linspace(1, 50)
plt.plot(iter_ranges, train_acc_list, label='train data')
plt.plot(iter_ranges, test_acc_list, label='test data')
plt.xlabel("num. of neighbors")
plt.ylabel("accuracy")
plt.legend(loc="upper right")
plt.show()
