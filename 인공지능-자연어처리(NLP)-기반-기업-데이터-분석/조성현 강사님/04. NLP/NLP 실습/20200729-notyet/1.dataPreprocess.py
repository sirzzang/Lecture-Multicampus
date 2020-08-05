# 지역별 '건강보조식품 소매업' 데이터를 생성한다.
# ------------------------------------------
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import pickle

sido = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', 
        '서울', '세종', '울산', '인천', '전남', '전북', '제주', '충남', '충북']

target_clss = '건강보조식품 소매업'

# 데이터를 읽어온다
fullData = pd.read_csv('dataset/201901-202003.csv')

# 특정 지역의 STD_CLSS_NM를 filtering한다.
def sidoData(data, sido, clss):
    df = data[data['CARD_SIDO_NM'] == sido]
    df = df[df['STD_CLSS_NM'] == clss]
    
    df = df.drop('CARD_SIDO_NM', 1)
    df = df.drop('STD_CLSS_NM', 1)
    df = df.drop('CARD_CCG_NM', 1)
    df = df.drop('HOM_SIDO_NM', 1)
    df = df.drop('HOM_CCG_NM', 1)
    df = df.drop('CSTMR_CNT', 1)
    df = df.drop('CNT', 1)
    return df

# 지역별 target_clss (ex : '건강보조식품 소매업')의 매출 합계를 집계한다.
cnt = []
std_mean = []
for i, area in enumerate(sido):
    # 지역별 target_clss만 발췌한다.
    df = sidoData(fullData, area, target_clss)
    df = df.set_index('REG_YYMM')
    
    # 날짜별로 'AGE', 'SEX_CTGO_CD', 'FLC' 필드만 사용해 본다.
    # 다른 필드들도 고려해야 하지만 결측치 (NaN)가 많이 발생해서
    # 3개 필드만 선택했다.
    df = df.groupby(['REG_YYMM', 'AGE', 'SEX_CTGO_CD', 'FLC']).sum()
    df = df.unstack().unstack().unstack()
    df = pd.DataFrame(np.array(df))
    
    # 결측치를 모두 삭제했다. 일부 결측치를 남겨 두고
    # 아래 과정으로 채워 넣는 것이 좋다. 여기서는 일단 모두 삭제했다.
    df = df.dropna(axis=1)
    
    
#    imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
#    d = pd.DataFrame(imputer.fit_transform(df))
#
    # 지역별로 AMT를 표준화 하고, 향후 복원을 위해 std와 mean을 보관해 둔다.
    std = df.std()
    mean = df.mean()
    df = (df - mean) / std
    std_mean.append(np.array([std, mean]))
    d = np.array(df).T
    
    if i == 0:
        trainD = d
    else:
        trainD = np.vstack([trainD, d])
    
    cnt.append(d.shape[0])
    print('%d : %s 지역을 완료했습니다 (%d-개).' % (i + 1, area, cnt[-1]))
    
# 2019.01 ~ 2020.03 까지의 변화를 관찰한다.
# 9월 (추석), 1월 (설날) 명절 때 건강보조식품 소매업의 매출이 높음을 알 수 있다.
plt.figure(figsize=(12, 8))
plt.plot(trainD.T)
plt.show()

with open('dataset/1.data.pickle', 'wb') as f:
    pickle.dump([sido, cnt, std_mean, trainD], f, pickle.HIGHEST_PROTOCOL)

# 제출용 파일을
# 특정 지역의 STD_CLSS_NM를 filtering한다.
def sidoData1(data, sido, clss):
    df = data[data['CARD_SIDO_NM'] == sido]
    df = df[df['STD_CLSS_NM'] == clss]
    
    df = df.drop('CARD_SIDO_NM', 1)
    df = df.drop('STD_CLSS_NM', 1)
    df = df.drop('CARD_CCG_NM', 1)
    df = df.drop('HOM_SIDO_NM', 1)
    df = df.drop('HOM_CCG_NM', 1)
    df = df.drop('AGE', 1)
    df = df.drop('SEX_CTGO_CD', 1)
    df = df.drop('FLC', 1)
    df = df.drop('CSTMR_CNT', 1)
    df = df.drop('CNT', 1)
    return df

# 지역별 '건강보조식품 소매업'의 매출 합계를 집계한다.
for i, area in enumerate(sido):
    df = sidoData1(fullData, area, '건강보조식품 소매업')
    df = df.set_index('REG_YYMM')
    df = df.groupby(['REG_YYMM',]).sum()

    if i == 0:
        df_amt = df.groupby(['REG_YYMM',]).sum()
        df_amt.columns = [sido[i]]
    else:
        df_amt[sido[i]] = df.groupby(['REG_YYMM',]).sum()
        
    print('%d : %s 지역을 완료했습니다.' % (i + 1, area))
    
with open('dataset/1.sumission_data.pickle', 'wb') as f:
    pickle.dump(df_amt, f, pickle.HIGHEST_PROTOCOL)
    