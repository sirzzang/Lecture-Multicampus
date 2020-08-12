# Attention을 이용한 ChatBot : 채팅 모듈
#
# 2020.06.04 : 조성현 (blog.naver.com/chunjein)
# ---------------------------------------------
from tensorflow.keras.layers import Input, LSTM, Dense, Dot
from tensorflow.keras.layers import Activation, Concatenate
from tensorflow.keras.layers import Embedding, TimeDistributed
from tensorflow.keras.models import Model
import tensorflow.keras.backend as K
import numpy as np
import pickle

import sys
sys.getdefaultencoding() 

# 단어 목록 dict를 읽어온다.
with open('./dataset/6-1.vocabulary.pickle', 'rb') as f:
    word2idx,  idx2word = pickle.load(f)
    
VOCAB_SIZE = len(idx2word)
EMB_SIZE = 128
LSTM_HIDDEN = 128
MAX_SEQUENCE_LEN = 10            # 단어 시퀀스 길이
MODEL_PATH = './dataset/6-6.Attention.h5'

# Encoder 출력과 decoder 출력으로 attention value를 생성하고,
# decoder 출력 + attention value (concatenate)를 리턴한다.
# x : encoder 출력, y : decoder 출력
# LSTM time step = 4, SMB_SIZE = 3 이라면 각 텐서의 dimension은
# 아래 주석과 같다.
def Attention(x, y):
    # step-1:
    # decoder의 매 시점마다 encoder의 전체 시점과 dot-product을 수행한다.
    score = Dot(axes=(2, 2))([y, x])                   # (1, 4, 4)
    
    # step-2:
    # dot-product 결과를 확률분포로 만든다 (softmax)
    # 이것이 attention score이다.
    dist = Activation('softmax')(score)                # (1, 4, 4)

    # step-3:    
    # encoder의 전체 시점에 위의 확률 분포를 적용해서 가중 평균한다.
    # 직접 계산이 어렵기 때문에 dist를 확장하고, 열을 복제해서
    # Dot 연산이 가능하도록 trick을 쓴다.
    # 이것이 attention value이다.
    # dist_exp = K.expand_dims(dist, 2)                   # (1, 4, 1, 4)
    # dist_rep = K.repeat_elements(dist_exp, EMB_SIZE, 2) # (1, 4, 3, 4)                                       
    # dist_dot = Dot(axes=(3, 1))([dist_rep, x])          # (1, 4, 3, 3)
    # attention = K.mean(dist_dot, axis = 2)              # (1, 4, 3)

    # step-4:
    # 교재의 step-3을 계산하지 않고 step-4를 직접 계산했다.
    attention = Dot(axes=(2, 1))([dist, x])
    
    # step-5:
    # decoder 출력과 attention을 concatenate 한다.
    return Concatenate()([y, attention])    # (1, 4, 6)

# 워드 임베딩 레이어. Encoder와 decoder에서 공동으로 사용한다.
K.clear_session()
wordEmbedding = Embedding(input_dim=VOCAB_SIZE, output_dim=EMB_SIZE)

# Encoder
# -------
# many-to-many로 구성한다. Attention value를 계산하기 위해 중간 출력이 필요하고
# (return_sequences=True), decoder로 전달할 h와 c도 필요하다 (return_state = True)
encoderX = Input(batch_shape=(None, MAX_SEQUENCE_LEN))
encEMB = wordEmbedding(encoderX)
encLSTM1 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
encLSTM2 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
ey1, eh1, ec1 = encLSTM1(encEMB)    # LSTM 1층 
ey2, eh2, ec2 = encLSTM2(ey1)       # LSTM 2층

# Decoder
# -------
# Decoder는 1개 단어씩을 입력으로 받는다. 학습 때와 달리 문장 전체를 받아
# recurrent하는 것이 아니라, 단어 1개씩 입력 받아서 다음 예상 단어를 확인한다.
# chatting()에서 for 문으로 단어 별로 recurrent 시킨다.
# 따라서 batch_shape = (None, 1)이다. 즉, time_step = 1이다. 그래도 네트워크
# 파라메터는 동일하다.
decoderX = Input(batch_shape=(None, 1))
decEMB = wordEmbedding(decoderX)
decLSTM1 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state=True)
decLSTM2 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state=True)
dy1, _, _ = decLSTM1(decEMB, initial_state = [eh1, ec1])
dy2, _, _ = decLSTM2(dy1, initial_state = [eh2, ec2])
att_dy2 = Attention(ey2, dy2)
decOutput = TimeDistributed(Dense(VOCAB_SIZE, activation='softmax'))
outputY = decOutput(att_dy2)

# Model
# -----
model = Model([encoderX, decoderX], outputY)
model.load_weights(MODEL_PATH)

# Chatting용 model
model_enc = Model(encoderX, [eh1, ec1, eh2, ec2, ey2])

