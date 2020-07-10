# LSTM Autoencoder를 이용한 차원 축소 예시
# 
# 20-기간, 8개 feature data를 20-기간 3개 feature data로 변환한다.
# shape = (None, 20, 8)
# t1  Open  High  Low  Close  ShortMA  LongMA  MACD  RSI
# t2   .     .     .     .       .        .      .    .
# t3   .     .     .     .       .        .      .    .
# ..
# t20  .     .     .     .       .        .      .    .
#
# Autoencoder를 통해 위의 데이터를 아래 형태로 변환한다 (차원 축소)
# shape = (None, 20, 3)
# t1  feat_1   feat_2   feat_3
# t2    .        .        .
# t3    .        .        .
# ..
# t20   .        .        .
#
# feature 개수가 많지 않아 축소하는 것이 큰 의미는 없다. Autoencoder의 동작 원리를 연습하기 위한 것이다.
#
# 2020.03.31, 아마추어퀀트 (조성현)
# --------------------------------------------------------------------------------------------------
from tensorflow.keras.layers import Dense, Input, LSTM
from tensorflow.keras.layers import Bidirectional, TimeDistributed
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from MyUtil import TaFeatureSet
import pickle

nInput = 3
nStep = 20
nHidden = 3         # 8개 feature를 3개로 줄인다.
MASHORT = 10        # 종가의 단기 이동평균
MALONG = 40         # 종가의 장기 이동평균

# Batch data를 생성한다. (7-6.CNN(2d_stock).py와 행/열이 바뀌어 있다.)
def createTrainData(xData, step=nStep):
    nFeature = xData.shape[1]
    m = np.arange(xData.shape[0] + 1)
    
    x = []
    y = []
    for i in m[0:(-step-5)]:
        a = xData[i:(i+step), :]
        x.append(a)
    
    # LSTM에 사용하기 위해 3차원 구조로 변환한다. (batch, time-step, feature)
    xBatch = np.reshape(np.array(x), (len(m[0:(-step-5)]), step, nFeature))
    
    # 5일후 이동평균을 예측한다
    for i in m[0:(-step-5)]:
        a = xData[i + step + 5 - 1, 4]
        y.append(a)
    yBatch = np.reshape(np.array(y), (len(m[0:(-step-5)]), 1))
    
    return xBatch, yBatch

# Normalize OHLC price
def normalizeOHLC(ohlc):
    m = np.mean(ohlc.mean())
    scale = np.mean(ohlc.std())
    
    rdf = pd.DataFrame((ohlc['open'] - m) / scale)
    rdf['high'] = (ohlc['high'] - m) / scale
    rdf['low'] = (ohlc['low'] - m) / scale
    rdf['close'] = (ohlc['close'] - m) / scale
    return rdf
    
# 주가 데이터
df = pd.read_csv('StockData/069500.csv', index_col=0, parse_dates=True)[::-1]
df = df.drop('volume', 1)

# Normalize OHLC
ndf = normalizeOHLC(df)

ndf['maShort'] = pd.DataFrame(df['close']).rolling(window=MASHORT).mean()
ndf['maLong'] = pd.DataFrame(df['close']).rolling(window=MALONG).mean()
ndf['macd'] = TaFeatureSet.MACD(df)
ndf['rsi'] = TaFeatureSet.RSI(df)
ndf = ndf.dropna()

# Normalize other features
ndf['maShort'] = (ndf['maShort'] - ndf['maShort'].mean()) / ndf['maShort'].std()
ndf['maLong'] = (ndf['maLong'] - ndf['maLong'].mean()) / ndf['maLong'].std()
ndf['macd'] = (ndf['macd'] - ndf['macd'].mean()) / ndf['macd'].std()
ndf['rsi'] = (ndf['rsi'] - ndf['rsi'].mean()) / ndf['rsi'].std()

# 학습 데이터 생성
data = np.array(ndf)
x, y = createTrainData(data, nStep)

# LSTM AutoEncoder.
# -----------------
xInput = Input(batch_shape=(None, x.shape[1], x.shape[2]))

# encoder
eLstm = Bidirectional(LSTM(nHidden, return_sequences=True), merge_mode = 'sum')(xInput)

# decoder
dLstm = Bidirectional(LSTM(nHidden, return_sequences=True), merge_mode = 'sum')(eLstm)
xOutput = TimeDistributed(Dense(x.shape[2]))(dLstm)
#xOutput = Dense(x.shape[2])(dLstm)

model = Model(xInput, xOutput)
model.compile(loss='mse', optimizer=Adam(lr=0.001))
encoder = Model(xInput, eLstm)

# AE를 학습한다.
h = model.fit(x, x, epochs = 300, batch_size=300, shuffle=True)

# loss trajectory를 확인한다.
plt.plot(h.history['loss'], label='Train loss')
plt.title('Loss trajectory')
plt.show()

# 학습데이터의 차원을 줄인다. shape = (None, 20, 8) --> (None, 20, 3)으로 축소됐다.
trainXE = encoder.predict(x)

# 결과를 저장한다.
with open('dataset/8-4.trainAE.pickle', 'wb') as f:
    pickle.dump([ndf, trainXE, y], f, pickle.HIGHEST_PROTOCOL)
