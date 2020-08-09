# 영화리뷰 데이터 감성분석
# 데이터 : Kaggle의 Bags of Words Meets Bags of Popcorns
# Kaggle의 우승자 Alejandro Pelaez의 문서 내용을 적용한다.
#
# 2차 전처리 작업을 수행한다. (Mutual Information을 고려한 사전 생성)
#
# 참고 문서 : 
# https://pdfs.semanticscholar.org/c521/80a8fe1acc99b4bf3cf3e11d3c8a38e2c7ff.pdf
#
# 2020.08.07 삼성멀티캠퍼스 혁신성장 (A)반 수업 자료
# -------------------------------------------------------------------------------
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

# 1차 전처리가 완료된 데이터를 읽어온다.
train_data = pd.read_csv('dataset/1.train_clean.csv')

reviews = list(train_data['review'])
sentiments = np.array(list(train_data['sentiment']))

# 1차 vocabulary를 생성하고, 리뷰 데이터를 인덱스로 표현한다.
tokenizer = Tokenizer()
tokenizer.fit_on_texts(reviews)
word2idx = tokenizer.word_index
idx2word = {v:k for k, v in word2idx.items()}
text_sequences = tokenizer.texts_to_sequences(reviews)

# [단어-label] 리스트를 만든다.
word_label = []
for review, label in zip(text_sequences, sentiments):
    for w in review:
        word_label.append([w, label])
        
word_label = np.array(word_label)

# 단어마다 Mutual Information (MI)을 계산한다.
#
# word_label : 단어 인덱스 - label 목록 배열 (예시)
#              [[   2, 0],
#               [  85, 0], ...]
#
# MI = p(x|y=0) * p(y=0) * log(p(x|y=0) / p(x)) +
#      p(x|y=1) * p(y=1) * log(p(x|y=1) / p(x))
#
# where, x = 단어, y = label
# p(x | y=0)의 의미 : label이 '0'인 것 중에 (ex) x = 'like'인 확률
# ===============================================================

# y = 0인 단어목록 (x[0])과 y = 1인 단어목록 (x[1])을 만들어 둔다.
x = np.array([np.where(word_label[:, 1] == i)[0] for i in [0, 1]])

# p(y=0)과 p(y=1)을 계산해 둔다. py[0] = p(y=0), py[1] = p(y=1)
py = np.array([(word_label[:, 1] == i).mean() for i in [0, 1]])
N = len(idx2word)

# 모든 단어에 대해 위의 공식으로 MI를 계산한다. (시간이 걸린다. 약 10분?)
mi_word = []
for i in range(1, N):
    px = (word_label[:, 0] == i).mean()
    
    mi = 0
    for y in [0, 1]:
        pxy = (word_label[x[y], 0] == i).mean()
        mi += (pxy * py[y]) * np.log(1e-8 + pxy / px)
        
    mi_word.append([mi, i])
    
    if i % 100 == 0:
        print(i, '/', N)

# mi_word 리스트를 내림차순으로 정렬한다.
mi_word.sort(reverse = True)

# MI 상위 20개 단어를 확인해 본다. Pelaez의 문서 내용과 일치하는지 확인한다.
print([idx2word[y] for x, y in mi_word[:20]])

# MI 상위 50% 단어로 vocabulrary를 생성한다.
n = int(len(mi_word) * 0.5)
word2idx2 = {idx2word[y]:(i+1) for i, [x, y] in enumerate(mi_word[:n])}
idx2word2 = {v:k for k, v in word2idx2.items()}

# MI 기반 vocabulary를 이용하여 리뷰 데이터를 다시 만든다. OOV는 제거한다.
new_review = []
for review in reviews:
    r = []
    for w in review.split():
        if w in word2idx2:    # OOV 제거
            r.append(w)
    new_review.append(r)

# 결과를 저장해 둔다.
with open('dataset/2.train_input.pickle', 'wb') as f:
    pickle.dump([new_review, sentiments, word2idx2, idx2word2], f, pickle.HIGHEST_PROTOCOL)