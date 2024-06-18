#자료구조
student1 = '시노부'
student2 = '카나에'
student3 = '네즈코'
student4 = '기유'
student5 = '탄지로'

students = ['시노부','카나에','네즈코','기유','탄지로']

print(student1)
print(students[:2])

# for student in students:
#     print(student)


# 리스트
# 숫자 , 문자, 논리형 등을 같이 저장할 수 있다.
# 리스트에 또 다른 자료형 데이터를 저장할 수도 있다.

# 인덱스 : 리스트 아이템에 자동으로 부여되는 번호표, 무조건 0부터 출발

print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])
print(len(students))
print('len()의 값은 인덱스 끝 번호 +1이네~')

for i in range(5):
    if i % 2 == 0:
        print('-'*5+'짝수 학생'+'-'*5)
        print(f'{students[i]}')

    else:
        print('-' * 5 + '홀수 학생'+'-' * 5)
        print(f'{students[i]}')


# 리스트의 길이 : 리스트에 저장된 아이템의 개수
# len() : 리스트 아이템 개수, 문자열의 길이 알 수 있다.

for i in range(len(students)):
    print(students[i])

print('range(len(students)) 은 students 리스트의 index와 똑같음')