# 영화리뷰 데이터 감성분석
# 데이터 : Kaggle의 Bags of Words Meets Bags of Popcorns
# Kaggle의 우승자 Alejandro Pelaez의 문서 내용을 적용한다.
#
# Doc2Vec과 TFIDF로 학습하고 성능을 평가한다.
# - 우승자의 기록에 미치지 못했다. 
#   Accuracy = 0.8776, AUC score = 0.9478. 이유가 무엇일까??
#
# 참고 문서 : 
# https://pdfs.semanticscholar.org/c521/80a8fe1acc99b4bf3cf3e11d3c8a38e2c7ff.pdf
#
# 2020.08.07 삼성멀티캠퍼스 혁신성장 (A)반 수업 자료
# -------------------------------------------------------------------------------
import pandas as pd
import numpy as np

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Concatenate, Dropout
from tensorflow.keras import optimizers
from sklearn.metrics import roc_auc_score
import pickle

# 전처리가 완료된 데이터를 읽어온다.
with open('dataset/2.train_input.pickle', 'rb') as f:
    reviews, y, word2idx, idx2word = pickle.load(f)

# volcbulary의 앞 부분 20개를 확인해 본다.
# Alejandro Pelaez의 문서 내용과 잘 일치한다.
# ['bad', 'worst', 'wast', 'great', 'aw', 'love', 'movi', 'stupid', 
#  'bore', 'terribl', 'excel', 'horribl', 'wors', 'beauti', 'noth', 
#  'best', 'poor', 'even', 'minut', 'crap']
print(list(word2idx)[:20])

# gensim을 이용하여 리뷰 문서들을 Doc2Vec으로 변환한다.
model_name = 'dataset/3.400features.doc2vec'
model_saved = True
EMB_SIZE = 400

if model_saved:
    model = Doc2Vec.load(model_name)
else:
    # gensim 패키지를 이용하여 문장을 vector화 한다 (Doc2Vec)
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(reviews)]
    model = Doc2Vec(vector_size=EMB_SIZE, alpha=0.005, min_alpha=0.0001, 
                    min_count=1, workers=4, dm = 1)
    model.build_vocab(documents)
    model.train(documents, total_examples=len(reviews), epochs=500)
    model.save(model_name)

# 전체 리뷰 문서를 Doc2Vec으로 변환한다.
pvdm = np.array([model.docvecs[i] for i in range(len(reviews))])

# 전체 리뷰 문서를 TFIDF로 변환한다.
sentences = []
for review in reviews:
    sentences.append(' '.join(review))
    
vectorizer = TfidfVectorizer(min_df = 1, analyzer="word", sublinear_tf=True, 
                             ngram_range=(1,1), max_features=EMB_SIZE)
    
tfidf = vectorizer.fit_transform(sentences).toarray()

# 학습 데이터와 시험 데이터로 분리한다.
# 시험데이터까지 Doc2Vec과 TFIDF로 변환했다. 문제의 소지가 있을 수 있다. But...
# 참고 문서의 9.2 뒷부분 참조.
# we are using the test data to build both the tf-idf vectors and to build 
# the distributed document representation, as both approaches are unsupervised,
# and thus do not require labels (This is allowed in the competition rules, 
# as long as they are used as unsupervised data, like we did).
x1_train, x1_test, x2_train, x2_test, y_train, y_test = \
    train_test_split(pvdm, tfidf, y, test_size=0.2)

# 딥러닝으로 classification을 수행한다.
#
# 리뷰 문서 (Doc2Vec) -----> Dense ----+
#                                      |--> Concatenate --> Dense --> label
# 리뷰 문서 (TFIDF) -------> Dense ----+
#
adam = optimizers.Adam(lr=0.0001)

x1 = Input(batch_shape=(None, EMB_SIZE))
x2 = Input(batch_shape=(None, EMB_SIZE))
h1 = Dense(200, activation='relu')(x1)
h1 = Dropout(0.5)(h1)
h2 = Dense(200, activation='relu')(x2)
h2 = Dropout(0.5)(h2)
concat = Concatenate()([h1, h2])
yOutput = Dense(1, activation='sigmoid')(concat)

model = Model([x1, x2], yOutput)
model.compile(loss='binary_crossentropy', optimizer=adam)

model.fit([x1_train, x2_train], y_train,
          batch_size = 512,
          epochs = 500,
          shuffle = True,
          validation_data = ([x1_test, x2_test], y_test))

# 시험 데이터로 학습 성능을 평가한다
predicted = model.predict([x1_test, x2_test])
test_pred = np.where(predicted > 0.5, 1, 0)
accuracy = (y_test.reshape(-1,1) == test_pred).mean()

print("\nAccuracy = %.4f" % accuracy)
print("AUC score = %.4f" % roc_auc_score(y_test, predicted))
