# OHLCV 데이터에서 기술적 분석 지표들의 FeatureSet을 추출한다
# -------------------------------------------------------------
import pandas as pd
import numpy as np
from MyUtil.ComFeatureSet import getUpDnClass

# 과거 n-day 동안의 주가 패턴으로 Feature Set을 구성한다
def getPatternFeatureSet(data, u, d, nPast=20, nHop=3, nFuture=20, binary=False):
    # OHLCV 데이터에 class를 부여한다.
    df = getUpDnClass(data, up=u, dn=d, period=nFuture)
    
    # 학습 데이터를 구성한다.
    ds = getclosePatternWithClass(df, nPast, nHop = nHop)
    
    # Class는 0, 1, 2로 (multi-class) 측정되었는데, binary-classification을
    # 위해서는 주가 횡보인 class=0을 1로 대치하고, class = 1을 0으로, 2를 1로 변환한다.
    if binary:
#        ds.loc[ds['class'] == 0.0, 'class'] = 1.0
        ds = ds[ds['class'] != 0.0]
        ds['class'] -= 1.0
    return ds
    
# OHLCV 데이터에서 종가 (close)를 기준으로 과거 n-기간 동안의 Pattern을 구성한다
# nHop = 3 : 3기간씩 건너 뛰면서 pattern을 구성한다.
def getclosePattern(data, n, nHop = 3, normalize=True):
    loc = tuple(range(0, len(data) - n, nHop))
    
    # n개의 column을 가진 데이터프레임을 생성한다
    column = [str(e) for e in range(1, (n+1))]
    df = pd.DataFrame(columns=column)
    
    for i in loc:
        pt = data['close'].iloc[i:(i+n)].values
        
        if normalize:
            pt = (pt - pt.mean()) / pt.std()
        df = df.append(pd.DataFrame([pt],columns=column, index=[data.index[i+n]]), ignore_index=False)
        
    return df

# OHLCV + class 데이터에서 종가 (close)를 기준으로 과거 n-기간 동안의 Pattern을 구성한다
# nHop = 3 : 3기간씩 건너 뛰면서 pattern을 구성한다.
# 리턴 값 :
#           1         2         3  ...          20       vol  class
# 0  0.056859 -0.492078 -1.041017  ...    1.586034  0.187116    0.0
# 1  0.056859 -0.492078 -1.041017  ...    1.586034  0.187116    2.0
# 2  0.056859 -0.492078 -1.041017  ...    1.586034  0.187116    1.0
# ...
def getclosePatternWithClass(data, n, nHop = 3, normalize=True):
    # 패턴의 시작 지점을 확인해 둔다
    loc = tuple(range(0, len(data) - n, nHop))
    
    # 1~n의 column과 vol, class을 가진 데이터프레임을 생성한다
    column = np.array([str(e) for e in range(1, (n+1))])
    column = np.append(column, ['vol', 'class'])
    df = pd.DataFrame(columns=column)
    
    # 패턴 시작 지점부터 n-기간 동안의 종가, 변동성, class를 column으로 갖는 dataframe을 생성한다
    for i in loc:       
        # n-기간 동안의 종가 패턴
        closePat = np.array(data['close'].iloc[i:(i+n)])
        
        # n-기간의 마지막 데이터의 class
        classY = data['class'].iloc[i+n-1]
        
        # closePat의 표준편차를 계산한다.
        # 주가 수익률의 표준편차로 변동성을 측정하는 것이 일반적이나, 여기서는
        # 주가의 표준편차 / 평균 주가로 측정한다.
        vol = np.sqrt(n) * np.std(closePat) / np.mean(closePat)
        
        if normalize:
            closePat = (closePat - np.mean(closePat)) / np.std(closePat)
        
        # n-기간 동안의 종가, 변동성, class를 colume으로 dataframe을 생성한다. (1-row)
        closePat = np.append(closePat, [vol, classY])
        tmpdf = pd.DataFrame([closePat], columns=column)
        
        # 결과 dataframe인 df에 계속 추가한다 (row bind)
        df = df.append(tmpdf)
        
    return df
