# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:19:42 2020

@author: sir95
"""

# module import
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import numpy as np

# make dataset
X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=42)

# plot data
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], marker='o', s=100, alpha=0.5)
plt.grid()
plt.show()

# calculate linkage
mergings = linkage(X, method='complete')

# plot dendrogram
plt.figure(figsize=(10, 10))
dendrogram(mergings)
plt.show()

# show cluster results
y_cluster = fcluster(Z=mergings, t=3, criterion='distance')

# centeroid X, y
c1 = np.mean(X[y_cluster == 1], axis=0)
c2 = np.mean(X[y_cluster == 2], axis=0)
c3 = np.mean(X[y_cluster == 3], axis=0)
center = np.vstack([c1, c2, c3])

# plot
plt.figure(figsize=(8, 6))
plt.scatter(X[y_cluster == 1,0], X[y_cluster == 1,1], s=100, c='green', marker='s', alpha=0.5, label='C1')
plt.scatter(X[y_cluster == 2,0], X[y_cluster == 2,1], s=100, c='orange', marker='s', alpha=0.5, label='C2')
plt.scatter(X[y_cluster == 3,0], X[y_cluster == 3,1], s=100, c='blue', marker='s', alpha=0.5, label='C3')
plt.scatter(center[:, 0], center[:, 1], s=250, marker='+', c='red', label='Centeroids')
plt.legend()
plt.grid()
plt.show()