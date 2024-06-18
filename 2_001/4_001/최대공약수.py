#최대공약수 구하는 법 : 공통인 소인수의 거듭제곱에서 지수가 작은 수를 모두 곱한다.

# 또는 소수로 나눗셈 해서 사용한 소수만 곱한다

num1 = int(input('정수입력 : '))
num2 = int(input('정수입력 : '))
maxNum=0

for n in range(1,num1+1): #num1보다 작은 숫자 중에서만 찾으면 된다.
    if num1 % n == 0 and num2 % n ==0:
        print(f'공약수 : {n}')
        maxNum = n

print(f'최대공약수 : {maxNum}')


# 유클리드 호제법으로 최대공약수를 구할 수 있다.

# num1 = int(input('정수입력 : '))
# num2 = int(input('정수입력 : '))
#
# temp1 = num1
# temp2 = num2
#
# while temp2 > 0:
#     temp = temp2
#     temp2 = temp1 % temp2 #처음 단계에서 temp1을 temp2로 나눈 나머지가 다음단계에서 temp2가 된다.
#     temp1 = temp #처음 단계에서 temp2였던 값이 다음 단계의 temp1이 된다
#
# print(f'{num1},{num2}의 최대 공약수 : {temp1}')

# 연습문제
import random

var1 = random.randint(100,1000)
var2 = random.randint(100,1000)
print(var1)
print(var2)
maxNum=0

if var1 < var2 :
    for i in range(1,var1+1):
        if var1 % i == 0 and var2 % i == 0:
            print(f'공약수 : {i}')
            maxNum=i

print(f'{var1}와 {var2}의 최대공약수 : {maxNum}')