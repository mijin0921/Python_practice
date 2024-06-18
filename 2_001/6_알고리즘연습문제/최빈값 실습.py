#회사직원의 나이 리스트

import random

age = []

for i in range(40):

    age.append(random.randint(20,51))

print(age)
print(len(age))

maxAge= 0
maxIdx = 0

for idx,a in enumerate(age):
    if a > age[maxIdx]:
        maxAge = a
        maxIdx = idx

print(f'maxAge : {maxAge}')

indeX = [0 for i in range(maxAge+1)]
print(indeX)
print(len(indeX))

for a in age:
       indeX[a] += 1




while True:
    maxBin = max(indeX)
    maxBinIdx = indeX.index(maxBin)

    if maxBin == 0:
        break

    print(f'{maxBinIdx}세 빈도수 : {maxBin}' + '*' * maxBin)
    indeX[maxBinIdx]=0





