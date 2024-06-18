#리스트와 마찬가지로 [n : m]로 슬라이싱 할 수 있다
#슬라이싱 단계 설정 가능
#튜플은 슬라이싱으로 아이템 변경 불가능
# slice() 함수 사용 가능

students = ('시노부','카나에','카나오','아오이','칸로지',20,18,17,19)

print(students[0:4])
print(students[4: -1:2])

# 리스트에 튜플 아이템으로 변경 가능

students2 = ['카나오','아오이','이노스케']

students2[1:]=('시노부','카나에','카나오','아오이','칸로지')

print(students2)

students2.append(students)
print(students2)



