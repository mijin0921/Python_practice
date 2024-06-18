
for i in range(1,11):
    print('{} * {} : {}'.format(2,i,(2*i)))


players=['시노부','카나에','카나오','아오이']
for i in players:
    print('{}에게 까마귀 발송'.format(i))

# 반복문 종류 : 횟수에 의한  반복 / 조건에 의한 반복

for i in range(1,11):
    print('{} * {} : {}'.format(2,i,(2*i))) #횟수에 의한 반복

num = 0
while (num <= 10):
    print('num -> {}'.format(num))
    num +=1  #조건에 의한 반복
