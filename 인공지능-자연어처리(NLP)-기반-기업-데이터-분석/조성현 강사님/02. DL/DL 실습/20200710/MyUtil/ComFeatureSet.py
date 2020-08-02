import numpy as np

# Supervised Learning을 위한 class를 부여한다
# 종목마다 변동성이 다르므로 목표 수익률을 "변동성의 몇 배"로 정의한다.
# ex : up = 0.5 이면 변동성의 +0.5 배.
# up : 목표 수익률 표준편차 배수
# dn : 손절률 표준편차 배수
# period : holding 기간
# return : 0 - 주가 횡보, 1 - 주가 하락, 2 - 주가 상승
# --------------------------------------------------------------
def getUpDnClass(data, up=1, dn=-1, period=20):
    # 주가 수익률의 표준편차를 측정한다. 컬럼 이름은 class라고 부여해 놓는다.
    # 수익률 표준편차 (변동성)는 목표 수익률과 손절률을 계산하기 위해 임시로 사용된다.
    data['class'] = np.log(data['close']) - np.log(data['close'].shift(1))
    s = np.std(data['class'])

    # 목표 수익률과 손절률을 계산한다
    uLimit = up * s * np.sqrt(period)
    dLimit = dn * s * np.sqrt(period)
    
    # 가상 Trading을 통해 미래 주가 방향에 대한 Class를 결정한다. class에는 원래 수익률이 기록되어 있었으나 NaN을 기록해 둔다
    data['class'] = np.nan
    for i in range(len(data)-period):
        buyPrc = data.iloc[i].close     # 매수 포지션을 취한다
        y = np.nan
            
        # 매수 포지션 이후 청산 지점을 결정한다
        duration = 0    # 보유 기간
        for k in range(i+1, len(data)):
            sellPrc = data.iloc[k].close
            #rtn = np.log(sellPrc / buyPrc)  # 수익률을 계산한다
            rtn = (sellPrc - buyPrc) / buyPrc
            
            # 목표 수익률이나 손절률에 도달하면 루프를 종료한다
            if duration > period:
                y = 0           # hoding 기간 동안 목표 수익률이나 손절률에 도달하지 못했음. 주가가 횡보한 것임.
                break
            else:
                if rtn > uLimit:
                    y = 2       # 수익
                    break
                elif rtn < dLimit:
                    y = 1       # 손실
                    break
            duration += 1
        data.iloc[i, 5] = y     # class 컬럼에 y를 기록한다.
    data = data.dropna()    # 마지막 부분은 class를 결정하지 못해 NaN이 기록되어 있으므로 이를 제거한다.
    return data
