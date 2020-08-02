# Labeling for supervised learning
# 
# 1. returnLabel() - 주어진 period 동안의 수익률이 upper bound를 touch 하면 "BUY", lower bound를 touch하면 "SELL", 아니면 "HOLD"
# 2. barrierLabel() - 주어진 period 동안 upper bound를 touch 하면 "BUY", lower bound를 touch하면 "SELL", 아니면 "HOLD"
# 3. tradeLabeling() - 주어진 window 크기에 대해 시계열 데이터의 저점에서 매수 (Buy)하고, 고점에서 매도 (Sell)하는 action을 찾는다
# 3-1. calculateRtn() - tradeLabeling() 함수가 결정한 action sequence를 따를 때의 누적 수익률을 계산한다
# 3-2. optimizeLabel() - 누적 수익률이 최대가 되는 window size를 결정한다. optimal tradeLabeling을 결정함.
# 3-2. neighborAction() - optimal labelel에 대해 분할 매수, 분할 매도를 적용한다.
#
# 2018.12.03, 아마추어퀀트 (조성현)
# ----------------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd

HOLD = 0
BUY = 1
SELL = 2
sAction = ['HOLD', 'BUY', 'SELL']

# Algorithm #1 : Fixed period return Labeling for supervised learning.
def returnLabel(df, upper=1, lower=-1, period=5):
    # 현재 주가와 period 이후 시점의 주가와의 수익률을 측정한다. 
    df['rtn'] = np.log(df['close'].shift(-period)) - np.log(df['close'])
    df = df.dropna()

    # 목표 수익률과 손절률을 계산한다
    s = df['rtn'].std() # n-기간 변동성
    uLimit = df['rtn'].mean() + upper * s
    dLimit = df['rtn'].mean() + lower * s
    
    # label을 부여한다
    rtn = np.array(df['rtn'])
    
    df2 = df.copy()  # 자꾸 SettingWithCopyWarning: 이 발생해서 copy해서 사용
    df2['label'] = HOLD
    df2.loc[np.where(rtn > uLimit)[0], 'label'] = BUY
    df2.loc[np.where(rtn < dLimit)[0], 'label'] = SELL
    return df2
    
# Algorithm #2 : Barrier Labeling for supervised learning.
#
# 종목마다 변동성이 다르므로 목표 수익률을 "변동성의 몇 배"로 정의한다.
# ex : up = 0.5 이면 변동성의 +0.5 배.
# up : 목표 수익률 표준편차 배수
# dn : 손절률 표준편차 배수
# period : holding 기간
# return : 0 - 주가 횡보, 1 - 주가 하락, 2 - 주가 상승
# --------------------------------------------------------------
def barrierLabel(df, upper=1, lower=-1, period=20):
    # 주가 수익률의 표준편차를 측정한다. 컬럼 이름은 label 이라고 임시로 부여해 놓는다.
    # 수익률 표준편차 (변동성)는 목표 수익률과 손절률을 계산하기 위해 임시로 사용된다.
    df['label'] = np.log(df['close']) - np.log(df['close'].shift(1))
    s = np.std(df['label'])

    # 목표 수익률과 손절률을 계산한다
    uLimit = upper * s * np.sqrt(period)
    dLimit = lower * s * np.sqrt(period)
    
    # 가상 Trading을 통해 미래 주가 방향에 대한 Class를 결정한다. class에는 원래 수익률이 기록되어 있었으나 NaN을 기록해 둔다
    df['label'] = np.nan
    for i in range(len(df)-period):
        buyPrc = df.iloc[i].close     # 매수 포지션을 취한다
        y = np.nan
            
        # 매수 포지션 이후 청산 지점을 결정한다
        duration = 0    # 보유 기간
        for k in range(i+1, len(df)):
            sellPrc = df.iloc[k].close
            rtn = np.log(sellPrc / buyPrc)  # 수익률을 계산한다
#            rtn = (sellPrc - buyPrc) / buyPrc
            
            # 목표 수익률이나 손절률에 도달하면 루프를 종료한다
            if duration > period:
                y = HOLD           # hoding 기간 동안 목표 수익률이나 손절률에 도달하지 못했음. 주가가 횡보한 것임.
                break
            else:
                if rtn > uLimit:
                    y = BUY       # 수익
                    break
                elif rtn < dLimit:
                    y = SELL       # 손실
                    break
            duration += 1
        df.loc[i, 'label'] = y     # label 컬럼에 y를 기록한다.
    df = df.dropna()    # 마지막 부분은 label을 결정하지 못해 NaN이 기록되어 있으므로 이를 제거한다.
    return df

