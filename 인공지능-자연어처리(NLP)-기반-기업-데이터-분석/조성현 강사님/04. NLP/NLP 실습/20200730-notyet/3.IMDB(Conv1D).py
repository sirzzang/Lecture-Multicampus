# SGNS로 pre-trained된 embedding vector를 이용해서
# IMDB 리뷰 문서들을 분류한다 (감성분석).
# -----------------------------------------------
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, Activation
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import pickle
import nltk

# 전처리가 완료된 IMDB 데이터를 읽어온다.
with open('data/preprocessed_review.pickle', 'rb') as f:
    reviews, label, word2idx, idx2word = pickle.load(f)

# pre-trained embedding layer의 W를 읽어온다.
with open('data/embedding_W.pickle', 'rb') as f:
    We = pickle.load(f)

# 학습 데이터를 vocabulary의 인덱스 (수치)로 표현한다.
X = []
for review in reviews:
    X.append([word2idx[w] for w in nltk.word_tokenize(review)])
             
# 학습, 시험 데이터로 분리한다.
x_train, x_test, y_train, y_test = train_test_split(X, label, test_size=0.2)


vocab_size = len(word2idx) + 1  # 사전의 크기
max_length = 200                # 한 개 리뷰 문서의 최대 단어 길이
   
# 1개 리뷰 문서의 단어 개수를 max_length = 200으로 맞춘다.
# 200개 보다 작으면 padding = 0을 추가하고, 200개 보다 크면 뒷 부분을 자른다.
x_train = sequence.pad_sequences(x_train, maxlen=max_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_length)

# Deep Learning architecture parameters
batch_size = 512
embedding_dims = 64
num_kernels = 260        # convolution filter 개수
kernel_size = 3          # convolution filter size
hidden_dims = 300
epochs = 100
xInput = Input(batch_shape = (None, max_length))
emb = Embedding(vocab_size, embedding_dims)(xInput)
emb = Dropout(0.5)(emb)
conv = Conv1D(num_kernels, kernel_size, padding='valid', activation='relu', strides=1)(emb)
conv = GlobalMaxPooling1D()(conv)
ffn = Dense(hidden_dims)(conv)
ffn = Dropout(0.5)(ffn)
ffn = Activation('relu')(ffn)
ffn = Dense(1)(ffn)
yOutput = Activation('sigmoid')(ffn)

model = Model(xInput, yOutput)
model.compile(loss='binary_crossentropy', optimizer='adam')
print(model.summary())

# SKNS에서 학습한 We를 적용한다. (pre-trained)
model.layers[1].set_weights(We)

# 학습한다. (fine-tune)
hist = model.fit(x_train, y_train, 
                 batch_size=batch_size, 
                 epochs=epochs,
                 validation_data = (x_test, y_test))

# Loss history를 그린다
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 성능 확인
y_pred = model.predict(x_test)
y_pred = np.where(y_pred > 0.5, 1, 0)
print ("Test accuracy:", accuracy_score(y_test, y_pred))

