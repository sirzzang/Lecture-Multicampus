# TensorFlow를 이용하여 KNN (K-nearest neighbors) 알고리즘을 연습한다.
# 학습 데이터는 대출 심사용 credit data를 이용하고 binary classification으로 분류한다.
#
# 2020.03.27, 아마추어퀀트 (조성현)
# ---------------------------------------------------------------------------------
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Credit data set을 읽어온다
ds = pd.read_csv('dataset/3-4.credit_data.csv')

# data set을 행을 기준으로 랜덤하게 섞는다 (shuffling)
ds = ds.sample(frac=1).reset_index(drop=True)

# 학습용 데이터와 시험용 데이터로 나눈다. (8 : 2)
trainRate = 0.8
trainLen = int(len(ds) * trainRate)
trainX = np.array(ds.iloc[0:trainLen, 0:6])
trainY = np.array(ds.iloc[0:trainLen, -1])
trainY = trainY.reshape(trainLen, 1)

testX = np.array(ds.iloc[trainLen:, 0:6])
testY = np.array(ds.iloc[trainLen:, -1])
testY = testY.reshape(len(testY), 1)

# KNN 학습
accuracy = []       # K = [1,2,3..]에 따른 정확도를 기록할 list
yHatK = []          # 최적 K일 때 testX의 class를 추정한 list
optK = 0            # 최적 K
optAccuracy = 0.0   # 최적 K일 때의 정확도
minK = 10
maxK = 100          # K = minK ~ maxK 까지 변화시키면서 정확도를 측정한다
for k in range(minK, maxK+1):
    yHat = []
    for tx in testX:
        # testX를 하나씩 읽어가면서 k-개의 가까운 거리를 찾는다
        tx = tx.reshape(1, 6)
        
        # test point와 모든 x와의 거리를 측정한다 (Euclidean distance)
        distance = tf.sqrt(tf.reduce_sum(tf.square(tf.subtract(trainX, tx)), 1))
        
        # test point와 모든 x와의 거리중 거리가 짧은 K개의 class (trainY)를 찾는다.
        # 이 classes에서 다수결로 test point의 class를 판정한다.
        # ex : tf.gather(trainY, indices) = [1, 1, 0, 1, 0, 1, 1] --> class = 1로 판정한다.
        #      class 들의 평균 = 5/7 = 0.714 --> 0.5 보다 크므로 class = 1로 판정함.
        values, indices = tf.nn.top_k(tf.negative(distance), k=k, sorted=False)
        classMean = tf.reduce_mean(tf.cast(tf.gather(trainY, indices), tf.float32))

        yHat.append(classMean.numpy())
    
    # test data의 class를 추정한다.
    yHat = np.array(yHat)
    yHat = yHat.reshape(len(yHat), 1)
    testYhat = np.where(yHat > 0.5, 1, 0)
    
    # test data의 실제 class와 추정 class를 비교하여 정확도를 측정한다.
    accK = 100 * (testY == testYhat).sum() / len(testY)
    
    # 정확도가 가장 높은 최적 K, yHatK, optAccuracy를 기록해 둔다
    if accK > optAccuracy:
        yHatK = yHat.copy()
        optK = k
        optAccuracy = accK
    
    # K에 따라 달라지는 정확도를 추적하기위해 history를 기록해 둔다
    accuracy.append(accK)
    print("k = %d done" % k)

# 결과를 확인한다
fig = plt.figure(figsize=(10, 4))
p1 = fig.add_subplot(1,2,1)
p2 = fig.add_subplot(1,2,2)

xK = np.arange(minK, maxK+1)
p1.plot(xK, accuracy)
p1.set_title("Accuracy (optimal K = " + str(optK) + ")")
p1.set_xlabel("K")
p1.set_ylabel("accuracy")
n, bins, patches = p2.hist(yHatK, 50, facecolor='blue', alpha=0.5)
p2.set_title("yHat distribution")
plt.show()

print("\nAccuracy = %.2f %s" % (optAccuracy, '%'))

# 2개 Feature를 선택하여 2-차원 상에서 각 Feature에 대한 class를 육안으로 확인한다.
# 전체 Feature의 6-차원 공간의 확인은 불가하므로 2-차원으로 확인한다.
dsX = 0     # x-축은 첫 번째 feature
dsY = 1     # y-축은 두 번째 feature
cnt = 300   # 300개만 그린다
class0 = ds[ds['class'] == 0].iloc[0:cnt, [dsX, dsY]]
colX = class0.columns[0]
colY = class0.columns[1]

plt.figure(figsize=(8, 7))
plt.scatter(class0[colX], class0[colY], color='blue', marker='o', s=50, alpha=0.5, label='class=0')

class1 = ds[ds['class'] == 1].iloc[0:cnt, [dsX, dsY]]
plt.scatter(class1[colX], class1[colY], color='red', marker='x', s=50, alpha=0.7, label='class=1')

plt.xlabel(colX)
plt.ylabel(colY)
plt.legend()
plt.show()
