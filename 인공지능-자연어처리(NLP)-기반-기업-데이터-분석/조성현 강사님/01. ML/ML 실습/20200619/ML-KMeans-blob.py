# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:12:16 2020

@author: sir95
"""

# set path
import os
os.getcwd()
os.chdir('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/20200619')
os.getcwd()

# module import
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# make data set
X_data, y_data = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=42)

# plot data set : scatter
plt.figure(figsize=(8,5))
plt.scatter(X_data[:, 0], X_data[:, 1], marker='^', s=100, alpha=0.5)
plt.grid()
plt.show()

# cluster data using K-means algorithm
km = KMeans(n_clusters=3, init='random', n_init=100, max_iter=300, tol=1e-4, random_state=42, ver)
km = km.fit(X_data)
print(f"KMeans Model ==>\n{km}")
y_km = km.predict(X_data)
print(f"KMeans Result ==>\n{y_km}")
print(f"Centeroids: {km.cluster_centers_}")
print(f"km inertia: {km.inertia_}")


# plot clustered result

plt.figure(figsize=(8,5))
plt.scatter(X_data[y_km==0,0], X_data[y_km==0,1], s=100, c='green', marker='s', alpha=0.5, label='cluster1')
plt.scatter(X_data[y_km==1,0], X_data[y_km==1,1], s=100, c='orange', marker='o', alpha=0.5, label='cluster2')
plt.scatter(X_data[y_km==2,0], X_data[y_km==2,1], s=100, c='blue', marker='v', alpha=0.5, label='cluster3')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=250, marker='+', c='red', label='Centeroids')
plt.legend()
plt.grid()
plt.show()