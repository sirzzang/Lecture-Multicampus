# 시계열분석 관련 함수를 정의한다
#
# 한국생산성본부 금융 빅데이터 전문가 과정 (금융 모델링 파트) 실습용 코드
# Written : 2018.2.5
# 제작 : 조성현
# -----------------------------------------------------------------
import numpy as np
import scipy.stats as stats
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

# ARIMA(ar, d, ma) 모형으로 n개의 데이터를 샘플링한다
def sampleARIMA(ar, d, ma, n):
    arparams = np.array(ar)
    maparams = np.array(ma)
    ar = np.r_[1.0, -arparams] # add zero-lag and negate
    ma = np.r_[1.0, maparams]  # add zero-lag
    
    # ARMA 모형으로 n개의 데이터를 샘플링한다
    y = arma_generate_sample(ar, ma, n)
    
    # 지정된 차분 횟수 (d) 만큼 누적한다
    for i in np.arange(d):
        y = np.cumsum(y)

    return y

# 시계열 데이터의 정규성을 확인한다
def checkNormality(data):
    fig = plt.figure(figsize=(10, 8))
    p1 = fig.add_subplot(2,2,1)
    p2 = fig.add_subplot(2,2,2)
    p3 = fig.add_subplot(2,2,3)
    p4 = fig.add_subplot(2,2,4)
    
    p1.plot(data)  # 육안으로 백색 잡음 형태인지 확인한다
    p1.set_title("Data")
    
    # Residual의 분포를 육안으로 확인한다
    r = np.copy(data)
    r.sort()
    pdf = stats.norm.pdf(r, np.mean(r), np.std(r))
    p2.plot(r,pdf)
    p2.hist(r, density=True, bins=100)
    p2.set_title("Distribution")
    
    # Q-Q plot을 그린다
    stats.probplot(data, dist="norm", plot=p3)
    
    # ACF plot을 확인한다. 백색 잡음은 자기상관성이 없다.
    plot_acf(data, lags=100, ax=p4)
    
    # Shapiro-Wilks 검정을 수행한다
    # (검정통계량, p-value)가 출력된다.
    # 귀무가설 : 정규분포 이다, 대립가설 : 아니다
    # p-value > 0.05 이면 귀무가설을 기각할 수 없다 --> "정규분포이다"
    w = stats.shapiro(data)
    print()
    print("Shapiro-Wilks 검정 : 검정통계량 = %.4f, p-value = %.4f" % (w[0], w[1]))