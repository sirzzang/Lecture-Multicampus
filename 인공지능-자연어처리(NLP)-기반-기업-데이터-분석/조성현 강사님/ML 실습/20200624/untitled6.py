# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:31:03 2020

@author: sir95
"""

# module import
import numpy as np
import tensorflow as tf

# 4x4 matrix
a = np.array([[1,2,3,4],\
              [4,5,6,7],\
              [1,2,3,4],\
              [4,5,6,7]])

# 손으로 짜보기 1
answer1 = np.zeros(16).reshape(4, 4)
for row in range(a.shape[0]):
    for col in range(a.shape[1]):
        print(f"{row}행 * {col}열")
        print(f"{a[row, :]} x {a[:, col]}")
        answer1[row, col] = np.dot(a[row, :], a[:, col].T)
print(answer1)

print('')

# 손으로 짜보기 2
answer2 = np.zeros(16).reshape(4, 4)
for row in range(a.shape[0]):
    for col in range(a.shape[1]):
        print(f"{row}행 * {col}열")
        for i in range(4):
            answer2[row][col] += (a[row][i] * a[i][col])
        print(f"계산 결과: {answer2[row][col]}")
print(answer2)

# check answer
print(np.dot(a, a))

# 강사님 정답
c = np.zeros(a.shape) # 한 번에 이렇게 하면 된다.
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[0]):
            c[i, j] += (a[i, k] * a[k, j])
print(c)