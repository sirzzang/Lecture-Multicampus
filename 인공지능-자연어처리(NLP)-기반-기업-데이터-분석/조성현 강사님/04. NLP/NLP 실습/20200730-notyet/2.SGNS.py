# SkNS 학습. pre-trained embedding vector를 생성한다.
# -------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from tensorflow.keras.layers import Input, Dense, Dropout, Embedding
from tensorflow.keras.layers import Dot, Activation, Reshape
from tensorflow.keras.models import Model
import pickle
import nltk

# 전처리가 완료된 IMDB 데이터를 읽어온다.
with open('data/preprocessed_review.pickle', 'rb') as f:
    reviews, label, word2idx, idx2word = pickle.load(f)

# Trigram으로 학습 데이터를 생성한다.
xs = []     # 입력 데이터
ys = []     # 출력 데이터
for line in reviews:   
    # 사전에 부여된 번호로 단어들을 표시한다.
    embedding = [word2idx[w.lower()] for w in nltk.word_tokenize(line)]
    
    # Trigram으로 주변 단어들을 묶는다.
    triples = list(nltk.trigrams(embedding))
    
    # 왼쪽 단어, 중간 단어, 오른쪽 단어로 분리한다.
    w_lefts = [x[0] for x in triples]
    w_centers = [x[1] for x in triples]
    w_rights = [x[2] for x in triples]
    
    # 입력 (xs)      출력 (xy)
    # ---------    -----------
    # 중간 단어 --> 왼쪽 단어
    # 중간 단어 --> 오른쪽 단어
    xs.extend(w_centers)
    ys.extend(w_lefts)
    xs.extend(w_centers)
    ys.extend(w_rights)

# SGNS용 학습 데이터를 생성한다.
rand_word = np.random.randint(1, len(word2idx), len(xs))
x_pos = np.vstack([xs, ys]).T
x_neg = np.vstack([xs, rand_word]).T

y_pos = np.ones(x_pos.shape[0]).reshape(-1,1)
y_neg = np.zeros(x_neg.shape[0]).reshape(-1,1)

x_total = np.vstack([x_pos, x_neg])
y_total = np.vstack([y_pos, y_neg])

X = np.hstack([x_total, y_total])
np.random.shuffle(X)

# SGNS 모델을 생성한다.
vocab_size = len(word2idx) + 1  # 사전의 크기
EMB_SIZE = 64
BATCH_SIZE = 10240
NUM_EPOCHS = 10

inputX = Input(batch_shape = (None, 1))
inputY = Input(batch_shape = (None, 1))
embX = Embedding(vocab_size, EMB_SIZE)(inputX)
embY = Embedding(vocab_size, EMB_SIZE)(inputY)
dotXY = Dot(axes=2)([embX, embY])
dotXY = Reshape((1,))(dotXY)
outputY = Activation('sigmoid')(dotXY)

model = Model([inputX, inputY], outputY)
model.compile(optimizer = "adam", loss="binary_crossentropy")
model.summary()

# 학습
hist = model.fit([X[:, 0], X[:, 1]], X[:, 2],
                 batch_size=BATCH_SIZE,
                 epochs=NUM_EPOCHS)

# Embedding (left side) layer의 W를 저장해 둔다
with open('data/embedding_W.pickle', 'wb') as f:
    pickle.dump(model.layers[2].get_weights(), f, pickle.HIGHEST_PROTOCOL)

