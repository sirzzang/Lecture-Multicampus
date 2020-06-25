# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 05:57:19 2020

@author: sir95
"""

# module import
from sklearn.ensemble import IsolationForest
import numpy as np

# set data: 6row * 1col
X_data = np.array([2, 2.5, 3.8, 4.1, 10.5, 15.4]).reshape(-1, 1)

# iForest model
def iForest(num_of_models, data):
    iForest = IsolationForest(n_estimators=num_of_models)
    iForest.fit(data)
    
    # prediction
    y_pred = iForest.predict(data)

    # anomaly score
    score = abs(iForest.score_samples(data))
    
    return y_pred, score


# compare: 1 vs. 50
model_1_pred, model_1_score = iForest(1, X_data)
print('판정 결과: tree 1개일 때')
print(model_1_pred)
print('========== anomaly score ==========')
print(model_1_score)

# anomaly score
model_2_pred, model_2_score = iForest(50, X_data)
print('판정 결과: tree 50개일 때')
print(model_2_pred)
print('========== anomaly score ==========')
print(model_2_score)
