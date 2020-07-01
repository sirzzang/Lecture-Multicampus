# Unsupervised Learning 예시 (단층 신경망)
# Self Origanized Map (SOM)에 의한 Clustering 예제 : Mnist clustering
#
# 2020.5.25, 아마추어퀀트 (조성현)
# -------------------------------------------------------------------

# CPU에서 작업한다. 이 경우는 GPU global memory로 데이터를 자주 보내기
# 때문에 GPU로 작업하는 것이 효율적이지 못하다.
# import os
# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import KernelPCA
import pickle

# 저장된 mnist 데이터를 읽어온다.
with open('dataset/mnist.pickle', 'rb') as f:
        mnist = pickle.load(f)

# Winner neuron을 찾는다.
# 방법 1 : w를 normalization한 후 output이 가장 큰 뉴런을 찾는다.
# 방법 2 : input x와 w와의 거리가 가장 짧은 뉴런을 찾는다. <-- 이 방법을 적용함.
#          K-Means의 중점과의 거리 계산과 유사한 개념임.
def findWinner(w, x):
    distance = tf.sqrt(tf.reduce_sum(tf.square(tf.subtract(w, tf.transpose(x))), 1))
    winner = tf.argmin(distance, axis=0)
    return tf.slice(distance, [winner], [1]), winner

# Winner neuron의 W를 업데이트한다 (Hebbian learning)
# Hebb's rule : W = W + alpha * (a - W)
def updateWeights(w, winner, x):
    subW = tf.gather(w, winner)
    updW = tf.add(subW, tf.multiply(ALPHA, tf.subtract(tf.transpose(x), subW)))
    newW = tf.tensor_scatter_nd_update(w, [[winner]], updW)
    return newW

# Winner-takes-all
# Winner neuron의 출력값만 '1'로 설정하고 나머지 neuron의 출력값은 '0'으로 설정한다.
# K-Means의 중점 할당 (assignment)과 유사한 개념임.
def winner_take_all(w, x, n):
    _, winner = findWinner(w, x)
    r = tf.one_hot(winner, n)
    return r, tf.argmax(r, 0)

# input data를 생성한다
inputX = mnist.data[:3000, :]
imageX = inputX.copy()
inputY = mnist.target[:3000]    # 나중에 확인용 사용

# Z-score nomalization.
# 그냥하면 세로 방향으로 표준화한다. 가로 방향으로 표준화하기 위해 transpose 후
# 표준화하고, 결과를 다시 transpose 했다.
sc = StandardScaler()
inputX = sc.fit_transform(inputX.T).T

# Kernel PCA로 차원을 줄인다
pca = KernelPCA(n_components = 100, kernel='rbf')
inputX = pca.fit_transform(inputX)

inputX = inputX.astype(np.float32).T
nInput = inputX.shape[0]
nOutput = np.unique(inputY).shape[0]
ALPHA = 0.05
loadWeights = False

# 그래프를 생성한다
if loadWeights:
    with open('dataset/comp_weights1.pickle', 'rb') as f:
        Wh = pickle.load(f)
    n_neighbor = 0   # neiborhood 없음
else:
    Wo = tf.Variable(tf.random.uniform([nOutput, nInput],0.0, 1.0), dtype=tf.float32)
    n_neighbor = nOutput - 1   # neiborhood

# 이미지 한 개씩 입력하면서 반복 학습한다.
n = inputX.shape[1]
for i in range(50):
    err = 0
    for k in range(n):
        dx = inputX[:, k].reshape([nInput, 1])
        
        # Winner neuron을 찾는다.
        distIW, winO = findWinner(Wo, dx)

        # Winner neuron의 W를 업데이트한다 (Hebb's Rule)
        winnerMin = np.max([0, winO.numpy() - n_neighbor])
        winnerMax = np.min([nOutput - 1, winO.numpy() + n_neighbor])

#        print(i, k, 'winner=', winO.numpy(), 'neighbor=', n_neighbor, winnerMin, winnerMax)
        for m in range(winnerMin, winnerMax+1):
            Wo = updateWeights(Wo, m, dx)
            
        # Error를 측정한다. Unsupervised Learning에서는 desired output이 없기 때문에
        # error라는 개념은 없지만, 각 중점에 할당된 데이터까지 거리의 합을 error로 정의할 수 있다.
        err += distIW.numpy()[0]

    # 이웃의 범위를 하나씩 좁혀 나간다.
    n_neighbor = np.max([0, n_neighbor - 1])
            
    print("%d done. error = %.8f, , neighborhood = %d" % (i+1, err / n, n_neighbor))

# Wo, Wh를 저장해 둔다.
with open('dataset/comp_weights1.pickle', 'wb') as f:
    pickle.dump(Wo, f, pickle.HIGHEST_PROTOCOL)
    
# 학습이 완료되었으므로, 이미지 한 개씩 입력하면서 clust를 결정한다.
clust = []
for k in range(n):
    dx = inputX[:, k].reshape([nInput, 1])
    
    # Winner-takes-all
    _, winOut = winner_take_all(Wo, dx, nOutput)

    clust.append(winOut.numpy())

# cluster 별로 이미지를 확인한다.
f = plt.figure(figsize=(8, 2))
for k in np.unique(clust):
    # cluster가 i인 imageX image 10개를 찾는다.
    idx = np.where(clust == k)[0][:10]
    
    f = plt.figure(figsize=(8, 2))
    for i in range(10):
        image = imageX[idx[i]].reshape(28,28)
        ax = f.add_subplot(1, 10, i + 1)
        ax.imshow(image, cmap=plt.cm.bone)
        ax.grid(False)
        ax.set_title(k)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        plt.tight_layout()
