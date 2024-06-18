# #파이썬을 이용하여 사용자가 입력한 숫자의 약수를 출력

user= int(input('숫자를 입력하시오 : '))

for number in range(1,(user+1)):
    if user % number == 0:
        print(f'{number}은 {user}의 약수입니다.')

# 핵심 : 나머지가 0인 숫자 찾기

#
# # 파이썬을 이용하여 사용자사 입력한 숫자까지의 소수 출력
#
# user2= int(input('숫자를 입력하시오 : '))
#
# for number in range(2,user2 + 1):
#     flag =True
#     for n in range(2,number):
#         if number % n == 0:
#             # 만약에 1과 자기자신 사이에 나머지가 0인 어떤 수가 존재한다면 그것은 소수가 아님
#             flag = False
#             break
#
#     if flag:
#         print(f'{number}는 소수')
#     else:
#         print(f'{number}는 합성수')

# 연습문제

import random

# var = random.randint(100,1000)
# print(var)
#
# # 약수
#
# n1=[]
#
# for i in range(1,var+1):
#     if var % i == 0:
#         print(f'{i}는 {var}의 약수')
#         n1.append(i)
#
# print(n1)
#
# # 소수
#
# n2=[]
#
# for i in range(2,var+1):
#     flag = True
#     for n in range(2,i):
#         if i % n == 0:
#             flag = False
#             break
#     if flag:
#         print(f'{i}는 소수')
#         n2.append(i)
#
#
# print(n2)

