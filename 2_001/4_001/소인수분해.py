#파이썬을 이용해서 사용자가 입력한 수를 소인수분해 하자

inputNum=int(input('정수를 입력하시오 : '))

n=2
while n <=inputNum:
    if inputNum % n == 0:
        print(f'소인수 : {n}')
        inputNum /= n #처음 n으로 나눈 몫을 다시 inputNum에다가 할당해 준것임

    else: #약수가 아닌 수이기 때문에 다음 숫자로 넘어가야 함
        n +=1


# 72에 x를 곱하면 y의 제곱이 된다. x가 되는 가장 작은 수를 구하라

# 소인수의 개수가 짝수가 되어야 함. 즉, 소인수의 개수가 중요하다

searchNums=[] # 리스트 사용

# n=2
# while n <=inputNum:
#     if inputNum % n == 0:
#         print(f'소인수 : {n}')
#         if searchNums.count(n) == 0:
#             searchNums.append(n)
#         elif searchNums.count(n) == 1:
#             searchNums.remove(n)
#         inputNum /= n  # 처음 n으로 나눈 몫을 다시 inputNum에다가 할당해 준것임
#
#
#     else: #약수가 아닌 수이기 때문에 다음 숫자로 넘어가야 함
#         n +=1
#
# print(searchNums)


# 연습문제

import random

var = random.randint(100,1000)
print(var)
nums =[]

n=2
while n <= var:
    if var % n == 0:
        print(f'소인수 : {n}')
        var /= n
        nums.append(n)

        if nums.count(n) >=0:
            print(f'{n}의 개수 : {nums.count(n)}')

    else:
        n +=1


