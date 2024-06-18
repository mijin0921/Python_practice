#튜플은 리스트처럼 수정이 불가능
#리스트로 변환후 정렬해야 한다

#sorted() 함수를 이용하면 튜플도 정렬할 수 있다.

students = ('시노부','카나에','카나오','아오이','칸로지')

students = sorted(students)

print(students) #리스트로 반환됨

