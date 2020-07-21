# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:46:20 2020

@author: sir95
"""

# module import
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_samples
from matplotlib import cm

# classify into clusters and compare
for n_c in range(2, 5):
    # make dataset
    X_data, y_data = make_blobs(n_samples=150, n_features=2, centers=n_c, cluster_std=0.5, shuffle=True, random_state=42)
    
    # model
    km = KMeans(n_clusters=n_c, init='random', n_init=100, max_iter=300, tol=1e-4, random_state=42)
    km = km.fit(X_data)
    y_km = km.predict(X_data)

    # plot clusters
    plt.figure(figsize=(8, 5))
    plt.scatter(X_data[y_km == 0,0], X_data[y_km == 0,1], s=100, c='green', marker='s', alpha=0.5, label='C-1')
    plt.scatter(X_data[y_km == 1,0], X_data[y_km == 1,1], s=100, c='orange', marker='o', alpha=0.5, label='C-2')
    plt.scatter(X_data[y_km == 2,0], X_data[y_km == 2,1], s=100, c='blue', marker='^', alpha=0.5, label='C-3')
    plt.scatter(X_data[y_km == 3,0], X_data[y_km == 3,1], s=100, c='black', marker='>', alpha=0.5, label='C-3')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=250, marker='+', c='red', label='Centeroids')
    plt.legend()
    plt.grid()
    plt.show()

    # Silhouette 
    cluster_labels = np.unique(y_km)
    print(f"labels: {cluster_labels}")
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X_data, y_km, metric='euclidean')
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_km == c] # code?
        c_silhouette_vals.sort() # code?
        y_ax_upper += len(c_silhouette_vals) # code?
        color = cm.jet(float(i) / n_clusters) # code?
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouette_vals, height=1.0, edgecolor='none', color=color) # code?
        yticks.append((y_ax_lower + y_ax_upper) / 2.0) # ?
        y_ax_lower += len(c_silhouette_vals) # ?
        
    silhouette_avg = np.mean(silhouette_vals) # ? 
    
    plt.axvline(silhouette_avg, color='red', linestyle='--')
    plt.yticks(yticks, cluster_labels + 1) # ?
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette Coef.')
    plt.tight_layout() # ?
    plt.show()

    
    