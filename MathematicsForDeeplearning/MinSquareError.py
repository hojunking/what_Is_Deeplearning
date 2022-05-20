import numpy as np
#MSE (Min Square Error) 평균 제곱 오차

# np배열에 데이터 넣기
x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

#임의의 기울기 a, y절편 b 설정햣 ㄴㅅㅁ
fake_a = 3
fake_b = 76

#결과 배열 초기화
predicted_result =[]

#predicted_value 구하기
def predict(x):
    return fake_a * x + fake_b
#배열 길이
n = len(x)

for i in range(n):
    predictValue = predict(x[i])
    predicted_result.append(predictValue)
    print("공부시간 =%.f , 실제점수 = %.f, 예측점수 = %.f "%
          (x[i], y[i], predicted_result[i]))

def MSE(y, y_pred):
    return (1/n)*sum((y - y_pred)**2)

#평균 제곱 오차 값 (MSE)
#배열 , 배열을 넣으면 자동 반복문처리 해준다!!
print("평균 제곱 오차 : " + str(MSE(y,predicted_result)))    