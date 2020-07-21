# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:13:13 2020

@author: sir95
"""

# module import
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# make data set
X_data, y_data = make_blobs(n_samples=200,
                            n_features=2,
                            centers=4,
                            cluster_std=0.5,
                            shuffle=True,
                            random_state=42)

# find optimal cluster num. using Elbow method
distortions = []
for c_num in range(2, 13):
    km = KMeans(n_clusters=c_num, 
                init='random',
                n_init=100,
                max_iter=3000,
                tol=1e-4,
                random_state=42,
                verbose=1)
    km = km.fit(X_data)
    distortions.append(km.inertia_)

# plot distortions
plt.plot(range(2, 13), distortions, marker='^')
plt.xlabel('Num. of Clusters')
plt.ylabel('Distortions(SSE)')
plt.title('Finding the Optimal Num. of Clusters', fontdict={'fontsize':18})
plt.show()

# plot optimal clusters
km_opt = KMeans(n_clusters=4, init='random', n_init=100, max_iter=300, tol=1e-4, random_state=42)
km_opt = km_opt.fit(X_data)
y_km_opt = km_opt.predict(X_data)
plt.figure(figsize=(8,5))
plt.scatter(X_data[y_km_opt==0,0], X_data[y_km_opt==0,1], s=100, c='green', marker='s', alpha=0.5, label='cluster1')
plt.scatter(X_data[y_km_opt==1,0], X_data[y_km_opt==1,1], s=100, c='orange', marker='o', alpha=0.5, label='cluster2')
plt.scatter(X_data[y_km_opt==2,0], X_data[y_km_opt==2,1], s=100, c='blue', marker='v', alpha=0.5, label='cluster3')
plt.scatter(X_data[y_km_opt==3,0], X_data[y_km_opt==3,1], s=100, c='black', marker='v', alpha=0.5, label='cluster4')
plt.scatter(km_opt.cluster_centers_[:, 0], km_opt.cluster_centers_[:, 1], s=250, marker='+', c='red', label='Centeroids')
plt.legend()
plt.grid()
plt.show()
