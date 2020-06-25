# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:38:47 2020

@author: sir95
"""


# module import 
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# load data
# 출처: https://archive.ics.uci.edu/ml/datasets/online+retail
retail = pd.read_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/OnlineRetail.csv')

# France Data: data too big...
retail_france = retail[retail['Country'] == 'France']

# 전처리
retail_france['Description'] = retail_france['Description'].str.strip()
retail_france.dropna(subset=['InvoiceNo'], axis=0, inplace=True)
retail_france = retail_france[~retail_france['InvoiceNo'].str.contains('C')]
retail_france['InvoiceNo'] = retail_france['InvoiceNo'].astype('str')

# group by InvoiceNo
retail_france_grps = retail_france.groupby(['InvoiceNo', 'Description'])['Quantity'].sum()
retail_france_grps = retail_france_grps.unstack()
retail_france_grps = retail_france_grps.fillna(0)
retail_france_grps = retail_france_grps.reset_index()
retail_france_grps = retail_france_grps.set_index('InvoiceNo')

# Quantity가 1보다 크면 무조건 1로 바꾸기
retail_france_grps[retail_france_grps <= 0] = 0
retail_france_grps[retail_france_grps >= 1] = 1

# apriori 알고리즘 적용
frequent_itemsets = apriori(retail_france_grps, min_support=0.05, use_colnames=True)

# 연관규칙
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)
rules = rules.sort_values(by=['lift'], axis=0, ascending=False)
rules[['antecedents', 'consequents']] = rules[['antecedents', 'consequents']].applymap(lambda x: tuple(x))

# 결과 파일 저장
rules.to_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/OnlineRetail_result.csv', index=False)
