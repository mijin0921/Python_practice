students = ['시노부','카나에','네즈코','기유','탄지로']

n = 0
while n < len(students):
    print(students[n])
    n +=1

n = 0
flag = True
while flag:
    print(students[n])
    n +=1

    if n == len(students):
        flag = False


n = 0
while True:
    print(students[n])
    n +=1

    if n == len(students):
        break

# 일반적으로 리스트는 for문과 많이 쓰임

#while문과 if문을 이용해서 과락 과목 출력하기

minScore= 60
scores=[['국어', 58],['영어',77],['수학',89],['과학',95],['국사',85]]

n = 0
while n <len(scores):
    if scores[n][1] < minScore:
        print(f'과락 과목 : {scores[n][0]} , 점수 : {scores[n][1]}')
    n +=1

