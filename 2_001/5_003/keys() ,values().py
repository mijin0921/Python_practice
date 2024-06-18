#keys() 함수 : 전체 키를 조회

students = {'시노부': '충주','카나에': '화주' ,'카나오' : '화주','아오이' : 1 ,'칸로지' : '연주'}

print(students.keys())
print(type(students.keys()))

# values() 함수 : 전체 값을 조회
print(students.values())
print(type(students.values()))

# items() 함수 : 전제 아이템을 조회 (튜플로 반환됨)
print(students.items())
print(type(students.items()))

#key , value, item을 따로 추출한 다름 리스트 형태로 변환하기

ks= list(students.keys())
print(ks)