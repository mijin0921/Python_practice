#pop()함수 : 마지막 인덱스에 해당하는 아이템을 삭제할 수 있다
#pop(n) : n인덱스에 해당하는 아이템을 삭제

students = ['시노부','카나에','네즈코','기유','탄지로']

students.pop(4)
print(students)

students.pop()
print(students)

rValue = students.pop() #삭제한 아이템을 반환
print(rValue)

# 최고점수 최저점수 삭제 프로그램

