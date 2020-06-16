# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:13:15 2020

@author: sir95
"""

# module import
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# load data
income = pd.read_csv("C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/data/income.csv",
                     index_col=False)
income['education_num']

# 범주형 변수를 숫자로 바꾼다.
income.columns
income.info() # workclass, marital_status, occupation, relationship, race, sex, native_country, income
cat_features = ['workclass', 'marital_status', 'occupation', 'relationship',\
                'race', 'sex', 'hours_per_week', 'native_country', 'income']
for c in cat_features:
    income[c] = pd.Categorical(income[c]).codes

income # 변환된 것을 확인
data = np.array(income) # dataframe -> np.array

# prepare data
X = data[:, 0:10] # 마지막 컬럼은 라벨
y = data[:, -1] 

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train, record accuracies
train_gini, test_gini = [], []
train_entropy, test_entropy = [], []

for i in range(1, 21):
    # decision tree classifier by Gini
    dt_gini = DecisionTreeClassifier(criterion='gini', max_depth=i)
    dt_gini.fit(X_train, y_train)    
    train_gini_acc = dt_gini.score(X_train, y_train)
    test_gini_acc = dt_gini.score(X_test, y_test)
    train_gini.append(train_gini_acc)
    test_gini.append(test_gini_acc)
    
    # decision tree classifier by Entropy
    dt_entropy = DecisionTreeClassifier(criterion='entropy', max_depth=i)
    dt_entropy.fit(X_train, y_train)    
    train_entropy_acc = dt_entropy.score(X_train, y_train)
    test_entropy_acc = dt_entropy.score(X_test, y_test)
    train_entropy.append(train_entropy_acc)
    test_entropy.append(test_entropy_acc)

# plot accuracies
iter_ranges = np.linspace(1, 20, num=20, dtype=np.int8)
plt.plot(iter_ranges, train_gini, label='Train Acc Gini')
plt.plot(iter_ranges, test_gini, label='Test Acc Gini')
plt.plot(iter_ranges, train_entropy, label='Train Acc Entropy')
plt.plot(iter_ranges, test_entropy, label='Test Acc Entropy')
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.legend(loc='upper right')
plt.show()