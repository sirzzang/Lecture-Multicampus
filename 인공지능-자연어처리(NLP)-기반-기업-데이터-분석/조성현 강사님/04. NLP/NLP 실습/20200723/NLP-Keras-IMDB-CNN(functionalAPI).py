# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VBz3cYXkMPTZp0umrd-XIuvDxADhKHKq
"""

# 모듈 불러오기
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Activation, Embedding, Dropout, Conv1D, GlobalMaxPooling1D
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np

# 파라미터 설정
max_features = int(input('최대 단어 수 설정: ')) # 어휘 집합 수
max_length = int(input('문장 길이 설정: '))

# 데이터 로드 및 확인
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)
print(f"훈련 데이터: {X_train.shape}, 훈련 라벨: {y_train.shape}")
print(f"테스트 데이터: {y_train.shape}, 테스트 라벨: {y_test.shape}")
print()
print("훈련 데이터 샘플 확인")
print(X_train[0]) # 단어 인덱스 확인
print()

# 어휘집합
vocabulary = imdb.get_word_index() # dict
vocab_dict = dict((v, k) for k, v in vocabulary.items())

# IMDB 데이터셋 문장 decode
def decode_sent(sentences, vocabulary=vocab_dict):
    '''
    - 0: padding, 1: start, 2: OOV
    - 실제 word index에서 3을 빼고, 없으면 '*'로 채운다.
    '''
    temp_sent = []
    for sent in sentences:
        temp = vocab_dict.get(sent-3, '*')
        temp_sent.append(temp)
    
    comb_sent = " ".join(temp_sent)

    return comb_sent

# 디코드해서 확인
print(decode_sent(X_train[0])) # 문장 앞에 '*' 붙는다.

# 패딩
X_train = pad_sequences(X_train, maxlen=max_length)
X_test = pad_sequences(X_test, maxlen=max_length)
print("========== 패딩 후 ==========")
print(f"훈련 데이터: {X_train.shape}")
print(f"테스트 데이터: {X_test.shape}")

# OOV 확인
for i in range(10):
    print(f"{i}번째 문장에서 OOV 개수: {(X_train[i] == 2).sum()}")
print()

# 네트워크 파라미터
BATCH = int(input('배치 사이즈 설정: '))
n_embed = int(input('임베딩 차원 설정: '))
n_filters = int(input('컨볼루션 필터 개수 설정: '))
s_filters = int(input('컨볼루션 필터 사이즈 설정: '))
n_hidden = int(input('은닉 노드 수 설정: '))
EPOCHS = int(input('학습 횟수 설정: '))

# 모델 레이어 구성
X_Input = Input(batch_shape=(None, max_length))
X_Embed = Embedding(input_dim=max_features, output_dim=n_embed, input_length=max_length)(X_Input)
X_Embed2 = Dropout(0.2)(X_Embed)
X_Conv = Conv1D(filters=n_filters, kernel_size=s_filters, strides=1, padding='valid', activation='relu')(X_Embed2)
X_Pool = GlobalMaxPooling1D()(X_Conv)
X_Dense = Dense(n_hidden, activation='relu')(X_Pool)
X_Dense2 = Dropout(0.5)(X_Dense)
y_output = Dense(1, activation='sigmoid')(X_Dense2)

# 모델 구성
model = Model(X_Input, y_output)

# 모델 컴파일
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001))
print("========== 모델 전체 구조 확인 ==========")
print(model.summary())
print()

# 모델 학습
es = EarlyStopping(monitor='val_loss', patience=5, verbose=1)
hist= model.fit(X_train, y_train,
                batch_size=BATCH,
                epochs=EPOCHS,
                validation_data=(X_test, y_test),
                callbacks=[es])

# plot loss
plt.plot(hist.history['loss'], label='Train Loss')
plt.plot(hist.history['val_loss'], label='Test Loss')
plt.legend()
plt.title('Loss Trajectory')
plt.xlabel('epoch')
plt.ylabel('Loss')
plt.show()
print()

# 예측 및 결과 확인: Deprecation Warning 주의
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
y_train_pred = np.reshape(np.where(y_train_pred > 0.5, 1, 0), y_train.shape)
y_test_pred = np.reshape(np.where(y_test_pred > 0.5, 1, 0), y_test.shape)
print(f"Train Accuracy: {accuracy_score(y_train, y_train_pred)}")
print(f"Test Accuracy: {accuracy_score(y_test, y_test_pred)}")