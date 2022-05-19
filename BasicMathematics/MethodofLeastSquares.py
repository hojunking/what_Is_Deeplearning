import numpy as np

#최소제곱법을 통해
# y = ax의 기울기 a와,y의 절편 b 계산

# np배열에 데이터 넣기
x = np.array([2,4,6,8])
y = np.array([81,94,91,97])

mx = np.mean(x) #x배열의 평균
my = np.mean(y)

print("x의 평균값 :",mx)
print("y의 평균값 :", my)

#분모
divisor = sum([(i-mx)**2 for i in x])
# (x - x평균)의 제곱의 합 
# for i in x -> x 배열 크기만큼 돌린다
def top(x,y, mx, my):
    d =0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return  d
divided = top(x,y,mx,my)

print("분자의 값은 : {}".format(divided))

#기울기 a
a =divided / divisor
print("기울기 : {}".format(a))

# y의 절편 b
b = my - (mx*a)
print("y의 절편 : {}".format(b))



