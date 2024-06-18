#reverse() 함수 : 아이템 순서 바꿀수 있다

students = ['시노부','카나에','네즈코','기유','탄지로']
students.reverse()
print(students)

# 암호해독

secret = '27156231'

secretList=[]
solvedList = ''

for cat in secret:
    secretList.append(int(cat))

secretList.reverse()
print(secretList)

