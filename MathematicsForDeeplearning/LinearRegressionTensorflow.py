import numpy as np
import matplotlib.pyplot as plt

# Sequential Model, layers from tensorflow keras
# 선형모델은 1:1 input : output 모델
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

# Sequential model 초기화
model = Sequential()

# H(x) (model) = wx + b (hypothesis = weight*x + bias)
# model.add(출력값, 입력변수, 분석방법 = 선형(linear))
model.add(Dense(1, input_dim =1, activation='linear'))

# 오차 수정을 위한 Optimizer => 경사하강법(Gradient Decent) - 'sgd'
# 오차 정도의 판단 Loss Function => 평균 제곱 오차(Min Square Error) - 'mse'
model.complie(optimizer='sgd', loss='mse')


