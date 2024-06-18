#팩토리얼 : 1부터 양의 정수 n까지의 정수를 모두 곱한 것
# 0!은 1로 약속한다

# 파이썬으로 팩토리얼 구현

# 1. 반복문을 이용 : while문 보다는 for문이 적절함

# inputN = int(input('n입력 : '))
#
# result = 1
# for i in range(1,inputN+1):
#     result *= i
#
# print(f'{inputN} 팩토리얼 : {result} ')
#
#
# # 2.재귀함수를 이용: 함수 안에서 나 자신을 다시 호출하는 함수
#
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#
#     return n * factorial(n-1)
#
# print(f'{inputN} 팩토리얼 : {factorial(inputN)}')
#
# # 3. math 모듈 이용
# import math
#
# math.factorial(inputN)
# print(f'{inputN} 팩토리얼 : {math.factorial(inputN)}')

# 연습문제

inputN = int(input('n입력 : '))
result = 1

for i in range(1,inputN+1):
    result *= i

print(f'{inputN} 팩토리얼 : {result}')

def fac(n):
    if n == 1 or n ==0:
        return 1

    return n * fac(n-1)

print(f'{inputN} 팩토리얼 : {fac(inputN)}')






