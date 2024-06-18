#딕셔너리에 아이템 추가하는 방식과 동일하게 값 수정 가능

students = {'시노부': '충주','카나에': '화주' ,'카나오' : '화주','아오이' : 1 ,'칸로지' : '연주'}

students['아오이'] = '간호대장'
print(students)

# 실습 : 학생점수가 60점 미만이면 f(재시험)으로 값 변경

scores={'kor':88,'eng':55,'mat':85,'sci':57,'his':82}

for sub in scores.keys():
    if scores[sub] < 60 :
        scores[sub] = 'F(재시험)'
        print(f'{sub} : {scores[sub]}')
    else:
        print(f'{sub} : {scores[sub]}')
        

