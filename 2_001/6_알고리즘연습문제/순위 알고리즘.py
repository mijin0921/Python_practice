import random

def rank():

    var = random.sample(range(50,101),20)
    rankIdx = [0 for i in range(20)]

    for idx,n1 in enumerate(var):
        for n2 in var:
            if n1 < n2:
                rankIdx[idx] +=1

    #우선 랭크를 오름차순 정렬하자

    for i in range(len(rankIdx)-1):
        minIdx= i

        for j in range(i+1,len(rankIdx)):
            if rankIdx[minIdx] > rankIdx[j]:
                minIdx = j

            rankIdx[i],rankIdx[minIdx]=rankIdx[minIdx],rankIdx[i]
            var[i],var[minIdx]= var[minIdx],var[i]



    # 풀이
    for i,n in enumerate(var):
        print(f'num : {n}  rank : {rankIdx[i]+1}')


    print(var)
    print(rankIdx)


rank()

