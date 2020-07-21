# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 06:41:06 2020

@author: sir95
"""


# module import
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# load data
df = pd.read_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/MarketBasket.csv',
                 header=None)
df.info()

# change data to list
dataset = []
for i, row in df.iterrows(): 
    # print(i, row)
    dataset.append([x for x in list(row) if str(x) != 'nan']) # row를 list로 받은 후, nan을 제거.

# item sparse matrix
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
market_basket_df = pd.DataFrame(te_ary, columns=te.columns_)

# apriori model
frequent_itemsets = apriori(market_basket_df, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=0.1)

# lift 큰 순서대로 sort
rules= rules.sort_values(by=['lift'], axis=0, ascending=False)
print(rules)

# frozenset to tuple
cols = ['antecedents', 'consequents']
rules[cols] = rules[cols].applymap(lambda x: tuple(x)) # 튜플 변환 과정?


# 결과 파일 저장
# rules.to_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/MarketBasket_result.csv', index=False)


############## without frozen ###################

# load data
df = pd.read_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/MarketBasket.csv',
                 header=None)
df.info()

# change data to list
dataset = []
for i, row in df.iterrows(): 
    dataset.append([x for x in list(row) if str(x) != 'nan']) # row를 list로 받은 후, nan을 제거.

# item sparse matrix
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
market_basket_df = pd.DataFrame(te_ary, columns=te.columns_)

# apriori model
frequent_itemsets = apriori(market_basket_df, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=0.1)

# lift 큰 순서대로 sort
rules= rules.sort_values(by=['lift'], axis=0, ascending=False)
print(rules)


# 결과 파일 저장
rules.to_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/MarketBasket_result_woFrozen.csv', index=False)
