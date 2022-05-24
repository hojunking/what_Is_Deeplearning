from matplotlib.transforms import Bbox
import numpy as np
import matplotlib.pyplot as plt
from pyrsistent import b

#독립변수 1 : 공부시간 x1, 독립변수 2 : 과외시간 x2, 종속변수 : 성적 y
#numpy array 선언

x1 = np.array([2, 4, 6, 8])
x2 = np.array([0, 4, 2, 3])
y = np.array([81, 93, 91, 97])

# 데이터 분포 3D그래프
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter3D(x1,x2,y)
#plt.show()

# 기울기 a1,a2와 y절편 b
a1 = 0
a2 = 0
b = 0

#학습률 초기화
lr = 0.01

#반복횟수
epoch = 2001

# x1,x2의 길이(횟수)
n = len(x1)

#start Gradient Decent // pred -> 예측값
for i in range(epoch):
    y_pred = a1 * x1 + a2 * x2 + b
    error = y - y_pred
    
    #오차 함수미분
    a1_diff =(2/n) * sum(-x1 * (error))
    a2_diff =(2/n) * sum(-x2 * (error))
    b_diff = (2/n) * sum(-(error))
    
    # 학습률 곱
    a1 = a1 - a1_diff * lr
    a2 = a2 - a2_diff * lr
    b = b - b_diff * lr
    
    # 100 단위로 출력
    if i % 100 == 0 :
        print("epoch=%.f, 기울기1=%.04f, 기울기2=%.04f, 절편=%.04f" % (i, a1, a2, b))
    
ax.scatter3D(x1,x2,y_pred)
plt.show()

#실재 성적과 예상점수
print("실재 점수 = ",y)
print("예상 점수 = ",y_pred)