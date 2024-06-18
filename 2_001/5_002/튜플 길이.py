# len() : 튜플의 길이를 알 수 있다

students = ('시노부','카나에','카나오','아오이','칸로지',20,18,17,19)

print(len(students))

# len() 과 반복문을 이용하면 튜플의 아이템 조회가 가능

for i in range(len(students)):
    print(f'{students[i]}')

n = 0
while n < len(students):
    print(f'{students[n]}')
    n +=1




