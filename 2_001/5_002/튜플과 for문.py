#튜플과 for문

students = ('시노부','카나에','카나오','아오이','칸로지')

for i in range(len(students)):
    print(f'{students[i]}')

for student in students:
    print(f'{student}')


students = (1,'시노부'),(2,'카나에'),(3,'카나오'),(4,'아오이'),(5,'칸로지')

maxS = 2

for score, student in students:
    if score <= maxS:
        print(f'{student}은 {score}등으로 상위권 학생입니다')

    else:
        print(f'{student}은 {score}등으로 하위권 학생입니다')

