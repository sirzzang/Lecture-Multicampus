# Pre-training용 데이터를 생성한다.
# GAN을 이용하여 지역별 '건강보조식품 소매업' 매출 데이터를 생성한다.
# ----------------------------------------------------------------
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import backend as K
import numpy as np
import matplotlib.pyplot as plt
import pickle

# 데이터를 읽어온다.
with open('dataset/1.data.pickle', 'rb') as f:
    _, _, _, realData = pickle.load(f)
np.random.shuffle(realData)

nDInput = realData.shape[1]
nDHidden = 256
nDOutput = 1
nGInput = 32
nGHidden = 256
nGOutput = nDInput
      
def getNoise(m, n=nGInput):
    z = np.random.uniform(-1., 1., size=[m, n])
    return z

def MyOptimizer(a = 0.0005):
    return RMSprop(lr = a)

# Discriminator를 생성한다
def BuildDiscriminator():
    x = Input(batch_shape = (None, nDInput))
    h = Dense(nDHidden, activation = 'relu')(x)
    h = Dropout(0.5)(h)
    Dx = Dense(nDOutput, activation = 'sigmoid')(h)
    model = Model(x, Dx)
    model.compile(loss = 'binary_crossentropy', optimizer = MyOptimizer(0.001))
    return model

# Generator를 생성한다
def BuildGenerator():
    z = Input(batch_shape = (None, nGInput))
    h = Dense(nGHidden, activation = 'relu')(z)
    h = Dropout(0.5)(h)
    Gz = Dense(nGOutput)(h)
    
    model = Model(z, Gz)
    return model

# Generator --> Discriminator를 연결한 모델을 생성한다.
# 아래 네트워크로 z가 들어가면 DGz = 1이 나오도록 G를 학습한다.
# D 네트워크는 업데이트하지 않고, G 네트워크만 업데이트한다.
#
#        +---+   Gz   +---+
#  z --->| G |------->| D |---> DGz
#        +---+        +---+
#      trainable   not trainable
# ----------------------------------------------------------
def BuildGAN(D, G):
    z = Input(batch_shape=(None, nGInput))
    Gz = G(z)
    DGz = D(Gz)
    D.trainable = False     # Discriminator는 업데이트하지 않는다.
    
    model = Model(z, DGz)
    model.compile(loss = 'binary_crossentropy', optimizer = MyOptimizer(0.0005))
    return model

K.clear_session()
Discriminator = BuildDiscriminator()
Generator = BuildGenerator()
GAN = BuildGAN(Discriminator, Generator)

nBatchCnt = 6       # Mini-batch를 위해 input 데이터를 n개 블록으로 나눈다.
nBatchSize = int(realData.shape[0] / nBatchCnt)  # 블록 당 Size
for epoch in range(1000):
    # Mini-batch 방식으로 학습한다
    for n in range(nBatchCnt):
        # input 데이터를 Mini-batch 크기에 맞게 자른다
        nFrom = n * nBatchSize
        nTo = n * nBatchSize + nBatchSize
        
        # 마지막 루프이면 nTo는 input 데이터의 끝까지.
        if n == nBatchCnt - 1:
            nTo = realData.shape[0]
               
        # 학습 데이터를 준비한다
        bx = realData[nFrom : nTo]
        bz = getNoise(m=bx.shape[0], n=nGInput)
        Gz = Generator.predict(bz)

        # Discriminator를 학습한다.
        # Real data가 들어가면 Discriminator의 출력이 '1'이 나오도록 학습하고,
        # Fake data (Gz)가 들어가면 Discriminator의 출력이 '0'이 나오도록 학습한다.
        target = np.zeros(bx.shape[0] * 2)
        target[ : bx.shape[0]] = 0.9     # '1' 대신 0.9로 함
        target[bx.shape[0] : ] = 0.1     # '0' 대신 0.1로 함
        bx_Gz = np.concatenate([bx, Gz])
        Dloss = Discriminator.train_on_batch(bx_Gz, target)
        
        # Generator를 학습한다.
        # Fake data (z --> Gz --> DGz)가 들어가도 Discriminator의 출력이 '1'이
        # 나오도록 Generator를 학습한다.
        target = np.zeros(bx.shape[0])
        target[:] = 0.9
        Gloss = GAN.train_on_batch(bz, target)
        
    if epoch % 10 == 0:
        z = getNoise(m=realData.shape[0], n=nGInput)
        fakeData = Generator.predict(z)
        print("epoch = %d, D-Loss = %.3f, G-Loss = %.3f" % (epoch, Dloss, Gloss))
    
# real data 분포 (p)와 fake data 분포 (q)를 그려본다
z = getNoise(m=realData.shape[0], n=nGInput)
fakeData = Generator.predict(z)

# fakeData를 육안으로 확인한다.
plt.figure(figsize=(12, 8))
plt.plot(fakeData.T)   
plt.show()

# pre-training용 데이터를 생성하고, 저장한다. (325 * 50 개)
z = getNoise(m=realData.shape[0] * 50, n=nGInput)
fakeData = Generator.predict(z)

with open('dataset/2.pre_train_data.pickle', 'wb') as f:
    pickle.dump(fakeData, f, pickle.HIGHEST_PROTOCOL)



