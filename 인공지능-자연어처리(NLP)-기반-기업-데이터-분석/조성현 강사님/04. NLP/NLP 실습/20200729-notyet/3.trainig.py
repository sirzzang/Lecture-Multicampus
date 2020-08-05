# 지역별 '건강보조식품 소매업' 매출 데이터를 학습한다
# -------------------------------------------------
from tensorflow.keras.layers import Dense, Input, LSTM, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt
import pickle

# pre-trining용 데이터를 읽어온다.
with open('dataset/2.pre_train_data.pickle', 'rb') as f:
    preData = pickle.load(f)

# 학습 데이터를 생성한다.
# 1년 데이터로 다음 데이터를 학습한다. (timestep = 12)
# 0 ~ 11 --> 12
# 1 ~ 12 --> 13
# 2 ~ 13 --> 14
x = preData[:, 0:12]
x = np.vstack([x, preData[:, 1:13]])
x = np.vstack([x, preData[:, 1:13]])
x = x[:, :, np.newaxis]

y = preData[:, 12]
y = np.hstack([y, preData[:, 13]])
y = np.hstack([y, preData[:, 14]])
y = y[:, np.newaxis]

nInput = 1
nOutput = 1
nStep = 12
nHidden = 50

# LSTM 모델을 생성한다.
xInput = Input(batch_shape=(None, nStep, 1))
xLstm = LSTM(nHidden, dropout=0.5)(xInput)
xOutput = Dense(nOutput)(xLstm)
xOutput = Dropout(0.5)(xOutput)
model = Model(xInput, xOutput)
model.compile(loss='mse', optimizer=Adam(lr=0.0005))

# Pre-training
h = model.fit(x, y, epochs=500, batch_size=512, shuffle=True)

# Loss history를 그린다
plt.figure(figsize=(8, 3))
plt.plot(h.history['loss'], color='red')
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 본 데이터를 읽어서 최종 학습한다 (fine-tuning)
with open('dataset/1.data.pickle', 'rb') as f:
    _, _, _, realData = pickle.load(f)
np.random.shuffle(realData)

x = realData[:, 0:12]
x = np.vstack([x, realData[:, 1:13]])
x = np.vstack([x, realData[:, 1:13]])
x = x[:, :, np.newaxis]

y = realData[:, 12]
y = np.hstack([y, realData[:, 13]])
y = np.hstack([y, realData[:, 14]])
y = y[:, np.newaxis]

# Fine-tunning
h = model.fit(x, y, epochs=300, batch_size=16, shuffle=True)

# Loss history를 그린다
plt.figure(figsize=(8, 3))
plt.plot(h.history['loss'], color='red')
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# save model
model.save('dataset/3.model.h5')


