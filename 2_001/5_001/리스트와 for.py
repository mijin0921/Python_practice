#리스트와 for문은 자주 같이 사용한다
# for문을 이용하면 리스트의 아이템을 자동으로 참조할 수 있다
# for~in 뒤에는 반복이 가능한 객체(리터러블 객체)이면 무엇이든지 들어올 수 있다

# for문을 이용한 내부 리스트 조회

students = [[1,'시노부'],[2,'카나에'],[3,'네즈코'],[4,'기유'],[5,'탄지로']]
# 편한 방식
for classNo, name in students:
    print(f'{name} {classNo}등')

# 좀 불편한 방식
for i in range(len(students)):
    print(f'{students[i][1]} {students[i][0]}등')


#for문과 if문을 이요해서 과락 과목 출력하기

minScore= 60
scores=[['국어', 58],['영어',77],['수학',89],['과학',95],['국사',85]]

for item in scores:
    if item[1] < minScore:
        print(f'과락 과목 : {item[0]} , 점수 : {item[1]}')


for subject,score in scores:
    if score < minScore:
        print(f'과락 과목 : {subject} , 점수 : {score}')

