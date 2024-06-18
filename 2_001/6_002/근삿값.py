#근삿값 : 특정 값(참값)에 가장 가까운 값 찾기

# 샘플 생성

import random

var = random.sample(range(0,51),20)
print(var)

# 입력값 받기

inputN=int(input('input Num : '))

nearN =0 # 근삿값 담을 변수
minNum = 50 # 입력값과 차이가 가장 적은 값 담을 변수(만약 데이터가 많아 최고값을 알기 어려울때는 최고값 먼저 구해야 함) 

# 반복문

for n in var:
    absNum = abs(n - inputN)

    if absNum < minNum:
        minNum = absNum
        nearN = n


print(f'{inputN}의 근삿값 : {nearN}')
