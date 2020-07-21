# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:29:38 2020

@author: sir95
"""


# module import
import pandas as pd
import random

# load data
retail = pd.read_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/OnlineRetail(small).csv')

# check data
retail.info()
retail.head(10)

# InvoiceNo to str.
retail['InvoiceNo'] = retail['InvoiceNo'].astype('str')
retail.info() # 변환 확인

# group by InvoiceNo
retail_grps = retail.groupby(['InvoiceNo', 'StockCode'])['Quantity'].sum()
display(retail_grps)

# pivot
retail_pivot = retail_grps.unstack()
display(retail_pivot)

# NaN to 0
retail_pivot = retail_pivot.fillna(0)

# set index : 순서 주의
retail_pivot = retail_pivot.reset_index()
retail_pivot = retail_pivot.set_index('InvoiceNo')

# 랜덤하게 구매목록 확인
sample_idx = random.choice(retail_pivot.index)
print(retail_pivot.loc[sample_idx])
