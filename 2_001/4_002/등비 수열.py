#등비 수열 : 연속된 두 항의 비가 일정한 수열
# 일반항 공식 : an = a1* r(공비)^(n-1)
# 등비 중항 : 연속된 세 항에서 가운데 항 , 등비 중항의 제곱은 양끝 값의 곱과 같다
# 등비 수열의 합 : sn= a1*(1-(r^n)) / (1-r)
#
# inputN1=int(input('a1 입력 : '))
# inputR=int(input('공비 입력 : '))
# inputN=int(input('n 입력 : '))
#
# valueN = 0
#
# n=1
# while n<=inputN:
#
#     if n == 1 :
#        valueN = inputN1
#        print(f'{n}번쨰 항의 값 : {valueN}')
#        n +=1
#        continue
#
#     valueN *= inputR
#     print(f'{n}번쨰 항의 값 : {valueN}')
#     n +=1
#
# # 공식을 이용
#
# valueN=inputN1*(inputR**(inputN-1))
# print(f'{inputN}번쨰 항의 값 : {valueN}')
#
# # 파이썬을 이용하여 등비수열의 합 구하기
#
# inputN1=int(input('a1 입력 : '))
# inputR=int(input('공비 입력 : '))
# inputN=int(input('n 입력 : '))
#
# valueN = 0
# sumN = 0
#
# n=1
# while n<=inputN:
#
#     if n == 1 :
#        valueN = inputN1
#        sumN += valueN
#        print(f'{n}번쨰 항까지 합 : {sumN}')
#        n +=1
#        continue
#
#     valueN *= inputR
#     sumN += valueN
#     print(f'{n}번쨰 항까지 합 : {sumN}')
#     n +=1
#
# # 공식 이용
#
# sumN = inputN1 * (1-(inputR**inputN)) / (1-inputR)
# print(f'{inputN}번쨰 항까지 합 : {int(sumN)}')

# 연습 문제

f1=int(input('a1 입력 : '))
fR=int(input('공비 입력 : '))
newN=int(input('n 입력 : '))

valueN=0
sumN=0

n =1
while n <= newN:

    if n ==1 :
        valueN = f1
        sumN += valueN
        print(f'{n}번쨰 항 : {valueN}')
        print(f'{n}번쨰 항 까지의 합 : {sumN}')
        n +=1

    valueN *= fR
    sumN += valueN
    print(f'{n}번쨰 항 : {valueN}')
    print(f'{n}번쨰 항 까지의 합 : {sumN}')
    n +=1

an=f1*(fR**(newN-1))
print(f'{newN}번쨰 항 : {an}')
sn= f1*(1-(fR**newN))/(1-fR)
print(f'{newN}번쨰 항 까지의 합 : {int(sn)}')

