# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:21:12 2020

@author: sir95
"""


# module import
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# load data
stock = pd.read_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/stockPattern.csv')

# prepare data
X = np.array(stock) # dataframe -> numpy array.
print(f"stock data: {X.shape}")

def plot_stock_clusters(num_of_clusters, data):
    print(f"Clustering into {num_of_clusters} groups, Start.")
    
    # cluster
    km = KMeans(n_clusters=num_of_clusters, init='k-means++', n_init=30, verbose=1, random_state=42)
    km = km.fit(X)
    y = km.predict(X)
    
    # plot
    fig = plt.figure(figsize=(10, 6))
    colors = 'bgrcmykw'
    centeroids = km.cluster_centers_
    
    for i in range(num_of_clusters):
        s = f"pattern {i}"
        p = fig.add_subplot(2, (num_of_clusters+1)//2, i+1) # 2행 k열로 구성
        p.plot(centeroids[i], 'b-o', markersize=3, color=colors[np.random.randint(0, 7)], linewidth=1.0)
        p.set_title(s)
        
    plt.tight_layout()
    plt.show()
    
    print(f"Clustering into {num_of_clusters} groups, Done.")
    return y, km.inertia_
    
# find optimal value: Elbow method 
distortions = []
for k in range(2, 13):
    y_km, inertia = plot_stock_clusters(k, X)
    distortions.append(inertia)

plt.plot(range(2, 13), distortions, marker='^')
plt.xlabel('Num. of Clusters')
plt.ylabel('Distortions(SSE)')
plt.title('Finding the Optimal Num. of Clusters', fontdict={'fontsize':18})
plt.show()

# optimal cluster
k_opt = 4
km_opt = KMeans(n_clusters=k_opt, init='k-means++', n_init=30, max_iter=300, random_state=42)
km_opt = km_opt.fit(X)
km_pred = km_opt.predict(X)
stock['cluster'] = km_pred

for c in km_pred:
    plt.figure(figsize=(6,6)) # plot base figure
    p = stock.loc[stock['cluster'] == c]
    p = p.sample(frac=1).reset_index(drop=True)
    print(p)
    for i in range(10):
        plt.plot(p.iloc[i][0:20])
    plt.title(f'Cluster-{c}')
    plt.show()