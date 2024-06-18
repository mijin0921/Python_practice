#extend() 함수 : 리스트에 또 다른 리스트를 연결하여 확장할 수 있다
#예를 들어 리스트A 와 리스트B를 연결하면 리스트A가 확장되는 형태

#덧셈(+)연산자로도 리스트를 연결할 수 있다
#이것은 새로운 리스트를 만들어 연결한 것이다 c = a + b

students = ['시노부','카나에','네즈코','기유','탄지로']
students2 = ['카나오','아오이','이노스케']

students.extend(students2)
print(students)

result = students + students2
print(result)



