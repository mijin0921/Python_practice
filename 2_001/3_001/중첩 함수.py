#함수안에 또 다른 함수가 선언되어 있는 형태이다.

#내부 함수를 함수 밖에서 호출할 수 없다.

def out_fun():
    print('out_fun called!')

    def in_fun():
        print('in_fun called!')

    in_fun() #이 호출은 out_fun 함수의 실행문이다.

out_fun()

# 응용

def calculator(n1,n2,operator):
    def add():
        print(f'덧셈 : {n1+n2}')
    def sub():
        print(f'뺄셈 : {n1-n2}')
    def mul():
        print(f'곱셈 : {n1*n2}')
    def div():
        print(f'나눗셈 : {n1/n2}')

    if operator == 1:
        add()
    elif operator == 2:
        sub()
    elif operator == 3:
        mul()
    elif operator ==4:
        div()


while True: #반복해서 리셋되는 프로그램을 만들려면 함수와 반복문 조건문 믹스 필요!!!
    num1=int(input('숫자를 입력하시오 : '))
    num2 =int(input('숫자를 입력하시오 : '))
    operatorNum =int(input('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료 :'))

    calculator(num1,num2,operatorNum)

    if operatorNum == 5:
        print('안녕히계세요')
        break


