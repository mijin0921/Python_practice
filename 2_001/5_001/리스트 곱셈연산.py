#리스트를 곱셈 연산하면 아이템이 반복된다

students = ['시노부','카나에','네즈코','기유','탄지로']

print(students*2)

#index() 함수 : 리스트 안의 아이템의 인덱스 번호를 알 수 있다

print(students.index('시노부'))

#실습 : 정수 7의 위치찾기

import random

var = random.sample(range(1,11),10)
print(var)
print(var.index(7))


