#순위 : 수의 크고 작음을 이용해서 수의 순서를 정하는 것

import random

var = list(random.sample(range(50,101),20))
print(var)

ranks=[0 for i in range(20)] #20개에 각각 대응하는 순위 자료구조를 생성
print(ranks)

for idx,num in enumerate(var):
    for num2 in var:
        if num < num2:
            ranks[idx] +=1

print(var)
print(ranks)

for idx, num in enumerate(var):
    print(f'num : {num}  \t  rank : {ranks[idx] + 1}')


