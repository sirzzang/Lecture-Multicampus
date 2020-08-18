# Transformer ChatBot : 채팅 모듈
# 참고 : https://github.com/suyash/transformer
#
# 2020.06.07 : 조성현 (blog.naver.com/chunjein)
# ---------------------------------------------
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
import tensorflow.keras.backend as K
from transformer import Transformer
import sentencepiece as spm
import pickle
import numpy as np

MAX_SEQUENCE_LEN = 15
MODEL_PATH = './dataset/transformer_model.h5'
SPM_MODEL = "./dataset/qa_model.model"

sp = spm.SentencePieceProcessor()
sp.Load(SPM_MODEL)

# 단어 목록 dict를 읽어온다.
with open('./dataset/vocabulary.pickle', 'rb') as f:
    word2idx,  idx2word = pickle.load(f)

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
model.load_weights(MODEL_PATH)
    
# Question을 입력받아 Answer를 생성한다.
def genAnswer(question):
    question = question[np.newaxis, :]
    target = np.array(word2idx['<START>']).reshape(1, 1)

    answer = []
    for i in range(MAX_SEQUENCE_LEN):
        preds = model.predict_on_batch([question, target])
        
        # 디코더의 출력은 vocabulary에 대응되는 one-hot이다.
        # argmax로 해당 단어를 채택한다.
        nextWord = np.argmax(preds[:, -1:, :], axis=-1)
        
        # 예상 단어가 <END>이거나 <PAD>이면 더 이상 예상할 게 없다.
        if nextWord == word2idx['<END>'] or nextWord == word2idx['<PAD>']:
            break

        # 다음 예상 단어인 디코더의 출력을 answer에 추가한다.
        answer.append(idx2word[nextWord[0][0]])
        
        # 다음 target을 준비한다.
        target = np.concatenate([target, nextWord], axis = -1)
    
    return sp.decode_pieces(answer)

# Chatting
def chatting(n=100):   
    for i in range(n):
        question = input('Q : ')
        
        if  question == 'quit':
            break
        
        q_idx = []
        for x in sp.encode_as_pieces(question):
            if x in word2idx:
                q_idx.append(word2idx[x])
            else:
                q_idx.append(word2idx['<UNK>'])   # out-of-vocabulary (OOV)
        
        # <PAD>을 삽입한다.
        if len(q_idx) < MAX_SEQUENCE_LEN:
            q_idx.extend([word2idx['<PAD>']] * (MAX_SEQUENCE_LEN - len(q_idx)))
        else:
            q_idx = q_idx[0:MAX_SEQUENCE_LEN]

        answer = genAnswer(np.array(q_idx))
        print('A :', answer)

####### Chatting 시작 #######
print("\nTransformer ChatBot (ver. 1.0)")
print("Chatting 모듈을 로드하고 있습니다 ...")

# 처음 1회는 시간이 걸리기 때문에 dummy question을 입력한다.
answer = genAnswer(np.zeros(MAX_SEQUENCE_LEN))
print("ChatBot이 준비 됐습니다.\n")

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

    