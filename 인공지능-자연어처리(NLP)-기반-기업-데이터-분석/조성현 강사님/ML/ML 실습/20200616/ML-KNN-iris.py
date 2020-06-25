# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:07:39 2020

@author: sir95
"""

# module import
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# load data
iris = load_iris() # dict 형태의 데이터

# check data
print(iris)
print(dir(iris))
iris.keys() # iris의 key
iris.data # 행과 열로 구성되어 있음.
print(f"iris data : {iris.data.shape}") # 2차원, 150행 4열.
iris.feature_names
iris.filename
iris.target

# split data set
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# train KNN Classifier
knn_clf = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn_clf.fit(X_train, y_train)

# calculate train set accuracy
y_train_pred = knn_clf.predict(X_train)
train_acc = (y_train_pred == y_train).mean()
print(f"train set accuracy: {train_acc*100}%")

# calculate test set accuracy
y_test_pred = knn_clf.predict(X_test)
test_acc = (y_test_pred == y_test).mean()
print(f"test set accuracy: {test_acc*100}%")

# change number of neighbors
train_acc_list = []
test_acc_list = []
for i in range(1, 51):
    # train model
    knn = KNeighborsClassifier(n_neighbors=i, p=2, metric='minkowski')
    knn.fit(X_train, y_train)
    
    # train set accuracy
    y_train_pred = knn.predict(X_train)
    train_acc = (y_train_pred==y_train).mean()
    print(f"{i} neighbors train set accuracy: {train_acc*100}%")
    train_acc_list.append(train_acc)
    
    # test set accuracy
    y_test_pred = knn.predict(X_test)
    test_acc = (y_test_pred==y_test).mean()
    print(f"{i} neighbors test set accuracy: {test_acc*100}%")
    test_acc_list.append(test_acc)

# plot accuracies
iter_ranges = np.linspace(1, 50)
plt.plot(iter_ranges, train_acc_list, label='train data')
plt.plot(iter_ranges, test_acc_list, label='test data')
plt.xlabel("num. of neighbors")
plt.ylabel("accuracy")
plt.legend(loc="upper right")
plt.show()
