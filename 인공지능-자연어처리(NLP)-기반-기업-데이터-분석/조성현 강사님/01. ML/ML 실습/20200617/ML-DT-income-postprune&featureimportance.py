# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:09:13 2020

@author: sir95
"""

# module import
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt

# load data
income = pd.read_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/income.csv', index_col=False)

# check data
income.info()
income.columns

# handle categorical variables
cat_features = ['workclass', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'income']
for c in cat_features:
    income[c] = pd.Categorical(income[c]).codes

# prepare data
data = np.array(income)
data_X = data[:, 0:-1]
data_Y = data[:, -1]

# split data
X_train, X_test, y_train, y_test = train_test_split(data_X, data_Y, test_size=0.2)

# control alpha and check results
dt_clf = DecisionTreeClassifier(random_state=42) # fix random seed, gini.
path = dt_clf.cost_complexity_pruning_path(X_train, y_train) # return: ccp_alphas, impurities.
ccp_alphas, impurities = path['ccp_alphas'], path['impurities']

# plot path: 앞부분이 너무 작아서 조밀하다.
plt.figure(figsize=(8,4))
plt.plot(ccp_alphas[:-1], impurities[:-1], marker='^', drawstyle='steps-post')
plt.xlabel('CCP Alpha')
plt.ylabel('Impurity')
plt.title('Finding Effective Alpha over training set')
plt.show()

# ccp_alpha가 너무 작은 것은 제외한다.
ccp_alphas = ccp_alphas[np.where(ccp_alphas > 0.0001)]
ccp_alphas

# classifier별로 다르게 저장한다.
dt_clfs = [] # dt classifier를 저장할 리스트
for i, a in enumerate(ccp_alphas):
    # train model
    dt_clf = DecisionTreeClassifier(random_state=42, criterion='gini', ccp_alpha=a)
    dt_clf.fit(X_train, y_train)
    dt_clfs.append(dt_clf) # save classifier
    
    print(f"{i}th ccp_alpha: {a}")
    # check model
    print(f"     Num of Nodes: {dt_clf.tree_.node_count}")
    print(f"     Tree Depth: {dt_clf.tree_.max_depth}")

# depth가 0인 마지막 트리는 제외한다.
dt_clfs = dt_clfs[:-1]
ccp_alphas = ccp_alphas[:-1]

# plot : num_of_nodes, max_depths
num_of_nodes = [dt_clf.tree_.node_count for dt_clf in dt_clfs]
depths = [dt_clf.tree_.max_depth for dt_clf in dt_clfs]
train_scores = [dt_clf.score(X_train, y_train) for dt_clf in dt_clfs]
test_scores = [dt_clf.score(X_test, y_test) for dt_clf in dt_clfs]

plt.figure(figsize=(8,4))
plt.plot(ccp_alphas, num_of_nodes, marker='^')
plt.title('CCP_alphas vs. Nodes')
plt.show()

plt.figure(figsize=(8,4))
plt.plot(ccp_alphas, depths, marker='^')
plt.title('CCP_alphas vs. Depths')
plt.show()

plt.figure(figsize=(8,4))
plt.plot(ccp_alphas, train_scores, marker='o', label='Train Set Acc')
plt.plot(ccp_alphas, test_scores, marker='o', label='Test Set Acc')
plt.title('CCP_alphas vs. Scores')
plt.legend(loc='upper right')
plt.show()


# find optimal tree
n=70 # 뒷부분의 alpha가 너무 크기 때문에 제외
opt_alpha = ccp_alphas[np.argmax(test_scores[:n])]
opt_dt = DecisionTreeClassifier(ccp_alpha=opt_alpha)
opt_dt.fit(X_train, y_train)
print("optimal ccp_alpha = %.8f" % opt_alpha)
print("optimal tree's test accuracy: %.4f" % opt_dt.score(X_test, y_test))

# analyze feature importances
opt_feature_importance = opt_dt.feature_importances_
feature_name = list(income.columns)
n_feature = X_train.shape[1]
idx = np.arange(n_feature)

# plot feature importances
plt.barh(idx, opt_feature_importance, align='center')
plt.yticks(idx, feature_name, size=12)
plt.xlabel('feature importances', size=15)
plt.ylabel('feature', size=15)
plt.show()

