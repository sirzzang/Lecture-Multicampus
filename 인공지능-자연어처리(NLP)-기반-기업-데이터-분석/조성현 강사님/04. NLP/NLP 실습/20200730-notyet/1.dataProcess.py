# IMDB 데이터를 전처리 한다.
# ------------------------
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk import pos_tag
from nltk.stem import PorterStemmer
import collections
from tensorflow.keras.datasets import imdb
import pickle

# 전처리
def MyPreprocessing(text):
    text2 = "".join([" " if ch in string.punctuation else ch for ch in text])
    tokens = nltk.word_tokenize(text2)
    tokens = [word.lower() for word in tokens]
    
    stopwds = stopwords.words('english')
    tokens = [token for token in tokens if token not in stopwds]
    
    tokens = [word for word in tokens if len(word)>=3]
    
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    tagged_corpus = pos_tag(tokens)    
    
    Noun_tags = ['NN','NNP','NNPS','NNS']
    Verb_tags = ['VB','VBD','VBG','VBN','VBP','VBZ']

    lemmatizer = WordNetLemmatizer()

    def prat_lemmatize(token,tag):
        if tag in Noun_tags:
            return lemmatizer.lemmatize(token,'n')
        elif tag in Verb_tags:
            return lemmatizer.lemmatize(token,'v')
        else:
            return lemmatizer.lemmatize(token,'n')
    
    pre_proc_text =  " ".join([prat_lemmatize(token,tag) for token,tag in tagged_corpus])             

    return pre_proc_text

# IMDB 데이터에 사용된 총 단어의 종류는 88,584개 (vocabulary 크기)이다.
# 가장 많이 사용되는 6,000개 단어만 사용하고, 나머지는 OOV로 표시한다.
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=6000,
                                                      start_char=0,
                                                      oov_char=0,
                                                      index_from=0)

# train, test 데이터를 합친다. 필요한 경우 나중에 나눠쓴다.
text = np.hstack([x_train, x_test])
label = np.hstack([y_train, y_test])

# vocabulary를 가져온다.
word2idx = imdb.get_word_index()
idx2word = dict((v,k) for k,v in word2idx.items())

# start_char와 oov_char는 '.'으로 표시해 둔다. 나중에 전처리 과정에서 제거된다.
idx2word[0] = '.'

# 숫자로 표시된 x_train을 실제 단어로 변환한다.
def decode(review):
    x = [idx2word[s] for s in review]
    return ' '.join(x)

# 리뷰 문서를 전처리한다.
reviews = []
for i, review in enumerate(text):
    reviews.append(MyPreprocessing(decode(review)))
    if i % 100 == 0: print(i)

# 전처리된 리뷰 문서로 vocabulary를 다시 생성한다.
counter = collections.Counter()
for line in reviews:
    for word in nltk.word_tokenize(line):
        counter[word.lower()] += 1

word2idx2 = {w:(i+1) for i, (w, _) in enumerate(counter.most_common())}
idx2word2 = {v:k for k,v in word2idx2.items()}

# 전처리된 리뷰 문서와 vocabulary를 저장한다.
with open('data/preprocessed_review.pickle', 'wb') as f:
    pickle.dump([reviews, label, word2idx2, idx2word2], f, pickle.HIGHEST_PROTOCOL)
