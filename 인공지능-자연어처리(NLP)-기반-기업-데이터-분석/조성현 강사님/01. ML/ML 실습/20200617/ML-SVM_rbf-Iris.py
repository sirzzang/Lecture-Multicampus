# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 15:33:05 2020

@author: sir95
"""


# module import
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import mglearn
import numpy as np

# load data
iris = load_iris()

# prepare data: sepal_length, sepal_width
data_X = iris.data[:, [0, 1]]
data_y = iris.target

# split data
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size = 0.2)

# train SVM-rbf model
SVM_rbf = SVC(kernel = 'rbf', gamma=1.0, C=5.0)
print(f"Model: {SVM_rbf}")
SVM_rbf.fit(X_train, y_train)

# predict test set and calculate accuracy
train_acc = SVM_rbf.score(X_train, y_train)
test_acc = SVM_rbf.score(X_test, y_test)
print(f"SVM rbf, train_accuracy: {train_acc * 100}%")
print(f"SVM rbf, test_accuracy: {test_acc * 100}%")

# visualize result
plt.figure(figsize=(7,7))
mglearn.plots.plot_2d_classification(SVM_rbf, X_train, alpha=0.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.legend(iris.target_names)
plt.xlabel('sepal Length')
plt.ylabel('sepal Width')
plt.show()

# find optimal c, gamma
opt_acc, opt_gamma, opt_C = -999, 0, 0
for gamma in np.arange(0.1, 5.0, 0.1):
    print(f"===== gamma: {gamma} =====")
    for C in np.arange(0.1, 5.0, 0.1):
        print(f"     C: {C}")
        model = SVC(kernel='rbf', gamma = gamma, C=C)
        model.fit(X_train, y_train)
        
        test_acc = model.score(X_test, y_test)        

        # optimal condition
        if test_acc > opt_acc:
            print("            Test Accuracy Improved. Change Optimal Parameter Values!")
            opt_gamma = gamma
            opt_C = C
            opt_acc = test_acc

# final optimal parameter values
print('optimal Gamma = %.2f' % opt_gamma)
print('optimal C = %.2f' % opt_C) 
print('best TestSet Accuracy = %.2f' % opt_acc)

# visualize optimal result
SVM_rbf = SVC(kernel = 'rbf', gamma=opt_gamma, C=opt_C)
print(f"Model: {SVM_rbf}")
SVM_rbf.fit(X_train, y_train)

# predict test set and calculate accuracy
train_acc = SVM_rbf.score(X_train, y_train)
test_acc = SVM_rbf.score(X_test, y_test)
print(f"SVM rbf, train_accuracy: {train_acc * 100}%")
print(f"SVM rbf, test_accuracy: {test_acc * 100}%")

# visualize result
plt.figure(figsize=(7,7))
mglearn.plots.plot_2d_classification(SVM_rbf, X_train, alpha=0.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.legend(iris.target_names)
plt.xlabel('sepal Length')
plt.ylabel('sepal Width')
plt.show()

