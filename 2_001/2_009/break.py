#반복 실행 중 break를 만나면 반복문을 빠져나온다

num=0

while True:
    print('Hello')
    num +=1

    if num >=5:
        break

print('End')

# 응용

result =1
num=0

for i in range(1,11):
    result *= i

    if result > 50:
        num = i
        break

print(num,result)

# 응용2

date = 0
currentweight = 800

while currentweight <= 2200:
    date +=1
    currentweight += 70

print(date)
