import random

var = random.sample(range(1,21),10)

inputNum = int(input('inputN : '))

resultIdx = -1

for idx,n in enumerate(var):
    if n == inputNum:
        resultIdx = idx

print(var)
print(f'검색숫자 : {inputNum}')
print(f'검색결과 인덱스 : {resultIdx}')


