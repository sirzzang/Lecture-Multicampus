# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:18:27 2020

@author: sir95
"""

# module import
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random

# change work path
os.getcwd()
os.chdir('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습')
os.getcwd()

# load data
credit = pd.read_csv('./dataset/credit_data.csv')

# prepare data
credit = np.array(credit, dtype=np.float32)
X_data = credit[:, :-1]
y_data = credit[:, -1]

# split data
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)

# train logistic regression model
model = LogisticRegression(verbose=1)
model.fit(X_train, y_train)

# caculate accuracy
print(f"Train Accuracy: {model.score(X_train, y_train)}")
print(f"Test Accuracy: {model.score(X_test, y_test)}")

# check model
print(f"Model Coefficients: {model.coef_}")
print(f"Model Intercept: {model.intercept_}")
print(f"Model Classes: {model.classes_}")

# predict random data manually
rand_num = random.randint(1, X_test.shape[0])
sample_test_data = X_test[rand_num]   # 여기서는 reshape 필요 없음.
sample_pred_manually = np.dot(model.coef_[0], sample_test_data) + model.intercept_
sample_pred_prob_manually = 1.0 / (1.0 + np.exp(-sample_pred_manually)) # 공식에 넣는다
print(f"Probability of the Class Manual: {sample_pred_prob_manually}")

# predict sample data by scikit-learn 
sample_test_data = sample_test_data.reshape(1, -1) # 여기서는 reshape 필요함.
print(f"Probability of the Class: {model.predict_proba(sample_test_data)}")
print(f"Predicted Class of the Sample Data: {model.predict(sample_test_data)}")


