
import random

def scoreF(ss):

    maxNum = 0
    maxNumIdx = 0
    maxNum = ss[0]

    for idx,n in enumerate(ss):
        if maxNum < n:
            maxNum = n
            maxNumIdx = idx

    indexes = [0 for i in range(maxNum+1)]

    for i in ss:
        indexes[i] = indexes[i] + 1



    for id,i in enumerate(indexes):
        if i != 0:
            print(f'{id}의 빈도수 : {i} \t {'*'* i}')



scores=[]

for i in range(100):
    rn = random.randint(71,100)
    if rn != 0 :
        rn= rn - (rn % 5)
        scores.append(rn)


scoreF(scores)



