def fun1():
    print('fun1 호출!')
    fun2()
    print('나 왜 마지막....ㅎ') #이 구문은 맨 마지막 순사임. 함수는 위에서부터 차례대로 실행되기 때문

def fun2():
    print('fun2 호출!')
    fun3()
def fun3():
    print('fun3 호출!')

fun1()

#pass 사용
def aa():
    pass

aa()

#구구단

def dudu123():
    for i in range(1,10):
        print('123 * {} : {}'.format(i,123*i))
    gugu124()
    print('끝!')
def gugu124():
    for i in range(1,10):
        print('124 * {} : {}'.format(i,124*i))

dudu123()