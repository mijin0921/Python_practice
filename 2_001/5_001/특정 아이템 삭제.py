#remove()함수 : 특정 아이템을 삭제할 수 있다.
#remove(특정 아이템) : 인자에 인덱스가 아닌 아이템을 넣어야 함

students = ['시노부','카나에','네즈코','기유','탄지로']

print(students)
students.remove('기유')
print(students)

#remove는 한개의 아이템만 삭제된다. 여러개의 아이템 삭제를 원하면 while문 사용필요

print('카나에' in students)

while '카나에' in students:
    students.remove('카나에')

print(students)

