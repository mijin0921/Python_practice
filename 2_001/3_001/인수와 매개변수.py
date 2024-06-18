#매개변수 : 함수의 호출부와 선언부의 관계를 맺어주는 변수다
#인수와 매개변수의 개수는 일치해야 한다.

def well(name): #name은 매개변수
    print('{}아 오늘도 화이팅!'.format(name))

well('미진') #미진과 지원은 인수
well('지원')

#매개변수 개수가 정해지지 않은 경우 '*'를 이용한다.

def printNum(*numbers):
    print(type(numbers))

printNum()
printNum(1,2,3)
printNum(2,3,4,5,6,7)

def avg(ko,en,mt):
    sum= ko + en + mt
    a=sum/3
    print(sum)
    print(round(a,2))

avg(55,100,99)