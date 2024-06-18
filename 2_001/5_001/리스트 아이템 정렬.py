#sort() 함수 : 이이템을 정렬할 수 있다(오름차순)
#sort(reverse = True) : 내림차순 정렬

students = ['시노부','카나에','네즈코','기유','탄지로']
students2 = ['카나오','아오이','이노스케']
students.extend(students2)
print(students)

students.sort()
print(students)

students.sort(reverse=True)
print(students)