
# 주가 데이터 수집 관련 함수를 정의한다
#
# 한국생산성본부 금융 빅데이터 전문가 과정 (금융 모델링 파트) 실습용 코드
# Written : 2018.2.5
# 제작 : 조성현
# -----------------------------------------------------------------
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime as dt

# Yahoo site로 부터 대형주 종목 데이터를 수집하여 파일에 저장한다.
# Yahoo site로 부터 주가 데이터를 수집한다. 가끔 안들어올 때가 있어서 10번 시도한다.
# 수정 주가로 환산하여 읽어온다
def getStockDataYahoo(stockCode, start='', end=''):
    # 수집 기간
    if start == '':
        start = dt.datetime(2007, 1, 1)
    else:
        start = dt.datetime.strptime(start, '%Y-%m-%d')
    
    if end == '':
        end = dt.date.today()
    else:
        end = dt.datetime.strptime(end, '%Y-%m-%d')
    
    stock = pd.DataFrame()
    for i in range(0, 10):
        try:
            stock = web.YahooDailyReader(stockCode, start, end, adjust_price=True).read()
        except:
            print("%s not collected (%d)" % (stockCode, i + 1))
            
        if not stock.empty:
            break
        
    if stock.empty:
        print("%s not collected" % stockCode)
    
    # 수정주가 비율은 이미 적용되었으므로 제거한다
    stock = stock.drop('Adj_Ratio', 1)
    
    # Volume이 0 인 경우가 있으므로, 이를 제거한다 
    stock = stock.drop(stock[stock.Volume < 10].index)
    
    # 데이터에 NA 값이 있으면 제거한다
    stock = stock.dropna()
    
    # 수집한 데이터를 파일에 저장한다.
    stock.to_csv('StockData/' + stockCode[0:6] + '.csv', date_format='%Y-%m-%d')
    print ("%s 데이터를 수집하였습니다. (rows = %d)" % (stockCode, len(stock)))
    return stock

def getStockDataList(stockList, start='', end=''):
    for code in stockList.keys():
        getStockDataYahoo(code + '.KS', start=start, end=end)
        
# 일일 데이터를 주간 (Weekly), 혹은 월간 (Monthly)으로 변환한다
def myAgg(x):
    names = {
            'Open' : x['Open'].head(1),
            'High' : x['High'].max(),
            'Low' : x['Low'].min(),
            'Close' : x['Close'].tail(1),
            'Volume' : x['Volume'].mean()}
    return pd.Series(names, index=['Open', 'High', 'Low', 'Close', 'Volume'])

def getWeekMonthOHLC(x, type='Week'):
    if type == 'Week':
        rtn = x.resample('W-Fri').apply(myAgg)
    elif type == 'Month':
        rtn = x.resample('M').apply(myAgg)
    else:
        print("invalid type in getWeekMonthOHLC()")
        return
    rtn = rtn.dropna()
    rtn = rtn.apply(pd.to_numeric)
    return rtn
