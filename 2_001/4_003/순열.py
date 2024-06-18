#순열 : n 개에서 r개를 택하여 나열하는 경우의 수 (단, 순서있게 나열했을 때 모든경우의 수를 따지는 것)
#순열은 팩토리얼을 이용해서 나타낼 수 있다
#순열 : nPr = n(n-1)(n-2)...(n-r+1) = n!/(n-r)!

# 파이썬으로 순열 구현하기

# numN = int(input('numN : '))
# numR = int(input('numR : '))
# result = 1
#
# for n in range(numN,(numN-numR),-1): #numN에서부터 numR까지 하나씩 내려오면서 곱하는 range 범위
#      result *= n
#      print(f'{n}')
#
# print(f'result : {result}')
#
# # 원 순열 : 시작과 끝의 구분이 없는 순열
# # 공식 : n!/n = (n-1)!
#
# # 파이썬 이용  원순열
# inputN=int(input('n입력 : '))
#
# result =1
# for i in range(1,inputN):
#      result *= i

# 연습문제

def sequence():
     numN = int(input('numN : '))
     numR = int(input('numR : '))
     result = 1

     for i in range(numN,(numN-numR),-1):
          result *= i

     return result


event1 = sequence()

event2 = sequence()

event3 = event1 * event2

print(f'경우의 수 : {event3}')




