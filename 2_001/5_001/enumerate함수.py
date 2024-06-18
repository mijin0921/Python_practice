#enumerate()함수 : 인덱스와 아이템을 열거할 수 있다.
#문자열에도 적용할 수 있다

students = ['시노부','카나에','네즈코','기유','탄지로']
for idx,student in enumerate(students):
    print(f'{idx} : {student}')

srt = '귀멸의 칼날'

for idx,s in enumerate(srt):
    print(f'{idx} : {s}')
