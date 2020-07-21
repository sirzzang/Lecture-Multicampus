# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:14:28 2020

@author: sir95
"""

# module import
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import time
import numpy as np

# mnist 데이터셋 다운로드 후 저장: 강사님이 미리 진행
with open('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/mnist.pickle', 'rb') as f:
    mnist = pickle.load(f)

# check data
dir(mnist)
sample_img = mnist['data'][0]
sample_img # 0 ~ 784까지 픽셀 강도
sample_img = sample_img.reshape(28, 28) # 
plt.imshow(sample_img, cmap='Greys')

# use only first 10000 data
X = mnist.data[:10000]
y = mnist.target[:10000]

# split train, test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
knn_clf = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn_clf.fit(X_train, y_train)

# calculate test set accuracy
start_time = time.time() # to check elapsed time
test_acc = knn_clf.score(X_test, y_test) # 내장함수 활용
elapsed_time = time.time()-start_time
print("Elapsed Time: {}".format(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))
print("Test Set Accuracy: %.2f" % test_acc)


# control num of neighbors
test_acc_list = []
for i in range(1, 21):
    knn_model = KNeighborsClassifier(n_neighbors=i, p=2, metric='minkowski')
    start_time = time.time() # to check elapsed time
    
    # train and calculate test accuracy
    knn_model.fit(X_train, y_train)
    test_acc = knn_model.score(X_test, y_test)
    print(i, "neighbors, Elapsed Time: {}".format(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))    
    print(i, "neighbors, Test Set Accuracy: %.2f" % test_acc)
    test_acc_list.append(test_acc)
    
# plot accuracies
iter_ranges = np.linspace(1, 20, num=20)
plt.plot(iter_ranges, test_acc_list, label='Test Accs')
plt.xlabel("num. of neighbors")
plt.ylabel("accuracy")
plt.legend(loc="upper right")
plt.show()

