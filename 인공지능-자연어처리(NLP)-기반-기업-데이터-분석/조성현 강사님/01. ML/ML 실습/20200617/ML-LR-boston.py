# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:35:40 2020

@author: sir95
"""

# module import
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import random


# load and prepare data
boston = load_boston()
data_X = boston.data
data_y = boston.target
print(f"X: {data_X.shape}, y: {data_y.shape}")

# split data
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.2)

# train model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
print(f"fitted LR model: {lr_model.coef_}")

# target price 아무 데이터로나 추정: reshape해야 한다.
rand_num = random.randint(1, len(data_X))
sample_X = X_train[rand_num]
sample_X = sample_X.reshape(1, -1) # 식에 넣을 수 있으려면 2차원으로 만들어야 한다.
print(f"random X data shape: {sample_X.shape}")
sample_X_pred = lr_model.predict(sample_X)
print(f"predicted sample data's price: {sample_X_pred}")
sample_X_real = boston.target[rand_num]
print(f"real sample data's price: {sample_X_real}")
print(f"predicted vs. target: {sample_X_pred[0]-sample_X_real}")
print("추정 오류(rmse): %.4f" % np.sqrt(np.square(sample_X_real - sample_X_pred)))

# 시험 데이터 전체의 오류를 rmse로 계산: 수작업 vs. score 함수
y_pred = lr_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # mse계산 후 루트
print(f"시험 데이터 전체 rmse: {rmse}")

# manual vs. score 함수
ssr = np.sum(np.square(y_pred - y_test))
sst = np.sum(np.square(y_test - y_test.mean()))
manual_r2 = 1 - (ssr/sst)
sklearn_r2 = lr_model.score(X_test, y_test)
print(f"Manual R2: {manual_r2} vs. Sklearn R2: {sklearn_r2}")