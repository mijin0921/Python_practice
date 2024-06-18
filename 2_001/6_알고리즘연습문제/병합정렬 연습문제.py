#병합정렬 : 재귀함수를 같이 쓰는 알고리즘이니 반복 연습 필요!

import random
import copy

def mergeP(ns,asc=True):

    if len(ns) < 2:
        return ns #재귀 호출 종료

    midIdx = len(ns) // 2
    leftNums = mergeP(ns[0:midIdx])
    rightNums = mergeP(ns[midIdx:len(ns)])

    mergeNums=[]
    leftIdx = 0; rightIdx =0

    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if leftNums[leftIdx] > rightNums[rightIdx]:

            mergeNums.append(rightNums[rightIdx])
            rightIdx +=1 #이미 작은값으로 지정되어 mergeNums에 들어간 값은 제외하고 비교해야 하기 때문에

        else:
            mergeNums.append(leftNums[leftIdx])
            leftIdx += 1 #이미 작은값으로 지정되어 mergeNums에 들어간 값은 제외하고 비교해야 하기 때문에



    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]
    print(mergeNums)
    return mergeNums


var = random.sample(range(1,100),20)
print(var)

mergeP(var)

