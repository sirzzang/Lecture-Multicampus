# Attention을 이용한 ChatBot : 학습 모듈
#
# 2020.06.04 : 조성현 (blog.naver.com/chunjein)
# ---------------------------------------------
from tensorflow.keras.layers import Input, LSTM, Dense, Dot
from tensorflow.keras.layers import Activation, Concatenate
from tensorflow.keras.layers import Embedding, TimeDistributed
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt
import pickle

# 단어 목록 dict를 읽어온다.
with open('./dataset/6-1.vocabulary.pickle', 'rb') as f:
    word2idx,  idx2word = pickle.load(f)
    
# 학습 데이터 : 인코딩, 디코딩 입력, 디코딩 출력을 읽어온다.
with open('./dataset/6-1.train_data.pickle', 'rb') as f:
    trainXE, trainXD, trainYD = pickle.load(f)
	
# 평가 데이터 : 인코딩, 디코딩 입력, 디코딩 출력을 만든다.
with open('./dataset/6-1.eval_data.pickle', 'rb') as f:
    testXE, testXD, testYD = pickle.load(f)

VOCAB_SIZE = len(idx2word)
EMB_SIZE = 128
LSTM_HIDDEN = 128
MODEL_PATH = './dataset/6-6.Attention.h5'
LOAD_MODEL = True

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
encoderX = Input(batch_shape=(None, trainXE.shape[1]))
encEMB = wordEmbedding(encoderX)
encLSTM1 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
encLSTM2 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
ey1, eh1, ec1 = encLSTM1(encEMB)    # LSTM 1층 
ey2, eh2, ec2 = encLSTM2(ey1)       # LSTM 2층

# Decoder
# -------
# many-to-many로 구성한다. target을 학습하고 Attention을 위해서는 중간 출력이 
# 필요하다. 그리고 초기 h와 c는 encoder에서 출력한 값을 사용한다 (initial_state)
# 최종 출력은 vocabulary의 인덱스인 one-hot 인코더이다.
decoderX = Input(batch_shape=(None, trainXD.shape[1]))
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
# target이 one-hot encoding되어 있으면 categorical_crossentropy
# target이 integer로 되어 있으면 sparse_categorical_crossentropy를 쓴다.
# sparse_categorical_entropy는 integer인 target을 one-hot으로 바꾼 후에
# categorical_entropy를 수행한다.
model = Model([encoderX, decoderX], outputY)
model.compile(optimizer=optimizers.Adam(lr=0.001), 
              loss='sparse_categorical_crossentropy')

if LOAD_MODEL:
    model.load_weights(MODEL_PATH)

# 학습 (teacher forcing)
# ----------------------
# loss = sparse_categorical_crossentropy이기 때문에 target을 one-hot으로 변환할
# 필요 없이 integer인 trainYD를 그대로 넣어 준다. trainYD를 one-hot으로 변환해서
# categorical_crossentropy로 처리하면 out-of-memory 문제가 발생할 수 있다.
hist = model.fit([trainXE, trainXD], trainYD, batch_size = 300, 
                 epochs=1, shuffle=True,
                 validation_data = ([testXE, testXD], testYD))

# Loss history를 그린다
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 학습 결과를 저장한다
model.save_weights(MODEL_PATH)

