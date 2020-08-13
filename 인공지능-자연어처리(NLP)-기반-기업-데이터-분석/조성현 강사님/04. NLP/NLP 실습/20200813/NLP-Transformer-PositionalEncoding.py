# https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/text/transformer.ipynb
import numpy as np

def get_angles(pos, i, d_model):
    angle_rates = 1 / np.power(10000, (2 * (i // 2)) / np.float32(d_model))
    return pos * angle_rates

def positional_encoding(position, d_model):
    angle_rads = get_angles(np.arange(position)[:, np.newaxis],
                            np.arange(d_model)[np.newaxis, :],
                            d_model)

    # apply sin to even indices in the array; 2i
    sines = np.sin(angle_rads[:, 0::2])    
    # apply cos to odd indices in the array; 2i+1
    cosines = np.cos(angle_rads[:, 1::2])
    
    pos_encoding = np.concatenate([sines, cosines], axis=-1)

    return pos_encoding
    
PE = positional_encoding(5, 6)
PE.round(3)

from sklearn.metrics.pairwise import euclidean_distances

for i in range(PE.shape[0] - 1):
    d = euclidean_distances(PE[i].reshape(1,-1), PE[i+1].reshape(1,-1))
    norm = np.linalg.norm(PE[i])
    dot = np.dot(PE[i], PE[i+1])
    print("%d - %d : distance = %.4f, norm = %.4f, dot = %.4f" % (i, i+1, d[0,0], norm, dot))


import matplotlib.pyplot as plt

PE = positional_encoding(5, 2) # 6차원 그림 못 그리므로, 임베딩 사이즈(dmodel)를 2차원으로 준다.
plt.figure(figsize=(8, 8))
plt.plot(PE[:, 0], PE[:, 1], marker='o')
plt.show()