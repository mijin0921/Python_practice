# #홀짝 게임
#
# import random
#
# var=random.randint(1,2)
# user=int(input('홀짝을 선택하시오 1.홀 2.짝 : '))
#
# if var==1 and user==1:  #and 연산자 활용!!
#     print('정답: {} 빙고!, 홀수!'.format(var))
# elif var==2!=user:
#     print('정답: {} 실패!, 짝수'.format(var))
# elif var==2==user:
#     print('정답: {} 빙고!, 짝수'.format(var))
# elif var==1!=user:
#     print('정답: {} 실패!, 홀수'.format(var))
# else:
#     print('다시 입력해 주세요')
#
# # 상수도 요금 계산기
#
# useType=int(input('업종 선택 1.가정용  2.대중탕용  3.공업용 : '))
# useAmount = int(input('사용량을 입력하세요 : '))
#
# print('='*25)
# if useType==1:
#    print('사용량 : 요금','\n{} : {}원'.format(useAmount,format(useAmount*540,   ',')))
#
# if useType==2:
#     if useAmount<=50:
#         print('사용량 : 요금','\n{} : {}원'.format(useAmount, format(useAmount * 820, ',')))
#     elif useAmount>50 and useAmount<=300:
#         print('사용량 : 요금','\n{} : {}원'.format(useAmount, format(useAmount * 1920, ',')))
#     elif useAmount>300:
#         print('사용량 : 요금','\n{} : {}원'.format(useAmount, format(useAmount * 2400, ',')))
#
# if useType ==3 and useAmount <=500:
#     print('사용량 : 요금','\n{} : {}원'.format(useAmount, format(useAmount * 240, ',')))
# elif useType ==3 and useAmount > 500:
#     print('사용량 : 요금','\n{} : {}원'.format(useAmount, format(useAmount * 470, ',')))
# print('='*25)

# 상수도 요금 풀이

# useType=int(input('업종 선택 1.가정용  2.대중탕용  3.공업용 : '))
# useAmount = int(input('사용량을 입력하세요 : '))
# price=0 # 사용량에 따른 가격 변수를 하나 생성한다! ->효율적임
#
# if useType==1:
#     price=540
#
# elif useType==2:
#     if useAmount<=50:
#         price=820
#     elif useAmount>50 and useAmount<=300:
#         price=1920
#     elif useAmount>300:
#         price=2400
#
# elif useType==3:
#     if useAmount <=500:
#         price=240
#     elif useAmount > 500:
#         price=470
#
# print('='*25)
# print('상수도 요금표')
# print('-'*25)
# userPrice=useAmount*price
# print('사용량 \t : \t 요금')  #간격 맞추려면 \t 쓰기!!
# print('{} \t : \t {}원'.format(useAmount,format(userPrice, ',')))
# print('='*25)
#
# # 미세먼지 차량 운행제한 프로그램
# import datetime  #현재 시간 정보 가져올 수 있음
# today=datetime.datetime.today()
# day=today.day
#
# dustRatio=int(input('미세먼지 수치 입력 : '))
# car=int(input('차량 종류 입력 1.승용차 2.영업용 차 : '))
# carNum=int(input('차량 번호 입력 : '))
# reg=0
#
# print('-' * 25)
# print(today)
# print('-'*25)
# if dustRatio<=150 and (day % 5) == (carNum % 5):
#     reg=5
#     print('차량 5부제로 금일 운행제한 차량입니다!')
# elif dustRatio>150:
#     if car==1 and (day % 2) == (carNum % 2):
#         reg=2
#         print('차량 2부제로 금일 운행제안 대상 차량입니다!')
#     elif car==2 and (day % 5) == (carNum % 5):
#         reg=5
#         print('차량 5부제로 금일 운행제한 차량입니다!')
#     else:
#         print('금일 운행 가능합니다')
# else:
#     print('금일 운행 가능합니다')
# print('-'*25)


# 상수도 요금 문제 복습
typeU = int(input('업종 선택 : 1. 가정용 2. 대중탕용 3. 공업용 : '))
amountU = int(input('사용량 입력 : '))
price = 0

print('='*20)
print('상수도 요금표')
print('='*20)

if typeU == 1:
    price = 540
    print('사용량\t:\t요금')
    print(f'{amountU}\t :\t{format(amountU * price, ',')}원')

elif typeU ==2:
    if amountU <50:
        price = 820
        print('사용량\t:\t요금')
        print(f'{amountU}\t :\t{format(amountU * price, ',')}원')
    elif amountU > 50 and amountU <=300:
        price = 1920
        print('사용량\t:\t요금')
        print(f'{amountU}\t :\t{format(amountU * price, ',')}원')
    elif amountU >300:
        price = 2400
        print('사용량\t:\t요금')
        print(f'{amountU}\t :\t{format(amountU * price, ',')}원')

elif typeU == 3:
    if amountU <= 500:
        price =240
        print('사용량\t:\t요금')
        print(f'{amountU}\t :\t{format(amountU * price, ',')}원')
    else:
        price = 470
        print('사용량\t:\t요금')
        print(f'{amountU}\t :\t{format(amountU * price,   ',')}원')

else:
    print('다시 입력해 주세요')

print('='*20)


# 난수 맞추기
import random

var = random.randint(1,1000)

flag = True
cnt = 0

while flag:
    inputN = int(input('정수를 입력하시오 : '))
    if inputN < var:
        cnt +=1
        print('난수가 크다')
        continue
    elif inputN > var:
        cnt +=1
        print('난수가 작다')
        continue
    elif inputN == var:
        cnt +=1
        flag = False
        break

print(f'난수 : {var}')
print(f'시도 횟수 : {cnt}')


