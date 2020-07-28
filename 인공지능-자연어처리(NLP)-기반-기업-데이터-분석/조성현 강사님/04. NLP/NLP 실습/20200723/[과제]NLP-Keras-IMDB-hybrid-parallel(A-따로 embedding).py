# -*- coding: utf-8 -*-
"""[과제]NLP-Keras-IMDB-hybrid(A: Embedding 각각).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSDCXhnpRIa1cGWJB_dCgR0XGQiNXzmV
"""

# 모듈 불러오기
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Dropout, Flatten
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D # CNN
from tensorflow.keras.layers import Bidirectional, LSTM # LSTM
from tensorflow.keras.layers import Concatenate
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import sys

np.set_printoptions(threshold=sys.maxsize) # numpy array 출력 길이 증가

# 데이터 불러 오기
max_features = int(input('최대 단어 빈도 설정: '))
(X_train_raw, y_train), (X_test_raw, y_test) = imdb.load_data(num_words=max_features)

## 문장 길이 체크
# def check_len(m, sentences):
#     cnt = 0
#     for sent in sentences:
#         if len(sent) <= m:
#             cnt += 1
    
#     return f'전체 문장 중 길이가 {m} 이하인 샘플의 비율: {(cnt/len(sentences))*100}'

# for length in range(100, 1000, 50):
#     print(check_len(length, X_train_raw))
# print()

# 문장 길이 설정
max_length = int(input('문장 길이 설정: '))

# 모델 파라미터 설정
BATCH = int(input('배치 사이즈 설정: '))
n_embed = int(input('임베딩 차원 설정: '))
n_hidden = int(input('은닉 노드 수 설정: '))
EPOCHS = int(input('학습 횟수 설정: '))
n_filters = int(input('CNN 컨볼루션 필터 개수 설정: '))
s_filters = int(input('CNN 컨볼루션 커널 사이즈 설정: '))

# 패딩 진행
X_train = pad_sequences(X_train_raw, maxlen=max_length)
X_test = pad_sequences(X_test_raw, maxlen=max_length)
y_train = y_train.copy()
y_test = y_test.copy()
print("========== 패딩 후 ==========")
print(f"훈련 데이터: {X_train.shape}")
print(f"테스트 데이터: {X_test.shape}")

####### ========== 모델 네트워크 구성 ========== #######
# 1) 입력
X_Input = Input(batch_shape=(None, max_length))

# 2) CNN : 입력 -> 임베딩 -> CNN
X_Embed_CNN = Embedding(input_dim=max_features, output_dim=n_embed, input_length=max_length)(X_Input)
X_Embed_CNN_2 = Dropout(0.2)(X_Embed_CNN) # CNN 최종 임베딩
X_Conv = Conv1D(filters=n_filters, kernel_size=s_filters, strides=1, padding='same', activation='relu')(X_Embed_CNN_2)
X_Pool = GlobalMaxPooling1D()(X_Conv)
X_Dense = Dense(n_hidden, activation='relu')(X_Pool)
X_Dense_2 = Dropout(0.5)(X_Dense)
X_Flatten = Flatten()(X_Pool)

# 3) LSTM : 입력 -> 임베딩 -> LSTM
X_Embed_LSTM = Embedding(input_dim=max_features, output_dim=n_embed, input_length=max_length)(X_Input)
X_Embed_LSTM_2 = Dropout(0.2)(X_Embed_LSTM) # LSTM 최종 임베딩
X_LSTM = Bidirectional(LSTM(n_hidden, return_sequences=True))(X_Embed_LSTM_2) ###### LSTM에 왜 relu를 넣어 놨니ㅠㅠ
X_LSTM = Flatten()(X_LSTM)

# 4) 네트워크 concat : CNN + LSTM -> FFNt
X_merge = Concatenate()([X_Flatten, X_LSTM])
y_output = Dense(1, activation='sigmoid')(X_merge)

####### ========== 모델 구성 ========== #######
# 학습할 모델: 감성분석 수행
model = Model(X_Input, y_output) # 컴파일할 모델
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001))
print("========== 전체 모델 구조 확인 ==========")
print(model.summary())

# 임베딩 벡터 확인을 위해 구성한 임베딩 모델
cnn_embed_model = Model(X_Input, X_Embed_CNN_2) # CNN 임베딩 모델
lstm_embed_model = Model(X_Input, X_Embed_LSTM_2) # LSTM 임베딩 모델

####### ========== 모델 학습 ========== #######
es = EarlyStopping(monitor='val_loss', patience=5, verbose=1)
hist = model.fit(X_train, y_train,
                 batch_size=BATCH,
                 epochs=EPOCHS,
                 validation_data=(X_test, y_test),
                 callbacks=[es])

####### ========== 모델 성능 확인 ========== #######
# loss 확인
plt.plot(hist.history['loss'], label='Train Loss')
plt.plot(hist.history['val_loss'], label='Test Loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.title('Loss Trajectory')
plt.show()

# 예측 및 결과 확인
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
y_train_pred = np.reshape(np.where(y_train_pred > 0.5, 1, 0), y_train.shape)
y_test_pred = np.reshape(np.where(y_test_pred > 0.5, 1, 0), y_test.shape)
print(f"Train Accuracy: {accuracy_score(y_train, y_train_pred)}")
print(f"Test Accuracy: {accuracy_score(y_test, y_test_pred)}")

####### ========== 임베딩 차이 확인 ========== #######
sample_sent = X_train[0]
print(sample_sent)

cnn_res = cnn_embed_model.predict(sample_sent.reshape(-1, max_length))
lstm_res = lstm_embed_model.predict(sample_sent.reshape(-1, max_length))

print("========== CNN 모델 임베딩 결과 ============")
print(cnn_res.reshape(max_length, -1))
print()
print("========== LSTM 모델 임베딩 결과 ============")
print(lstm_res.reshape(max_length, -1))