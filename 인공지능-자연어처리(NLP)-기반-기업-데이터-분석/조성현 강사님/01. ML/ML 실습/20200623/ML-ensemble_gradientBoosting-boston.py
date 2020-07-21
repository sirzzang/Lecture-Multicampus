# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:02:53 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import random
import numpy as np
from sklearn.metrics import mean_squared_error

# load data
boston = load_boston()

# split data
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

# Gradient Boosting Classifier
gboost = GradientBoostingRegressor(loss='ls',
                                   learning_rate=0.1,
                                   n_estimators=100,
                                   max_depth=3)
gboost.fit(X_train, y_train)

# 임의의 테스트 데이터에 대한 target price 추정
n = random.randint(1, len(X_test))
sample = X_test[n]
print('')
print(f"임의({n})의 테스트 샘플: {sample}")
price = gboost.predict(sample.reshape(1, -1)) # reshape!
print(f"추정 price: {price}, 실제 price: {y_test[n]}")
print("추정 RMSE(추정 price-실제 price) = %.2f" % np.sqrt(np.square(price-y_test[n])))

# 시험 데이터 전체에 대한 오류
y_pred = gboost.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # RMSE : 값의 범위가 크다.
r2_score = gboost.score(X_test, y_test)
print('')
print("전체 시험 데이터의 오류(RMSE) = %.4f" % rmse)
print("전체 시험 데이터의 R2 score = %.4f" % gboost.score(X_test, y_test))
