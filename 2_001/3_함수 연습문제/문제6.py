

def cal(a1,r,n):
    resultN = 0
    sumN = 0

    for i in range(1, n + 1):
        if i == 1:
            resultN = a1
            sumN += resultN
            print(f'{i}항의 값 : {resultN}')
        else:
            resultN *= r
            sumN += resultN
            print(f'{i}항의 값 : {resultN}')

    print(f'{n}항의 값 : {resultN}')
    print(f'{n}항 까지의 합 : {sumN}')

while True:
        inputA1 = int(input('a1을 입력하시오 : '))
        inputR = int(input('r을 입력하시오 : '))
        inputN = int(input('n을 입력하시오 : '))

        cal(inputA1, inputR, inputN)








