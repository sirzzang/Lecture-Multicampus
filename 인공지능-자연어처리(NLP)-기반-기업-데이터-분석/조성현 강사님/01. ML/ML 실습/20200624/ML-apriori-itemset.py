# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 06:34:12 2020

@author: sir95
"""

# module import
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Market Basket Transaction data 
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'], \
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'], \
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'], \
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'], \
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]
print(dataset)

# item sparse matrix
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
print(te_ary)
df = pd.DataFrame(te_ary, columns=te.columns_)

# apriori model
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print(frequent_itemsets)

# association rules
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=0.7)
print(rules)
rules.loc[:, ('antecedents', 'consequents', 'support', 'confidence', 'lift')]

