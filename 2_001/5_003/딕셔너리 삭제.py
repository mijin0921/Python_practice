#del 과 key를 이용한 item삭제

students = {'시노부': '충주','카나에': '화주' ,'카나오' : '화주','아오이' : 1 ,'칸로지' : '연주'}
print(students)
del students['아오이']
print(students)

del students['카나에']
print(students)

#pop() 함수와 key를 이용한 삭제

returnV = students.pop('카나오')
print(returnV)
print(students)

#실습 : 최고와 최저점 찾아서 삭제하기

scores = { 's1': 8.9, 's2': 8.1, 's3': 8.5 , 's4': 9.8, 's5': 8.8}

minS=10 ; minK=''
maxS=0 ; maxK =''

for key in scores.keys():
    if scores[key] < minS:
        minS = scores[key]
        minK = key

    if scores[key] > maxS:
        maxS = scores[key]
        maxK = key


print(f'{minK}:{minS}')
print(f'{maxK}:{maxS}')

del scores[minK]
del scores[maxK]

print(scores)




