#count() 함수 : 특정 아이템의 개수를 알 수 있다

students = ['시노부','카나에','네즈코','기유','탄지로','시노부','시노부','카나에']

print(students.count('시노부'))

#del +리스트명 [인덱스] 키워드를 사용하면 특정 아이템을 삭제할 수 있다

del students[5:]
print(students)

#실습 : 헌혈 혈액형 개수

import random

types = ['A','B','AB','O']
todayData =[]

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

print(f'todayData : {len(todayData)}')

for type in types:
    print(f'{type}형 \t: {todayData.count(type)}개 ')






