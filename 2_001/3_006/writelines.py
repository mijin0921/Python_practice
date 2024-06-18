#writelines()는 리스트 또는 튜플 데이터를 파일에 쓰기 위한 함수이다.

week = ['월','화','수','목','금','토','일']

uri='C:/파이썬.ex/파이썬txt/'
# for day in week:
#     with open(uri+'week.txt','a') as w:
#         w.write(day)
#         w.write('\n')

with open(uri + 'week.txt', 'a') as w:
    w.writelines(week)
    #for문을 쓰지않고 바로 리스트(or튜플)를 넣으면 자동으로 반복해 준다.

    w.writelines(day + '\n' for day in week)
    #개행하고 싶을 때 