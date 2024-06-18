#버스 정류장 문제

#
# busA = 6:0     #
# busB = 6:0
# busC = 6:20
# time=0
#
# while True:
#     busA += 15
#     busB += 13
#     busC += 8
#     if busA ==busB:
#         time=busA
#         break
# print('{}와 {} 동시 정차! {}'.format)
#     elif busA == busC:


# 풀이
# 공배수와 비슷한 문제
#
# busA = 15
# busB = 13
# busC = 8
# totalMin=60*17 #6시 부터 오후11시까지 총 분
#
# for i in range(totalMin+1):  #총 분 만큼 반복문
#     if i<20 or i > (totalMin-60): #A버스와 B버스만 운행하는 경우
#         if i % busA ==0 and i % busB==0:  #15와 13으로 동시에 나눴을 때 나머지가 같은 분
#             print('busA와 busB 동시정차!',end='')
#             hour = 6+ (i//60) # 첫차시간 6시 부터 i분 을 60분으로 나눈 몫 더하기
#             min = i % 60 #i분을 60분으로 나눈 나머지
#             print('\t{}:{}'.format(hour,min))
#     else:  # A,B,C가 다 운행할 때
#         if i % busA ==0 and i % busB==0:  #15와 13으로 동시에 나눴을 때 나머지가 같은 분
#             print('busA와 busB 동시정차!',end='')
#             hour = 6+ (i//60) # 첫차시간 6시 부터 i분 을 60분으로 나눈 몫 더하기
#             min = i % 60 #i분을 60분으로 나눈 나머지
#             print('\t{}:{}'.format(hour,min))
#         elif i % busA ==0 and i % busC==0:  #15와 13으로 동시에 나눴을 때 나머지가 같은 분
#             print('busA와 busC 동시정차!',end='')
#             hour = 6+ (i//60) # 첫차시간 6시 부터 i분 을 60분으로 나눈 몫 더하기
#             min= i % 60 #i분을 60분으로 나눈 나머지
#             print('\t{}:{}'.format(hour,min))
#         elif i % busB ==0 and i % busC==0:  #15와 13으로 동시에 나눴을 때 나머지가 같은 분
#             print('busB와 busC 동시정차!',end='')
#             hour = 6+ (i//60) # 첫차시간 6시 부터 i분 을 60분으로 나눈 몫 더하기
#             min= i % 60 #i분을 60분으로 나눈 나머지
#             print('\t{}:{}'.format(hour,min))



#톱니바퀴
#최소 공배수 : 최초로 맞물린 톱니가 다시 만났을 때 거쳐간 톱니 수
#
# n1=int(input('톱니바퀴1의 톱니 수: '))
# n2=int(input('톱니바퀴2의 톱니 수: '))
# finish1=0
# finish2=0
# min=0
#
# while True:
#     finish1= n1 % i
#     finish2= n2 % i
#
#     if finish1 == 0 and finish2 ==0:
#         min = i
#     else:
#         min = n1*n2
#         break
# #
# print('최초 만나는 톱니수(최소 공배수) : {}'.format(min))
# print('gearA 회전수 : {}회전'.format(min//n1))
# print('gearB 회전수 : {}회전'.format(min//n2))

# 풀이

# n1=int(input('톱니바퀴1의 톱니 수: '))
# n2=int(input('톱니바퀴2의 톱니 수: '))
# gear1=0 #다시 만나기 까지 톱니바퀴 1의 톱니가 몇개 지나가는지를 담는 변수
# gear2=0
# leastNum=0 #최소공배수를 담을 변수
# flag= True
#
# #아직 최소공배수를 모르기 때문에 각각 얼마나 돌아가야하는지 모름. 그러므로 조건에 의한 반복문이 적합
#
# while flag:
#     if gear1 != 0:
#         if gear1 != leastNum:
#             gear1 +=n1
#         else:
#             flag=False
#     else:
#         gear1 += n1
#
#     #제일먼저 최소공배수가 구해지는 순간의 조건문 작성
#     if gear2 !=0 and gear2 % n1 ==0:
#         leastNum = gear2 #이때가 최소공배수
#     else:
#         gear2 += n2 #만약 최소공배수가 구해지지 않았으면 톱니바퀴2는 계속 돌아가야함


# print('최초 만나는 톱니수(최소공배수): {}'.format(leastNum))
# print('gear1 회전수: {}'.format(int(leastNum/n1)))
# print('gear2 회전수: {}'.format(int(leastNum/n2)))

# 톱니바퀴 문제 복습

# 두 수의 최소공배수
# 먼저 최대 공약수를 구한다음
# 두 수를 곱하고 최대공약수로 나누면 됨

# gearA = int(input('톱니수 입력 : '))
# gearB = int(input('톱니수 입력 : '))
# maxN = 0 #최대공약수
# minN = 0 #최소공배수
#
# for i in range(1,gearA + 1):
#     if gearA % i == 0 and gearB % i == 0: #여기 나눗셈 공식 주의!!!
#         maxN = i
#
#
# minN = (gearA * gearB) // maxN
#
# print(f'최소 만나는 톱니수 : {minN}')
# print(f'gearA 톱니수 : {int(minN // gearA)}회전')
# print(f'gearB 톱니수 : {int(minN // gearB)}회전')
#
# # 윤년 계산기
#
# while True:
#     inputY = int(input('연도 입력 : '))
#     if inputY % 4 == 0 and inputY % 100 != 0:
#         print(f'{inputY}년 : 윤년!')
#     elif inputY % 400 == 0:
#         print(f'{inputY}년 : 윤년!')
#     else:
#         print(f'{inputY}년 : 평년')



