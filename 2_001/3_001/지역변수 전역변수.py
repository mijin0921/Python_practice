#전역변수 : 함수 밖에 선언된 변수로 어디에서나 사용가능하지만 함수 안에서 수정할 수는 없다.
#즉, 함수안에서 잠시 값을 바꿔도 본래의 값이 변하지는 않는다.

num_out = 10 #전역 변수

def printNum():
    num_out = 20 #지역 변수
    print('num_out : {}'.format(num_out))

printNum()
print('num_out : {}'.format(num_out))

# 지역 변수 : 함수 안에 선언된 변수로 함수 안에서만 사용 가능하다.

# global 키워드를 사용하면 함수 안에서도 전역변수의 값을 수정할 수 있다.
# 방문객 수를 카운트 하는 함수

totalVisit=0

def countVisit():
    global totalVisit
    totalVisit += 1
    print('누적 방문객 : {}'.format(totalVisit))

countVisit()
countVisit()
countVisit()
print(totalVisit)
