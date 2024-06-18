#key를 이용해서 아이템 추가

students = {'시노부': '충주','카나에': '화주' ,'카나오' : '화주','아오이' : 1 ,'칸로지' : '연주'}

#아이템 추가 방법
students['기유']='수주'
students['렌고쿠']='염주'

print(students)

#만약 기존에 있던 key에 새로운 값을 다시 넣으면, 기존의 값이 새로운 값으로 변경된다

students['아오이']='간호대장'
print(students)

# 실습 : 1부터 10까지 팩토리얼 구해서 딕셔너리에 추가하기

result = {}

for i in range(0,11):
    if i == 0:
        result[i] = 1

    else:
        for j in range(1,i+1):
            result[i] = result[j-1] * j

print(result)
