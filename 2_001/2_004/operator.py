#나머지 연산자

num1= 10
num2= 3

print(num1 % num2)

# 몫 연산자

print(num1 // num2)

# 나머지와 몫을 한번에 구하기

result =divmod(num1,num2)
print(result)
print('몫 : {}'.format(result[0]))
print('나머지 : {}'.format(result[1]))

# 거듭제곱 연산자

a=9
b=9

print(a**b)

# n의 m 제곱근 구하기

# 2의 3제곱근 구하기
result = 2**(1/3)
print(result)
print('result : %.2f' %result) #소수점 자리수 정하는 방법


# math 모듈의 sqrt()-제곱근, pow()-거듭제곱 함수
#sqrt는 2제곱근만 구할 수 있음

import math

print('2의 제곱근 : %.2f' %math.sqrt(2))
print('2의 거듭제곱 : %.f' %math.pow(2,2))