# --------------------------------------------------------------------------------------------------------------------------
# Algorithm #3 : Action Labeling for supervised learning.
# 
# 1. tradeLabeling() - 주어진 window 크기에 대해 시계열 데이터의 저점에서 매수 (Buy)하고, 고점에서 매도 (Sell)하는 action을 찾는다
# 2. calculateRtn() - tradeLabeling() 함수가 결정한 action sequence를 따를 때의 누적 수익률을 계산한다
# 3. optimizeLabel() - 누적 수익률이 최대가 되는 window size를 결정한다. optimal tradeLabeling을 결정함.
# 4. neighborAction() - optimal labelel에 대해 분할 매수, 분할 매도를 적용한다.
# --------------------------------------------------------------------------------------------------------------------------

# 주어진 window 크기에 대해 시계열 데이터의 저점에서 매수 (Buy)하고, 고점에서 매도 (Sell)하는 action sequence를 찾는다
def tradeLabeling(data, nWindow):
    nPtr = 0
    nDays = data.shape[0]
    action = np.repeat(HOLD, nDays)
    while nPtr < nDays:
        if nPtr > nWindow:
            idxBegin = nPtr - nWindow
            idxEnd = idxBegin + nWindow - 1
            midIndex = int((idxBegin + idxEnd) / 2)
            
            prcMin = 99999999999
            prcMax = 0
            for i in np.arange(idxBegin, (idxEnd + 1)):
                price = data[i]
                if price < prcMin:
                    prcMin = price
                    minIdx = i
                if price > prcMax:
                    prcMax = price
                    maxIdx = i
            if maxIdx == midIndex:
                action[maxIdx] = SELL
            if minIdx == midIndex:
                action[minIdx] = BUY
        nPtr += 1
    
    # 중첩된 action을 제거한다. [BUY - BUY] --> [HOLD - BUY] or [BUY - HOLD]
    n = 0
    for i in np.where(action != HOLD)[0]:
        n += 1
        if n == 1:
            prevIdx = i
            prevAct = action[i]
            prevPrc = data[i]
            continue
        
        if prevAct == BUY and action[i] == BUY:
            # 둘 중 높은 가격 지점은 HOLD로 바꿔준다
            if prevPrc > data[i]:
                action[prevIdx] = HOLD
            else:
                action[i] = HOLD
            
        if prevAct == SELL and action[i] == SELL:
            # 둘 중 낮은 가격 지점은 HOLD로 바꿔준다
            if prevPrc < data[i]:
                action[prevIdx] = HOLD
            else:
                action[i] = HOLD

        if action[i] != HOLD:
            prevIdx = i
            prevAct = action[i]
            prevPrc = data[i]
    return action

# tradeLabeling() 함수가 결정한 action sequence를 따를 때의 누적 수익률을 계산한다
def calculateRtn(data, action):
    profit = 0.0
    nTrade = 0
    n = 0
    for i in np.where(action != HOLD)[0]:
        n += 1
        if n == 1:
            prevAct = action[i]
            prevPrc = data[i]
            continue
        
        if prevAct == BUY and action[i] == SELL:
            profit += 100 * np.log(data[i] / prevPrc) - 5.0
            nTrade += 1
            n = 0
        if prevAct == SELL and action[i] == BUY:
            profit += 100 * np.log(prevPrc / data[i]) - 5.0
            nTrade += 1
            n = 0
            
    return profit, nTrade

# 누적 수익률이 최대가 되는 window size를 결정한다. optimal tradeLabeling을 결정한다.
def optimizeLabel(data, verbose=False):
    trajProfit = []
    maxProfit = 0
    maxWindow = 0
    maxAction = []
    maxTrade = 0
    for i in np.arange(10, int(len(data) / 60)):
        action = tradeLabeling(data, i)
        profit, nTrade = calculateRtn(data, action)
        if profit > maxProfit:
            maxProfit = profit
            maxWindow = i
            maxAction = np.copy(action)
            maxTrade = nTrade
        trajProfit.append(profit)
        if verbose == True:
            print("nWindow = %d, profit = %.4f (%s)" % (i, profit, '%'))
    return maxWindow, maxProfit, maxTrade, maxAction, trajProfit

# optimal labelel에 대해 분할 매수, 분할 매도를 적용한다.
def neighborAction(action, neighbor=1):
    # action 전,후를 동일하게 만든다. [HOLD - BUY - HOLD] --> [BUY - BUY - BUY]
    # 특정 지점이 아닌 부근에서 매수하거나 매도하는 것으로..
    for i in np.arange(0, neighbor):
        loc = np.where(action == BUY)[0]
        action[loc - 1] = BUY
        action[loc + 1] = BUY
        
        loc = np.where(action == SELL)[0]
        action[loc - 1] = SELL
        action[loc + 1] = SELL
    return action

def tradeLabel(df, window=20, optimize=True, neighbor=1, verbose=False):
    data = np.array(df['close'])
    if optimize == True:
        nWindow, profit, trade, action, trajProfit = optimizeLabel(data, verbose=verbose)
        if neighbor > 0:
            action = neighborAction(action, neighbor)
    else:
        action = tradeLabeling(data, window)
        if neighbor > 0:
            action = neighborAction(action, neighbor)
    
    df['label'] = pd.DataFrame(action)
    return df, trajProfit

