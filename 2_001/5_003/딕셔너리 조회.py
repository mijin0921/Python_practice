#key를 이용해서 값을 조회한다

students = {'시노부': '충주','카나에': '화주' ,'카나오' : '화주','아오이' : 1 ,'칸로지' : '연주'}

print(students['시노부'])
print(students['카나에'])
print(students['카나오'])
print(students['아오이'])
print(students['칸로지'])

# get()함수 : 딕셔너리의 값 조회 가능(딕셔너리 안에 없는 키 값을 입력해도 에러가 발생하지 않는다)

print(students.get('시노부'))
print(students.get('카나에'))
print(students.get(1))
