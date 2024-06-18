# in , not in 키워드 : key 존재 유무 판단

students = {'시노부': '충주','카나에': '화주' ,'카나오' : '화주','아오이' : 1 ,'칸로지' : '연주'}

print('시노부' in students)
print('카나에' in students)

print('시노부' not in students)
print('카나에' not in students)

# len() : 딕셔너리 아이템의 개수를 알 수 있다

print(len(students))

# clear() : 모든 아이템을 삭제한다

students.clear()
print(students)


#실습

students2 = {'시노부': '충주','카나에': '화주' ,'카나오' : '화주','아오이' : 1 ,'칸로지' : '연주','도우마': '오니','무잔':'오니'}
trash = ['도우마','무잔']

for t in trash:
    if t in students2:
        del students2[t]

print(students2)

