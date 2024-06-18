# math, random, time 모듈

# 파이썬에서 제공하는 수학 관련 함수

# sum()
# max()
# min()
# pow()
# round()

import math

# 절댓값
print(math.fabs(-20))

# 올림
print(math.ceil(-5.22))

# 내림
print(math.floor(-5.22))

# 버림
print(math.trunc(6.45))

# 최대공약수
print(math.gcd(14,21))

# 팩토리얼
print(math.factorial(10))

# 제곱근
print(math.sqrt(13))

import time

lt=time.localtime()
print(lt)

lt=lt.tm_mon
print(lt)