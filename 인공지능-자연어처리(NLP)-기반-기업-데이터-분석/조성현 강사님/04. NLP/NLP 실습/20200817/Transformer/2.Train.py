# Transformer ChatBot : 학습 모듈
# 참고 : https://github.com/suyash/transformer
#
# 2020.06.07 : 조성현 (blog.naver.com/chunjein)
# ---------------------------------------------
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras import optimizers
import tensorflow.keras.backend as K
from transformer import Transformer
import matplotlib.pyplot as plt
import pickle

MODEL_PATH = './dataset/transformer_model.h5'
LOAD_MODEL = True

# 단어 목록 dict를 읽어온다.
with open('./dataset/vocabulary.pickle', 'rb') as f:
    word2idx,  idx2word = pickle.load(f)
    
# 학습 데이터 : 인코딩, 디코딩 입력, 디코딩 출력을 읽어온다.
with open('./dataset/train_data.pickle', 'rb') as f:
    trainXE, trainXD, trainYD = pickle.load(f)
   
# Model
# -----
K.clear_session()
src = Input((None, ), dtype="int32", name="src")
tar = Input((None, ), dtype="int32", name="tar")

logits, enc_enc_attention, dec_dec_attention, enc_dec_attention = Transformer(
    num_layers=4,
    d_model=128,
    num_heads=8,
    d_ff=512,
    input_vocab_size=len(word2idx) + 2,
    target_vocab_size=len(word2idx) + 2,
    dropout_rate=0.1)(src, tar)

model = Model(inputs=[src, tar], outputs=logits)
model.compile(optimizer=optimizers.Adam(lr=0.001), loss='sparse_categorical_crossentropy')

if LOAD_MODEL:
    model.load_weights(MODEL_PATH)

# 학습 (teacher forcing)
# ----------------------
hist = model.fit([trainXE, trainXD], trainYD, 
                 batch_size = 512, 
                 epochs=3, shuffle=True)

# Loss history를 그린다
plt.plot(hist.history['loss'], label='Train loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 학습 결과를 저장한다
model.save(MODEL_PATH)


