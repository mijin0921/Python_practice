#return 키워드: 함수 실행 결과를 호출부로 반환할 수 있다.

def add(n1,n2):
    print(n1+n2) #반환하지 않고 그냥 값 출력

def add2(n1,n2):
    result= n1+n2

    return result #함수의 호출부로 반환

def add3(n1,n2):
    result = n1 + n2

    return result

add3(1,2)  #그냥 반환한 것

total= add3(1,2) #반환하여 변수에 할당한 것

print(add3(1,2)) #반환한 값을 출력한 것


#함수가 return을 만나면 실행을 종료한다
def add3(n1,n2):
    result = n1 + n2

    return result
    print('안녕')  #이 구문은 실행되지 않음

# return으로 결과값을 복수로 반환할 수 있음 ->튜플로 반환됨
def add3(n1, n2):
    result = n1 + n2
    result2 = n1 - n2
    return result, result2

var=add3(1,2)
print(var)
print(type(var))

# 응용

import random

def oddNum():

    while True:
        var=random.randint(1,100)
        if var % 2 != 0:
            break
    return var

print(oddNum()) #return var의 값이 출력되게 됨