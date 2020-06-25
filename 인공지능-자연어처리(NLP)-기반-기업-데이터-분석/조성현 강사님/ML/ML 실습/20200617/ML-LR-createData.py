# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:25:10 2020

@author: sir95
"""

# module import
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# create sample data
def createData(a, b, n):
    result_X, result_y = [], []
    
    for i in range(n):
        x = np.random.normal(0.0, 0.6)
        y = a*x + b+ np.random.normal(0.0, 0.05) # y = ax + b + e, error term 0.0 ~ 0.05
        result_X.append(x)
        result_y.append(y)
    
    return np.array(result_X).reshape(-1, 1), np.array(result_y).reshape(-1, 1)

# prepare data
X, y = createData(0.1, 0.3, 2000) # y = 0.1x + 0.3 + error term, 2000 samples.

# train model
lr_model = LinearRegression()
lr_model.fit(X, y)

# coefficients
print(f"선형회귀 모형 회귀 계수(W): {lr_model.coef_}")
print(f"선형회귀 모형 회귀 절편(b): {lr_model.intercept_}")

# equation
a = lr_model.coef_[0][0]
b = lr_model.intercept_[0]
print(f"추정된 선형회귀 식의 방정식: y = {a}*x + {b}")

# prdeict
y_hat = lr_model.predict(X)

# plot
fig = plt.figure(figsize=(8, 6))
plt.plot(X, y, 'ro', markersize=1.5) #  raw data
plt.plot(X, y_hat) # estimated data
plt.show()

# error term
print(f"시험 데이터 전체 오류(R2-score): {lr_model.score(X, y)}")