#for문과 유클리드 호제법을 이용해서 최소공배수를 구하자
#
# num1 = int(input('정수입력 : '))
# num2 = int(input('정수입력 : '))
# maxNum=0
#
# for n in range(1,num1+1): #num1보다 작은 숫자 중에서만 찾으면 된다.
#     if num1 % n == 0 and num2 % n ==0:
#         print(f'공약수 : {n}')
#         maxNum = n
#
# print(f'최대공약수 : {maxNum}')
#
# # 최대공약수를 이용해서 최소공배수 구하는 법
#
# minNum = (num1*num2)//maxNum #두개수를 곱해서 최대공약수로 나눈 몫이 최소공배수이다.
# print(f'최소공배수 : {minNum}')

# 섬마을에 과일, 생선, 야채를 판매하는 배가 각 3,4,5일 주기로 입항한다고 할 때 모든 배가 동시에 입항하는 날짜를 계산해보자.
# 3,4,5의 최소공배수

num1 = 3
num2 = 4
num3= 5
maxNum=0

for n in range(1,num1+1): #num1보다 작은 숫자 중에서만 찾으면 된다.
    if num1 % n == 0 and num2 % n ==0:
        print(f'공약수 : {n}')
        maxNum = n

print(f'최대공약수 : {maxNum}')

# 최대공약수를 이용해서 최소공배수 구하는 법

minNum = (num1*num2)//maxNum #두개수를 곱해서 최대공약수로 나눈 몫이 최소공배수이다.
print(f'최소공배수 : {minNum}')

newNum=minNum



for n in range(1,newNum+1): #2개의 수에서 나온 최소공배수를 나머지 숫자와 함께 다시 최소공배수 구한다
    if num3 % n == 0 and newNum % n ==0:
        print(f'공약수 : {n}')
        maxNum = n

print(f'최대공약수 : {maxNum}')

# 최대공약수를 이용해서 최소공배수 구하는 법

minNum = (num3*newNum)//maxNum #두개수를 곱해서 최대공약수로 나눈 몫이 최소공배수이다.
print(f'3척의 최소공배수 : {minNum}')

# 연습문제

import random

var1 = random.randint(100,1000)
var2 = random.randint(100,1000)
maxNum=0
print(f'var1 : {var1}')
print(f'var2 : {var2}')

if var1 < var2:
    for i in range(1,var1+1):
        if var1 % i ==0 and var2 % i ==0:
            print(f'공약수 : {i}')
            maxNum=i


minNum = (var1*var2) // maxNum

print(f'최대공약수 : {maxNum}')
print(f'최소공배수 : {minNum}')
