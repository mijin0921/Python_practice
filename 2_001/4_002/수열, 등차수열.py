#수열 : 규칙성을 가지고 나열되어 있는 수들
#일반항 : 수열의 규칙성을 나타내는 항
#항 : 나열되어 있는 수 한개
#수열의 합 : an(특정항)  = sn-s(n-1)

# 등차 수열 : 연속된 두 항의 차이가 일정한 수열
# 등차 수열의 규칙성을 이용해서 일반항을 구할 수 있다.
# 일반항 식 : an = a1 + (n-1) * d
# 등차 중항 : 연속된 세 항 가운데 항 , 양 끝쪽을 더한 다음 2로 나누면 됨
# 등차 수열의 합 : sn = n(a1 + an) /2


# 파이썬을 이용하여 등차 수열을 구현

# inputN1=int(input('a1 입력 : '))
# inputD=int(input('공차 입력 : '))
# inputN=int(input('n 입력 : '))
#
# valueN = 0
# n=1
# while n <= inputN:
#
#     if n ==1: #첫 번째 항일 떄
#         valueN=inputN1
#         print(f'{n}번재 항의 값 : {valueN}')
#         n +=1
#         continue
#
#     valueN += inputD #두번쨰 항부터 계산 시작
#     print(f'{n}번재 항의 값 : {valueN}')
#     n +=1
#
#
#
# # 등차 수열의 공식을 이용
#
# valueN = inputN1 + (inputN-1)* inputD
# print(f'{inputN}번재 항의 값 : {valueN}')
#
#
# #파이썬을 이용하여 특정 항까지의 합 구하기 (일반항에 대한 코드를 먼저 생각하면 도움됨)
#
# inputN1=int(input('a1 입력 : '))
# inputD=int(input('공차 입력 : '))
# inputN=int(input('n 입력 : '))
#
# valueN = 0
# sumN=0
#
# n=1
# while n <= inputN:
#
#     if n ==1: #첫 번째 항일 떄
#         valueN=inputN1
#         sumN += valueN
#         print(f'{n}번재 항까지의 합 : {sumN}')
#         n +=1
#         continue
#
#     valueN += inputD #두번쨰 항부터 계산 시작
#     sumN +=valueN
#     print(f'{n}번재 항까지의 합 : {sumN}')
#     n +=1
#
# # 공식을 이용
# valueN = inputN1 + (inputN-1)* inputD
# sumN = inputN*(inputN1 + valueN) / 2
# print(f'{inputN}번재 항까지의 합 : {int(sumN)}')


# 연습 문제

newN=int(input('n번째 항 : '))
f1= int(input('첫번째 항 : '))
fd= int(input('공차 : '))

valueN = 0
sumN = 0

n=1
while n <= newN:

    if n == 1:
        valueN = f1
        sumN += valueN
        print(f'{n}번쨰 항 : {valueN}')
        print(f'{n}번쨰 항까지의 합 : {sumN}')
        n +=1

    valueN += fd
    sumN += valueN
    print(f'{n}번쨰 항 : {valueN}')
    print(f'{n}번쨰 항까지의 합 : {sumN}')
    n += 1



an = f1+(newN-1)*fd
print(f'{newN}번쨰 항 : {an}')

sn=newN*(f1+an)/2
print(f'{newN}번쨰 항까지의 합 : {int(sn)}')


