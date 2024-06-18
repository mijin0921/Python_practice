# 논리형 데이터를 통해 반복문 빠져나오기
# flag=True
# num=0
# sum=0
#
# while flag:
#     num += 1
#     sum += num
#     print('{}까지 합은 {}입니다.'.format(num,sum))
#
#     if sum > 100:
#         flag = False

import random

flag=True
date=0
sum=0

while flag:
    people = random.randint(50, 100) #얘를 반복문 안에 넣어야 매일 다른 난수가 만들어짐
    date +=1
    sum +=people
    print('날짜 :{}, 환자수 :{}, 누적 환자수 : {}'.format(date,people,sum))

    if sum >= 10000:
        flag=False

print(date)