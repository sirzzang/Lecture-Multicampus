# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:18:31 2020

@author: sir95
"""

# module import
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN


# plot raw data
X, y = make_moons(n_samples=200, noise=0.05, random_state=42)
print(f"X: {X.shape}, example: {X[:3]}")
print(f"y: {y.shape}, example: {y[:3]}")
plt.scatter(X[:, 0], X[:, 1]) # 2d scatter
plt.tight_layout()
plt.show()

# KMeans, HCluster
def clusterDistanceBased(num_of_clusters, data):    
    km = KMeans(n_clusters=num_of_clusters, random_state=42) # kmeans
    km_pred = km.fit_predict(data)
    ac = AgglomerativeClustering(n_clusters=num_of_clusters) # hcluster
    ac_pred = ac.fit_predict(data)
    return km_pred, ac_pred

def clusterDBSCAN(eps, min_samples, data):
    db = DBSCAN(eps=eps, min_samples=min_samples) # DBSCAN
    db_pred = db.fit_predict(data)
    return db_pred


# get cluster results
y_km, y_ac = clusterDistanceBased(2, X)
y_db = clusterDBSCAN(0.2, 5, X)


# plot: kmeans, hcluster
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
ax1.scatter(X[y_km==0, 0], X[y_km==0, 1],
            edgecolor='black', c='lightblue', marker='o', s=40, label='KMeans_C1')
ax1.scatter(X[y_km==1, 0], X[y_km==1, 1],
            edgecolor='black', c='red', marker='s', s=40, label='KMeans_C2')
ax1.legend()
ax2.scatter(X[y_ac==0, 0], X[y_ac==0, 1],
            edgecolor='black', c='lightblue', marker='o', s=40, label='Agglomerative_C1')
ax2.scatter(X[y_ac==1, 0], X[y_ac==1, 1],
            edgecolor='black', c='red', marker='s', s=40, label='Agglomerative_C2')
ax1.set_title('K-means Clustering')
ax2.set_title('Agglomerative Clustering')
ax2.legend()
plt.tight_layout()
plt.show()

# plot: dbscan
plt.scatter(X[y_db==0, 0], X[y_db==0, 1],
            edgecolor='black', c='lightblue', marker='o', s=40, label='DBSCAN_C1')
plt.scatter(X[y_db==1, 0], X[y_db==1, 1],
            edgecolor='black', c='red', marker='s', s=40, label='DBSCAN_C2')
plt.title('DBSCAN Clustering')
plt.legend()
plt.show()