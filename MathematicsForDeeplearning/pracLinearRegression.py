import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

model = Sequential()

model.add(Dense(1,input_dim = 1, activation = 'linear'))
model.complie(optimizer = 'sgd', loss = 'mse')
# loss function
# 평균 제곱 오차 : min square error
