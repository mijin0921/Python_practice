#퀵 정렬 : 기준값보다 작은값과 큰 값을 분리한다

def qSort(ns):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    smallVal =[] ; sameVal=[] ; bigVal =[]

    for n in ns:
        if n < midVal:
            smallVal.append(n)
        elif n == midVal:
            sameVal.append(n)
        else:
            bigVal.append(n)

    return qSort(smallVal) + sameVal + qSort(bigVal)

nums = [8,1,4,3,2,5,4,10,6,8]

print(qSort(nums))

