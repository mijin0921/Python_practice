#병합 정렬 : 자료구조를 분할하고 각각의 분할된 자료구조를 정렬한 후 다시 병합하여 정렬
# 1. 분할  2. 정렬  3. 병합


def mSort(ns):
    # 분할단계
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx])
    rightNums = mSort(ns[midIdx:len(ns)])

    # 병합단계
    mergeNums = []
    leftIdx =0 ; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if leftNums[leftIdx] < rightNums[rightIdx]:
            mergeNums.append(leftNums[leftIdx])
            leftIdx +=1

        else:
            mergeNums.append(rightNums[rightIdx])
            rightIdx +=1


    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]
    print(mergeNums)
    return mergeNums










nums = [8,1,4,3,2,5,10,6]
# midIdx = len(nums) // 2 #몫
# print(midIdx)
mSort(nums)
