# 시그마 : 수열의 합을 나타내는 기호

# 계차 수열 : 두항의 차로 이루어진 또 다른 수열
# 계차 수열을 이용해서 수열의 일반항을 구할 수 있다.
# 계차 수열에서 특정항 까지의 합을 구한 다음 수열의 첫번 째 항을 빼면 일반항 공식이 나온다


# 파이썬을 이용하여 계차 수열을 이용한 일반항 값 구하기
# an = {3,7,13,21,31,43,57}
# bn=    4 6  8 10 12 14

# inputAN1= int(input('a1 입력 : '))
# inputAN= int(input('an 입력 : '))
#
# inputBN1= int(input('b1 입력 : '))
# inputBD= int(input('bn 입력 : '))
#
# valueAN = 0
# valueBN = 0
# n = 1
#
# while n<=inputAN:
#
#     if n == 1:
#         valueAN = inputAN1
#         valueBN = inputBN1
#         print(f'an의 {n}번쨰 항의 값 : {valueAN}')
#         print(f'bn의 {n}번쨰 항의 값 : {valueBN}')
#         n +=1
#
#     valueAN = valueAN + valueBN
#     valueBN = valueBN + inputBD
#     print(f'an의 {n}번쨰 항의 값 : {valueAN}')
#     print(f'bn의 {n}번쨰 항의 값 : {valueBN}')
#     n +=1
#
# # 공식을 이용
#
# # 첫번 째 , bn의 일반항 구하기
# # 두번 쨰 , bn의 일반항 합 공식 구하기
# # bn의 합 공식 = an -a1 대입하여 an 일반항 공식 구하기
#
# # n^2 + n + 1 = an 이 공식은 직접 계산해야함
#
# valueAN = inputAN **2 + inputAN + 1
# print(f'an의 {inputAN}번쨰 항의 값 : {valueAN}')

# 연습 문제

var =int(input('n을 입력하시오 : '))

sn = 2*(1-(2**var))/-1
print(f'{var}일 째 받게 되는 쌀의 개수 : {format(int(sn),   ',')}')


#계차수열 연습문제

n=int(input('n을 입력 :'))

an = (3*n*(n-1)/2) + 2
print(f'{n}항의 값 : {int(an)}')


