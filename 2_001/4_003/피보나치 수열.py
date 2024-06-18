#피보나치 수열 : 어떤 수가 어떤 규칙성을 가지고 나열되더라, 세 번쨰 항은 두번쨰 항과 첫 번쨰 항을 더한 값이다.
# 토끼가 증식하는 현상을 보고 피보나치 수열 도출함
# a1 =1 , a2 =1 이고 n>2일 떄 ,an = an-2 + an-1

# 파이썬을 이용해서 피보나치 수열 구현

# inputN=int(input('n 입력 : '))
#
# valueN =0 #즉, valuePre1 + valuePreN2 = valueN임
# sumN =0
#
# valuePreN1 =0 #valueN이전의 값 1
# valuePreN2 =0 #valueN이전의 값 2
#
# n =1
# while n <= inputN:
#     if n == 1 or n ==2: # 첫번쨰와 두번째 항 처리
#         valueN = 1
#         valuePreN1 = valueN
#         valuePreN2 = valueN
#         sumN +=valueN
#         n +=1
#
#     else: #세번쨰 항부터 처리
#         valueN = valuePreN1 + valuePreN2
#         valuePreN1 = valuePreN2
#         valuePreN2 = valueN
#         sumN += valueN
#         n +=1
#
#
# print(f'{inputN}번쨰 항의 값 : {valueN}')
# print(f'{inputN}번쨰 항 까지의 합 : {sumN}')

# 연습문제
inputN=int(input('n 입력 : '))

valuePre1 = 0
valuePre2 = 0
valueN = 0
sumN = 0

n =1
while n <= inputN:
    if n == 1 or n == 2:
        valueN = 1
        valuePre1 = valueN
        valuePre2 = valueN
        sumN +=valueN
        n +=1


    #세번쨰 항 부터
    else:
        valueN = valuePre1 + valuePre2
        valuePre1 = valuePre2
        valuePre2 = valueN
        sumN += valueN
        n += 1

print(f'{inputN}항의 값 : {valueN}')
print(f'{inputN}항까지의 합 : {sumN}')


