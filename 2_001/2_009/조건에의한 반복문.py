#조건에 만족하면 반복 실행한다. 그렇지 않으면 반복을 중단한다.

# endNum =10
# num = 0
#
# while num <= endNum:
#     print(num)
#     num +=1 #이 조건이 없으면 무한루프에 빠짐
#
# user=int(input('희망 구구단 입력 : '))
#
# n=1
#
# while n <= 9:
#     result = user * n
#     print('{}*{} : {}'.format(user,n,result))
#     n +=1
#
# 응용

n=0
max=0
current=30
remove=0.15

while max <=20:
    n+=1
    max = current-(remove * n)
    print('구를수 있는 횟수 : {}'.format(n)) # 틀림

count = 0 #구를 횟수
current = 30 #현재 바퀴 두께
remove = 0.15 #한번 돌면 마모되는 두께

while current >=20: #현재 바퀴 두께가 20 이하로 내려가면 반복문 종료
    count += 1
    current -=remove

print('구를수 잇는 횟수 : {}'.format(count))


