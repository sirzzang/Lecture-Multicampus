# -*- coding: utf-8 -*-
"""credit-fraud-AE vs. iForest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NYsJHvB3TeMbodszRXJDUMYCklrhmbMu
"""

# module import
import pandas as pd
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.callbacks import EarlyStopping #, ModelCheckpoint
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf
from sklearn.ensemble import IsolationForest
# from sklearn.metrics.pairwise import cosine_distances

# 경로 설정
root_path = "/content/drive/My Drive/멀티캠퍼스/[혁신성장] 인공지능 자연어처리 기반/[강의]/조성현 강사님"
data_path = f"{root_path}/dataset"

# 데이터 로드
credit = pd.read_csv(f"{data_path}/creditcard_fraud.csv")

########## ======== 원본 데이터 보존 ======== ################ 
# 피쳐 선택: Time 제외 모두 사용
X_data = credit.iloc[:, 1:-1]
# y_train = credit.iloc[:, -1]

# 표준화
scaler = StandardScaler()
scaler.fit(X_data)
X_train = scaler.transform(X_data)
X_train
print(X_train)
# print(y_train)

########## ======== 오토인코더 모델 구성 ======== ################ 
X_train_AE = X_train.copy()

# 파라미터 설정
n_input = X_train_AE.shape[1]
n_output = n_input

# 모델 레이어 설정
x_Input = Input(batch_shape=(None, n_input))
x_Encoder1 = Dense(256, activation='relu')(x_Input)
x_Encoder1 = Dropout(0.3)(x_Encoder1)
x_Encoder2 = Dense(512, activation='relu')(x_Encoder1)
x_Encoder2 = Dropout(0.2)(x_Encoder2)
y_Decoder1 = Dense(256, activation='relu')(x_Encoder2)
y_Decoder1 = Dropout(0.3)(y_Decoder1)
y_Decoder2 = Dense(n_output, activation='linear')(y_Decoder1)

# 모델 구조 설정
model = Model(x_Input, y_Decoder2)
model.compile(loss='mse', optimizer=Adam(lr=0.001))
print("====== 모델 전체 구조 ======")
print(model.summary())

# 모델 학습 파라미터, 체크포인트
# EPOCHS = int(input('학습 횟수 설정: '))
# BATCH = int(input('배치 사이즈 설정: '))
EPOCHS = 500
BATCH = 500
es = EarlyStopping(monitor='loss', patience=5, verbose=1)

# 훈련
hist = model.fit(X_train_AE, X_train_AE,
                 epochs=EPOCHS,
                 batch_size=BATCH,
                 callbacks=[es],
                 shuffle=True)

# plot loss
plt.plot(hist.history['loss'], label='Train Loss')
plt.title('Loss Trajectory_AutoEncoder')
plt.legend()
plt.show()

# 예측
y_pred_AE = model.predict(X_train_AE)
y_pred_AE

# 거리 계산: 불확실!!
def calc_distance(origin, pred):
    dist = []
    for i in range(len(pred)):
        dist.append(np.sqrt(np.sum((np.square(origin[i]-pred[i])))))
    dist = np.array(dist)
    return pd.Series(dist)

# %%time
distance_AE = calc_distance(X_train_AE, y_pred_AE)

# 원래 데이터에 넣기
credit['distance_AE'] = distance_AE
display(credit)


########## ======== isolationForest 모델 구성 ======== ################ 

# 데이터 준비 
X_train_IF = X_train.copy()
y_train_IF = y_train.copy()
print(X_train_IF)
print(y_train_IF)

# iForest 학습
model = IsolationForest(n_estimators=200, verbose=1)
model.fit(X_train_IF)

# 이상치 점수 by 거리
score = abs(model.score_samples(X_train_IF))

# 이상치 점수 시각화
plt.hist(score, bins=50)
plt.show()

# 이상치 점수 기준: 0.7
y_pred_IF = (score > 0.7).astype(int)
print(y_pred_IF)

# iForest 라벨 원래 데이터에 넣기
credit['Class_iForest'] = pd.Series(y_pred_IF)
display(credit)

########## ======== 3) 결과 비교 ======== ################ 

# AE 거리 순 정렬
df = credit.sort_values(by='distance_AE', ascending=False)
display(df)

# 각 라벨 확인 원래 몇 개 있는지 확인
print(df['Class'].value_counts()) # original label 이상치 : 492
print(df['Class_iForest'].value_counts()) # iForest label 이상치 : 207

# AE로 계산한 거리 상위 n개 중 이상치 몇 개 있는지 반환
def count_abnormal(data, threshold, num=30):
    for i in range(threshold//num):
        print(f"<< 상위 {(i+1)*num}개에서 이상치 체크 >> ")
        print("  ====== AutoEncoder vs. Original Label ======")
        print(data['Class'][:(i+1)*num].value_counts())        
        print("  ====== AutoEncoder vs. iForest Label ======")
        print(data['Class_iForest'][:(i+1)*num].value_counts())
        print(" ")

# 원래 이상치 데이터 492개이므로 AE 기준 거리 상위 600개 데이터 정도 까지만 비교
count_abnormal(df, 600)