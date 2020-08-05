# 지역별 '건강보조식품 소매업' 매출을 예측한다
# -------------------------------------------
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import pickle

# 본 데이터를 읽어서 다음 달 매출을 예측한다.
with open('dataset/1.data.pickle', 'rb') as f:
    sido, cnt, std_mean, realData = pickle.load(f)

# 학습 모델을 읽어온다.
model = load_model('dataset/3.model.h5')

# 지역별 '건강보조식품 소매업' 매출을 예측한다.
pred_amt = []
n_start = 0
for i, area in enumerate(sido):
    n_end = n_start + cnt[i]
    predData = realData[n_start:n_end, -12:]
    predData = predData[:, :, np.newaxis]
    predY = model.predict(predData)
    n_start = n_end
    
    amt = predY[:, -1] * std_mean[i][0] + std_mean[i][1]
    pred_amt.append(np.sum(amt))
    print("%s : %d" % (sido[i], pred_amt[-1]))
    
# 원 데이터뒤에 예측 결과를 붙여 넣고, 육안으로 결과를 확인한다.
with open('dataset/1.sumission_data.pickle', 'rb') as f:
    df_amt = pickle.load(f)
    
# 원 데이터 뒤에 예측 결과를 붙여 넣는다.
pred_amt = np.vstack([np.array(df_amt), np.array(pred_amt)])

# 결과를 육안으로 확인한다.
plt.figure(figsize=(12, 8))
plt.plot(pred_amt, marker='o')
plt.axvline(x=14, linestyle='dashed')
plt.show()