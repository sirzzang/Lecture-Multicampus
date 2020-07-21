# 차원 축소 LSTM 예시 : KODEX200 주가 (2010 ~ 현재)를 예측해 본다.
# KODEX200의 종가와, 10일, 40일 이동평균을 이용하여 향후 5일 동안의 평균 종가를 예측해 본다.
# 과거 20일 (step = 20) 종가, 이동평균 패턴을 학습하여 예측한다.
# 차원을 축소하지 않았을 때의 결과와 비교해 보면 어떠한가? 다르다면 왜 그런가?
#
# 2020.03.30, 아마추어퀀트 (조성현)
# ---------------------------------------------------------------------------------------
from tensorflow.keras.layers import Dense, Input, LSTM
from tensorflow.keras.layers import Bidirectional, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt
import pickle

nInput = 3
nOutput = 1
nStep = 20
nHidden = 64

# 저장된 학습 데이터 (원래 데이터 세트와 차원이 축소된 학습 데이터)를 읽어온다.
with open('dataset/8-4.trainAE.pickle', 'rb') as f:
    df, x, y = pickle.load(f)

# LSTM 모델을 생성한다.
xInput = Input(batch_shape=(None, nStep, nInput))
xLstm = Bidirectional(LSTM(nHidden), merge_mode='concat')(xInput)
xLstm = Dropout(0.1)(xLstm)
xOutput = Dense(64, activation = 'relu')(xLstm)
xOutput = Dropout(0.1)(xOutput)
xOutput = Dense(nOutput)(xOutput)
model = Model(xInput, xOutput)
model.compile(loss='mse', optimizer=Adam(lr=0.001))
model.summary()

# 학습한다
h = model.fit(x, y, epochs = 100, batch_size=300, shuffle=True)

# Loss history를 그린다
plt.figure(figsize=(8, 3))
plt.plot(h.history['loss'], color='red')
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# x의 마지막 값으로 다음 y 값을 예측한다. (5일후 주가의 이동평균 값을 예측함)
px = np.reshape(x[-1], (-1, nStep, nInput))
yHat = model.predict(px)[0][0]

# 원 시계열의 마지막 100개를 plot으로 그려본다.
# [3,4,5]는 ['close', 'maShort', 'maLong']을 의미한다.
lastData = np.array(df.iloc[-200:, [3,4,5]])

# 원 시계열과 예측된 시계열을 그린다
ax1 = np.arange(1, len(lastData) + 1)
ax2 = np.arange(len(lastData), len(lastData) + 5 + 1)
plt.figure(figsize=(10, 5))
plt.plot(ax1, lastData[:, 0], 'b-o', markersize=4, color='blue', label='Time series', linewidth=1)
plt.plot(ax1, lastData[:, 1], color='red', label='Short MA', linewidth=1)
plt.plot(ax1, lastData[:, 2], color='black', label='Long MA', linewidth=1)
plt.plot((200, 205), (lastData[-1:, 0], yHat), 'b-o', markersize=8, color='red', label='Estimate')
plt.axvline(x=ax1[-1],  linestyle='dashed', linewidth=1)
plt.legend()
plt.show()