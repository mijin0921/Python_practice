import random

rNums=random.sample(range(1,101),10)

print(rNums)

def mSort(ns,asc = True):

    if len(ns) < 2:
        return ns


    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx],asc=asc) #재귀함수 호출할 때도 반드시 기본값 같이 호출헤야함!!!
    rightNums = mSort(ns[midIdx:len(ns)],asc=asc)

    mergeNums = []

    leftIdx = 0; rightIdx =0

    while leftIdx < len(leftNums) and rightIdx < len(rightNums):
        if asc:
            if leftNums[leftIdx] < rightNums[rightIdx]: #여기 부등호 바꾸면 내림차순으로 바꿀수 있다!
                mergeNums.append(leftNums[leftIdx])
                leftIdx +=1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx +=1

        else:
            if leftNums[leftIdx] > rightNums[rightIdx]:  # 여기 부등호 바꾸면 내림차순으로 바꿀수 있다!
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1


    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]

    return mergeNums

print(mSort(rNums,asc=False))


