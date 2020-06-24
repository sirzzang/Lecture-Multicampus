# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 06:05:42 2020

@author: sir95
"""

# module import
from sklearn.ensemble import IsolationForest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix


# load data
credit = pd.read_csv('C:/Users/sir95/Desktop/LECTURE/인공지능-자연어처리(NLP)-기반-기업-데이터-분석/조성현 강사님/ML 실습/dataset/creditcard_fraud.csv')

# check data
credit.info()
credit.Class.value_counts()
credit.Amount

# visualize transactions: Time
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
ax1.hist(credit['Time'][credit['Class'] == 0], bins=50)
ax2.hist(credit['Time'][credit['Class'] == 1], bins=50)
plt.xlabel('Transactions')
ax1.set_title('Normal Use')
ax2.set_title('Abnormal Use')
plt.show()

# visualize transactions: Amount
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
ax1.hist(credit['Amount'][credit['Class'] == 0], bins=50)
ax2.hist(credit['Amount'][credit['Class'] == 1], bins=50)
# ax1.set_yscale('log')
# ax2.set_yscale('log')
ax1.set_title('Normal Use')
ax2.set_title('Abnormal Use')
plt.show()


# check according to features
def visualize_Features(df, feature):
    sns.distplot(df[feature][df['Class'] == 0], bins=50)
    sns.distplot(df[feature][df['Class'] == 1], bins=50)
    plt.legend(['Normal', 'Abnormal'], loc='best')
    plt.title(feature + ' distribution')
    plt.show()
    
features = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', \
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', \
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']

for feature in features:
    visualize_Features(credit, feature)

# prepare data
credit = np.array(credit)
X_train = credit[:, :-1]
y_train = credit[:, -1]

# check fraud samples
normal = (y_train == 0).sum()
fraud = (y_train == 1).sum()
print('===== 정상 사례 =====', normal)
print('===== 비정상 사례 =====', fraud)
print('===== 비정상 사례 비율 ===== %.4f' %(100*(fraud/normal)))

# train iForest model
model = IsolationForest(n_estimators=100)
model.fit(X_train)

# check anomaly score
score = abs(model.score_samples(X_train))

# visualize
plt.hist(score, bins=50)
plt.show()

# decision: anomaly 1에 가까우면 이상 판정
y_pred = (score > 0.65).astype(int) # 판정 기준!
fraud_count = (y_pred == 1).sum()
print('')
print(' =========== 이상 데이터로 판정한 개수 ============', fraud_count)

# confusion matrix
cm = confusion_matrix(y_train, y_pred) # row: actual, col: pred.
cm_df = pd.DataFrame(cm)
cm_df.columns = ['pred_normal', 'pred_fraud']
cm_df.index = ['actual_normal', 'actual_fraud']
print('')
print(cm_df)

# precision, recall
print('')
print('비정상으로 판정한 것 중')
print(f'     정상 데이터를 비정상으로 판정한 비율 = {round(cm[0, 1] / cm[:, 1].sum(), 4)}')
print(f'     비정상 데이터를 비정상으로 판정한 비율 = {round(cm[1, 1] / cm[:, 1].sum(), 4)}')


# 기존 코드: print('     정상 데이터를 비정상으로 판정한 비율 = %.4f' % cm[0, 1] / cm[:, 1].sum())
# TypeError: ufunc 'true_divide' not supported for the input types, 
# and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
print(cm)
print(type(cm))
print(cm[0, 1])
print(type(cm[0, 1]))

print(cm[:, 1])
print(cm[:, 1].sum())
print(type(cm[:, 1].sum()))

