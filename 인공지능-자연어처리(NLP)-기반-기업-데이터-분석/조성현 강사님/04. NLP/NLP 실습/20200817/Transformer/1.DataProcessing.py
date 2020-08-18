# Transformer ChatBot : 학습 데이터 모듈
# Google의 Sentencepiece를 이용해서 학습 데이터를 생성한다.
# > pip install sentencepiece
#
# 2020.06.07 : 조성현 (blog.naver.com/chunjein)
# -----------------------------------------------------
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import sentencepiece as spm
import re
import pickle

# 데이터 파일을 읽어온다.
data_df = pd.read_csv('./dataset/ChatBotData.csv', header=0)
question, answer = list(data_df['Q']), list(data_df['A'])

# 특수 문자를 제거한다.
FILTERS = "([~.,!?\"':;)(])"
question = [re.sub(FILTERS, "", s) for s in question]
answer = [re.sub(FILTERS, "", s) for s in answer]

# Sentencepice용 사전을 만들기 위해 question + answer를 저장해 둔다.
data_file = "./dataset/qa_data.txt"
with open(data_file, 'w', encoding='utf-8') as f:
    for sent in question + answer:
        f.write(sent + '\n')
        
# Google의 Sentencepiece를 이용해서 vocabulary를 생성한다.
# -----------------------------------------------------
# 참조 : https://github.com/google/sentencepiece
# https://github.com/google/sentencepiece/blob/master/python/sentencepiece_python_module_example.ipynb
#
# --input : one-sentence-per-line raw corpus file. No need to run tokenizer, 
#           normalizer or preprocessor. By default, SentencePiece normalizes 
#           the input with Unicode NFKC. You can pass a comma-separated list of 
#           files.
# --pad_id : padding ID
# --unk_id : unknown or oov ID. default = 0
# --bos_id : begin of sentence ID. default = 1
# --eod_id : end of sentence ID. default = 2
# --model_prefix : output model name prefix
# --vocab_size : vocabulary size
# --character_coverage : amount of characters covered by the model, good defaults 
#                        are: 0.9995 for languages with rich character set like 
#                        Japanse or Chinese and 1.0 for other languages with small 
#                        character set.
# --model_type : model type. Choose from unigram (default), bpe, char, or word. 
#                The input sentence must be pretokenized when using word type
templates= "--input={} \
            --pad_id=0 --pad_piece=<PAD>\
            --unk_id=1 --unk_piece=<UNK>\
            --bos_id=2 --bos_piece=<START>\
            --eos_id=3 --eos_piece=<END>\
            --model_prefix={} \
            --vocab_size={} \
            --character_coverage=1.0 \
            --model_type=unigram"

VOCAB_SIZE = 9000
model_prefix = "./dataset/qa_model"
params = templates.format(data_file, model_prefix, VOCAB_SIZE)

spm.SentencePieceTrainer.Train(params)
sp = spm.SentencePieceProcessor()
sp.Load(model_prefix + '.model')

with open(model_prefix + '.vocab', encoding='utf-8') as f:
    vocab = [doc.strip().split('\t') for doc in f]

word2idx = {k:v for v, [k, _] in enumerate(vocab)}
idx2word = {v:k for v, [k, _] in enumerate(vocab)}

# 학습 데이터를 생성한다. (인코더 입력용, 디코더 입력용, 디코더 출력용)
MAX_LEN = 15
enc_input = []
dec_input = []
dec_output = []

for Q, A in zip(question, answer):
    # Encoder 입력
    enc_i = [word2idx[k] for k in sp.encode_as_pieces(Q)]
    enc_input.append(enc_i)

    # Decoder 입력, 출력
    dec_i = [sp.bos_id()]   # <START>에서 시작함
    dec_o = []
    for ans in sp.encode_as_pieces(A):
        dec_i.append(word2idx[ans])
        dec_o.append(word2idx[ans])
    dec_o.append(sp.eos_id())   # Encoder 출력은 <END>로 끝남.        
    
    # dec_o는 <END>가 마지막에 들어있다. 나중에 pad_sequences()에서 <END>가
    # 잘려 나가지 않도록 MAX_LEN 위치에 <END>를 넣어준다.
    if len(dec_o) > MAX_LEN:
        dec_o[MAX_LEN] = sp.eos_id()
        
    dec_input.append(dec_i)
    dec_output.append(dec_o)

# 각 문장의 길이를 맞추고 남는 부분에 padding을 삽입한다.
enc_input = pad_sequences(enc_input, maxlen=MAX_LEN, value = sp.pad_id(), padding='post', truncating='post')
dec_input = pad_sequences(dec_input, maxlen=MAX_LEN, value = sp.pad_id(), padding='post', truncating='post')
dec_output = pad_sequences(dec_output, maxlen=MAX_LEN, value = sp.pad_id(), padding='post', truncating='post')
 
# 사전과 학습 데이터를 저장한다.
with open('./dataset/vocabulary.pickle', 'wb') as f:
    pickle.dump([word2idx, idx2word], f, pickle.HIGHEST_PROTOCOL)

with open('./dataset/train_data.pickle', 'wb') as f:
    pickle.dump([enc_input, dec_input, dec_output], f, pickle.HIGHEST_PROTOCOL)
