#미분 -> 순간기울기 -> 최솟값은 기울기가 0이 되는 지점
#기울기가 0인 지점을 도달하기 위한 판단 -> 경사하강법(gradient decent)

import numpy as np
import matplotlib.pyplot as plt #matplotlib lib

x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

#데이터 분포를 그래프로 나타낸다
# plt.scatter(x,y)
# plt.show()

#기울기 a의 값과 절편 b의 값을 초기화
a = 0
b = 0

#학습률 초기화
lr = 0.03

#반복횟수 초기화
epochs = 2001

#x의 갯수 (4)
n = len(x)

# 경사하강법(gradient decent)
for i in range(epochs):
    y_pred = a * x +b  # 예측값 구하기
    error = y - y_pred # 실제 값과 비교한 오차 error 처리
    
    # 오차 함수에 대한 미분
    a_diff = (2/n) * sum(-x * (error))
    b_diff = (2/n) * sum(-(error))
    
    a = a -lr * a_diff #학습률을 곱해 기존 기울기 a값 업뎃
    b = b -lr * b_diff #학습율 곱해 기존 y절편값 업뎃
    
    if i % 100 == 0 :#100단위로 출력
        print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))

# 다음 반복을 통해 최종 기울기 a와 y절편을 통해 그래프 그리기
y_pred = a * x + b

#그래프 출력
plt.scatter(x,y)
plt.plot(x,y_pred, 'r')
plt.show()