ih1 = Input(batch_shape = (None, LSTM_HIDDEN))
ic1 = Input(batch_shape = (None, LSTM_HIDDEN))
ih2 = Input(batch_shape = (None, LSTM_HIDDEN))
ic2 = Input(batch_shape = (None, LSTM_HIDDEN))
ey = Input(batch_shape = (None, MAX_SEQUENCE_LEN, LSTM_HIDDEN))

dec_output1, dh1, dc1 = decLSTM1(decEMB, initial_state = [ih1, ic1])
dec_output2, dh2, dc2 = decLSTM2(dec_output1, initial_state = [ih2, ic2])
dec_attention = Attention(ey, dec_output2)
dec_output = decOutput(dec_attention)
model_dec = Model([decoderX, ih1, ic1, ih2, ic2, ey], 
                  [dec_output, dh1, dc1, dh2, dc2])

# Question을 입력받아 Answer를 생성한다.
def genAnswer(question):
    question = question[np.newaxis, :]
    init_h1, init_c1, init_h2, init_c2, enc_y = model_enc.predict(question)

    # 시작 단어는 <START>로 한다.
    word = np.array(word2idx['<START>']).reshape(1, 1)

    answer = []
    for i in range(MAX_SEQUENCE_LEN):
        dY, next_h1, next_c1, next_h2, next_c2 = \
            model_dec.predict([word, init_h1, init_c1, init_h2, init_c2, enc_y])
        
        # 디코더의 출력은 vocabulary에 대응되는 one-hot이다.
        # argmax로 해당 단어를 채택한다.
        nextWord = np.argmax(dY[0, 0])
        
        # 예상 단어가 <END>이거나 <PADDING>이면 더 이상 예상할 게 없다.
        if nextWord == word2idx['<END>'] or nextWord == word2idx['<PADDING>']:
            break
        
        # 다음 예상 단어인 디코더의 출력을 answer에 추가한다.
        answer.append(idx2word[nextWord])
        
        # 디코더의 다음 recurrent를 위해 입력 데이터와 hidden 값을
        # 준비한다. 입력은 word이고, hidden은 h와 c이다.
        word = np.array(nextWord).reshape(1,1)
    
        init_h1 = next_h1
        init_c1 = next_c1
        init_h2 = next_h2
        init_c2 = next_c2
        
    return ' '.join(answer)

# Chatting
def chatting(n=100):
    for i in range(n):
        question = input('Q : ')
        
        if  question == 'quit':
            break
        
        q_idx = []
        for x in question.split(' '):
            if x in word2idx:
                q_idx.append(word2idx[x])
            else:
                q_idx.append(word2idx['<UNKNOWN>'])   # out-of-vocabulary (OOV)
        
        # <PADDING>을 삽입한다.
        if len(q_idx) < MAX_SEQUENCE_LEN:
            q_idx.extend([word2idx['<PADDING>']] * (MAX_SEQUENCE_LEN - len(q_idx)))
        else:
            q_idx = q_idx[0:MAX_SEQUENCE_LEN]
        
        answer = genAnswer(np.array(q_idx))
        print('A :', answer)

chatting(100)

# 대화 내용 예시
# 가끔 궁금해 : 그 사람도 그럴 거예요.,0
# 가끔 뭐하는지 궁금해 : 그 사람도 그럴 거예요.,0
# 가끔은 혼자인게 좋다 : 혼자를 즐기세요.,0
# 가난한 자의 설움 : 돈은 다시 들어올 거예요.,0
# 가만 있어도 땀난다 : 땀을 식혀주세요.,0
# 가상화폐 쫄딱 망함 : 어서 잊고 새출발 하세요.,0
# 가스불 켜고 나갔어 : 빨리 집에 돌아가서 끄고 나오세요.,0
# 가스불 켜놓고 나온거 같아 : 빨리 집에 돌아가서 끄고 나오세요.,0
# 가스비 너무 많이 나왔다. : 다음 달에는 더 절약해봐요.,0
# 가스비 비싼데 감기 걸리겠어 : 따뜻하게 사세요!,0
# 남자친구 교회 데려가고 싶어 : 마음을 열 때까지 설득해보세요.,0
# 남자친구 또 운동 갔어 : 운동을 함께 해보세요.,0
# 남자친구 생일인데 뭘 줄까 : 평소에 필요한 것 생각해보세요.,0
# 남자친구 승진 선물로 뭐가 좋을까? : 평소에 필요했던 게 좋을 것 같아요.,0
# 남자친구 오늘 따라 훈훈해 보인다 : 전생에 나라를 구하셨나요.,0
# 남자친구 오늘 좀 질린다. : 결단은 빠를수록 좋아요.,0
# 남자친구가 나 안 믿어줘 : 거짓말 적당히 하세요.,0
# 남자친구가 너무 바빠 : 너무 집착하지 마세요.,0
# 남자친구가 너무 운동만 해 : 운동을 함께 해보세요.,0
# 남자친구가 너무 잘생겼어 : 전생에 나라를 구하셨나요.,0