from gensim.models.doc2vec import Doc2Vec, TaggedDocument

samples = ['너 오늘 이뻐 보인다',
           '나는 오늘 기분이 더러워',
           '끝내주는데, 좋은 일이 있나봐',
           '나 좋은 일이 생겼어',
           '아 오늘 진짜 짜증나',
           '환상적인데, 정말 좋은거 같아']

sentences = [s.split() for s in samples]

# 문장마다 paragraph ID 를 붙인다.
documents = [TaggedDocument(doc, [f'd{i}']) \
             for i, doc in enumerate(sentences)]

    

# PV-DM 모델을 생성한다.
model = Doc2Vec(size = 5, alpha = 0.025, min_alpha=0.00025, min_count=1, dm = 1)

# PV-DM 모델을 학습한다.
model.build_vocab(documents)
model.train(documents, total_examples = len(samples), epochs = 100)

# Word vector를 확인해 본다.
model.wv['오늘']

# Paragraph vector를 확인해 본다.
model.docvecs[0]

# 전체 문장에 대한 paragraph vector를 확인해 본다.
model.docvecs.vectors_docs

# 새로운 문장에 대한 PV를 inference 한다.
model.infer_vector("오늘 좋은 일이 있을 것 같아".split())

