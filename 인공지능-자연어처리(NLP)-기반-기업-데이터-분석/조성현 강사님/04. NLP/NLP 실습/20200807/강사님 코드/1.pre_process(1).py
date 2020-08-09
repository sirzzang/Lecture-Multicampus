# 영화리뷰 데이터 감성분석
# 데이터 : Kaggle의 Bags of Words Meets Bags of Popcorns
# Kaggle의 우승자 Alejandro Pelaez의 문서 내용을 적용한다.
#
# 1차 전처리 작업을 수행한다. (HTML 태그, 불용어 제거 및 Stemming)
#
# 2020.08.07 삼성멀티캠퍼스 혁신성장 (A)반 수업 자료
# --------------------------------------------------------------
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# 4.1 장에서 사용할 데이터인 영화 리뷰 데이터를 불러온다
train_data = pd.read_csv('dataset/0.labeledTrainData.tsv', 
                         header = 0, delimiter = '\t', quoting = 3)

# 1차 전처리 작업
def preprocessing(review, stops, remove_stopwords = True): 
    # 1. HTML 태그 제거
    review_text = BeautifulSoup(review, "html5lib").get_text()

    # 2. 영어가 아닌 특수문자들을 공백(" ")으로 바꾸기
    review_text = re.sub("[^a-zA-Z]", " ", review_text)

    # 3. 대문자들을 소문자로 바꾸고 공백단위로 텍스트들 나눠서 리스트로 만든다.
    words = review_text.lower().split()

    # 4. 불용어 제거
    words = [w for w in words if not w in stops]

    # 5. Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(w) for w in words]

    # 6. 단어 리스트를 공백을 넣어서 하나의 글로 합친다.
    clean_review = ' '.join(words)
    return clean_review

stops = set(stopwords.words("english"))
clean_train_reviews = []
for review in train_data['review']:
    r = preprocessing(review, stops, remove_stopwords = True)
    clean_train_reviews.append(r)

# 전처리한 데이터 확인
clean_train_reviews[0]

# 전처리가 완료된 리뷰 데이터를 데이터프레임으로 구성한다. (학습할 데이터)
clean_train_df = pd.DataFrame({'review': clean_train_reviews, 
                               'sentiment': train_data['sentiment']})

# 전처리가 완료된 리뷰 데이터를 저장한다.
clean_train_df.to_csv('dataset/1.train_clean.csv', index = False)
