#확률 : 모든 사건에서 특정 사건이 일어날 수 있는 수
# 표본 공간 : 모든 사건
# 특정 사건 : 사건
# 조합을 이용해서 확률을 알아낼 수 있다

# 파이썬을 이용한 확률 프로그램

def C():
    numN = int(input('n : '))
    numR = int(input('r : '))

    resultP = 1
    resultR = 1
    resultC = 1

    for n in range(numN, (numN - numR), -1):
        resultP *= n
    print(f'resultP : {resultP}')

    for n in range(numR, 0, -1):
        resultR *= n
    print(f'resultR : {resultR}')

    resultC = int(resultP / resultR)
    print(f'resultC : {resultC}')

    return resultC



sample = C()
print(f'sample : {sample}')

event1 = C()
print(f'event1 : {event1}')

event2 = C()
print(f'event2 : {event2}')

probability= event1*event2/sample
print(f'probability : {round((probability * 100),2)}%')



