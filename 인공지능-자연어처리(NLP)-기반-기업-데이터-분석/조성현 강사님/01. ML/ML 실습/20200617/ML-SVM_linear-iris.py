# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:43:32 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
import mglearn
import matplotlib.pyplot as plt
import numpy as np


# load data
iris = load_iris()

# prepare data: sepal_length, sepal_width
data_X = iris.data[:, [0, 1]]
data_y = iris.target

# split data
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size = 0.2)

# train SVM model
SVM = SVC(kernel = 'linear')
SVM.fit(X_train, y_train)

# predict test set and calculate accuracy
train_acc = SVM.score(X_train, y_train)
test_acc = SVM.score(X_test, y_test)
print(f"SVM linear, train_accuracy: {train_acc * 100}%")
print(f"SVM linear, test_accuracy: {test_acc * 100}%")

# visualize
plt.figure(figsize=(7,7))
mglearn.plots.plot_2d_classification(SVM, X_train, alpha=0.1)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.legend(iris.target_names)
plt.title('SVM, linear kernel')
plt.xlabel('sepal Length')
plt.ylabel('sepal Width')
plt.show()

# C 조정해 보기
train_acc_list, test_acc_list = [], []
for c in np.linspace(1, 20, num=20):
    svm_model = SVC(kernel='linear', C=c)
    svm_model.fit(X_train, y_train)
    
    train_acc = svm_model.score(X_train, y_train)
    test_acc = svm_model.score(X_test, y_test)
    
    train_acc_list.append(train_acc)
    test_acc_list.append(test_acc)
    
plt.plot(train_acc_list, label='Train Acc', marker='o')
plt.plot(test_acc_list, label='Test Acc', marker='o')
plt.xlabel('C')
plt.ylabel('Accuracy')
plt.title('C vs. Accuracy', fontsize=18)
plt.legend(loc='center right')
plt.show()


################### 똑같은 과정을 linearSVC로 해봅시다. #############################

# train model
model = LinearSVC()
model.fit(X_train, y_train)

# predict test set and calculate accuracy
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)
print(f"LinearSVC, train_accuracy: {train_acc * 100}%")
print(f"LinearSVC, test_accuracy: {test_acc * 100}%")

# visualize
plt.figure(figsize=(7,7))
mglearn.plots.plot_2d_classification(model, X_train, alpha=0.1)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.legend(iris.target_names)
plt.title('LinearSVC')
plt.xlabel('sepal Length')
plt.ylabel('sepal Width')
plt.show()

# C 조정해 보기
train_acc_list, test_acc_list = [], []
for c in range(1, 100):
    model = LinearSVC(C=c, max_iter=2000)
    model.fit(X_train, y_train)
    
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    
    train_acc_list.append(train_acc)
    test_acc_list.append(test_acc)
    
plt.plot(train_acc_list, label='Train Acc', marker='o')
plt.plot(test_acc_list, label='Test Acc', marker='o')
plt.xlabel('C')
plt.ylabel('Accuracy')
plt.title('C vs. Accuracy', fontsize=18)
plt.legend(loc='center right')
plt.show()