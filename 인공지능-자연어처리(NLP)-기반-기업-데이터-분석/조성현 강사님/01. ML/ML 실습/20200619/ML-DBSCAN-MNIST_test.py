# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:49:31 2020

@author: sir95
"""

# module import 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import KernelPCA
import pickle

# load data
with open('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/mnist.pickle', 'rb') as f:
    mnist = pickle.load(f)

# prepare data
X_data = mnist.data[:5000, :]
X_image = X_data.copy() # copy raw data

# normalization: standard scaler, transpose(axis=1)
scaler = StandardScaler()
X_input = scaler.fit_transform(X_data.T).T

# DBSCAN cluster
def clusterDBSCAN(eps, min_samples, data):
    db_model = DBSCAN(eps=eps, min_samples=min_samples) # DBSCAN
    db_pred = db_model.fit_predict(data)
    return db_model.labels_, db_pred

# WithOut PCA : 
# 1) eps 바꿔 보자 : pca 없으면 전부 다 노이즈인듯?
for eps in np.arange(0.1, 1.0, 0.1):
    print(f"eps: {eps}")
    db_labels, db_res = clusterDBSCAN(data=X_input, min_samples=5, eps=eps)
    print(db_labels, np.unique(db_labels))

# 2) min_samples 바꿔 보자 
for ms in range(1, 15):
    print(f"min_samples: {ms}")
    db_labels, db_res = clusterDBSCAN(data=X_input, eps=0.1, min_samples=ms)
    print(db_labels, np.unique(db_labels))
    
# 3) 다 바꿔보자.
for eps in np.arange(0.1, 1.0, 0.1):
    print(f"=============== eps: {eps} ===============")
    for ms in range(2, 51):
        print(f"min_samples: {ms}")
        db_labels, db_res = clusterDBSCAN(data=X_input, eps=eps, min_samples=ms)
        print(f"clustering_labels: {np.unique(db_labels)}")


# 4) PCA까지 해보자        
param_dict = []
for n_dim in range(2, 51):
    print(f"         pca: {n_dim}         ")
    pca = KernelPCA(n_components=n_dim, kernel='rbf')
    X_input = pca.fit_transform(X_input)
    for eps in np.arange(0.1, 1.0, 0.1):
        print(f"=============== eps: {eps} ===============")
        for ms in range(2, 51):
            print(f"min_samples: {ms}")
            db_labels, db_res = clusterDBSCAN(data=X_input, eps=eps, min_samples=ms)
            print(f"clustering_labels: {np.unique(db_labels)}")
        
            if len(np.unique(db_labels)) > 1:
                print("    Found!!!!!!    ")
                param_dict.append({'n_dim': n_dim,
                                   'eps': eps,
                                   'min_samples': ms})

print(param_dict)
            

#########################################################################################################    

# 3) pca + eps 바꿔 보자 : 오호? eps 0.2일 때 괜찮은데?
# 근데 전혀 잘 분류되지 않는다^^
for eps in np.arange(0.1, 1.0, 0.1):
    print(f"eps: {eps}----------")
    db_labels, db_res = clusterDBSCAN(data=X_input, min_samples=5, eps=eps)
    print(db_labels, np.unique(db_labels))
    
db_test_labels, db_test_res = clusterDBSCAN(eps=0.2, min_samples=5, data=X_input)
f = plt.figure(figsize=(8, 2))
for k in np.unique(db_test_res):
    print(f"cluster: {k}")
    # cluster가 k인 이미지 10개
    idx = np.where(db_test_res==k)[0][:10]
    print(f"{k}-cluster: {idx}")
    
    f = plt.figure(figsize=(8, 2))
    for i in range(6): # idx로 하지 않는 이유는, 밑에 subplot 위치 지정하기 위해.
        image = X_image[idx[i]].reshape(28, 28) # reshape to show image
        ax = f.add_subplot(1, 10, i+1) # range(10), subplot.
        ax.imshow(image, cmap=plt.cm.bone)
        ax.grid(False)
        ax.set_title(k)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        plt.tight_layout()



# check image
f = plt.figure(figsize=(8, 2))
for k in np.unique(db_test):
    print(f"cluster: {k}")
    # cluster가 k인 이미지 10개
    idx = np.where(db_test==k)[0][:10]
    print(f"{k}-cluster: {idx}")
    
    f = plt.figure(figsize=(8, 2))
    for i in range(10): # idx로 하지 않는 이유는, 밑에 subplot 위치 지정하기 위해.
        image = X_image[idx[i]].reshape(28, 28) # reshape to show image
        ax = f.add_subplot(1, 10, i+1) # range(10), subplot.
        ax.imshow(image, cmap=plt.cm.bone)
        ax.grid(False)
        ax.set_title(k)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        plt.tight_layout()
        
DBSCAN?
