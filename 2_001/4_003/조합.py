#조합 : 순서 상관없이 r개 선택
# nCr = nPr / r!

# 파이썬으로 조합 구현

# numN=int(input('n : '))
# numR=int(input('r : '))
#
# resultP =1; resultR = 1
#
# for n in range(numN,(numN-numR),-1):
#     print(f'{n}')
#     resultP *= n
# print(f'resultP : {resultP}')
#
# for i in range(numR,0,-1):
#     print(f'{i}')
#     resultR *= i
# print(f'resultR : {resultR}')
#
# resultC = int(resultP/resultR)
#
# print(f'resultC : {resultC}')

# 연습문제
numN=int(input('n : '))
numR=int(input('r : '))

resultP =1; resultR = 1; resultC = 0

for n in range(numN,(numN-numR),-1):
    resultP *= n
print(f'resultP : {resultP}')

for n in range(numR,0,-1):
    resultR *= n
print(f'resultR : {resultR}')


resultC=int(resultP/resultR)
print(f'resultC : {resultC}')

probability=round((1/resultC)*100,2)
print(f'probability : {probability}%')



