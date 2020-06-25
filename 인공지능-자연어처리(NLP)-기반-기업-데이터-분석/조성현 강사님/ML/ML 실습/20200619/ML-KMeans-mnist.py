# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:27:40 2020

@author: sir95
"""

# module import 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

# PCA


pca = KernelPCA(n_components=50, kernel='rbf')
X_input = pca.fit_transform(X_input)

# KMeans clusterering, using kmeans++ initializer
km = KMeans(n_clusters=10, init='k-means++', n_init=3, max_iter=300, tol=1e-04, random_state=42, verbose=1)
km = km.fit(X_input)
cluster = km.predict(X_input)

# check image
f = plt.figure(figsize=(8, 2))
for k in np.unique(cluster):
    print(f"cluster: {k}")
    # cluster가 k인 이미지 10개
    idx = np.where(cluster==k)[0][:10]
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