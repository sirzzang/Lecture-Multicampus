# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:07:48 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import numpy as np

# load data
breast = load_breast_cancer()

# split train, test data
X_train, X_test, y_train, y_test = train_test_split(breast.data, breast.target, test_size=0.2)

######## decision tree model by Gini ########
# control max_depth parameter
train_Gini, test_Gini = [], []

for i in range(1, 16):
    # train model
    dt_gini = DecisionTreeClassifier(criterion='gini', max_depth=i)
    dt_gini.fit(X_train, y_train)
    
    # record accuracies
    train_acc = dt_gini.score(X_train, y_train) # train_acc
    train_Gini.append(train_acc)
    print(f"max_depth: {i}, train_accuracy: {train_acc * 100}%")
    test_acc = dt_gini.score(X_test, y_test) # test_acc
    test_Gini.append(test_acc)
    print(f"max_depth: {i}, test_accuracy: {test_acc * 100}%")

# plot accuracies
iter_ranges = np.linspace(1, 15, num=15)
plt.plot(iter_ranges, train_Gini, label="Train Acc, Gini")
plt.plot(iter_ranges, test_Gini, label="Test Acc, Gini")
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.legend(loc="upper right")
plt.show()

######## decision tree model by Entropy ########
# control max_depth parameter
train_Entropy, test_Entropy = [], []

for i in range(1, 16):
    # train model
    dt_entropy = DecisionTreeClassifier(criterion='entropy', max_depth=i)
    dt_entropy.fit(X_train, y_train)
    
    # record accuracies
    train_acc = dt_entropy.score(X_train, y_train) # train_acc
    train_Entropy.append(train_acc)
    print(f"max_depth: {i}, train_accuracy: {train_acc * 100}%")
    test_acc = dt_entropy.score(X_test, y_test) # test_acc
    test_Entropy.append(test_acc)
    print(f"max_depth: {i}, test_accuracy: {test_acc * 100}%")

# plot accuracies
iter_ranges = np.linspace(1, 15, num=15)
plt.plot(iter_ranges, train_Entropy, label="Train Acc, Entropy")
plt.plot(iter_ranges, test_Entropy, label="Test Acc, Entropy")
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.legend(loc="upper right")
plt.show()