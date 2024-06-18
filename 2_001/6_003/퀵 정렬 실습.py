import random

var=random.sample(range(1,101),10)

def qSort(ns,asc=True):

    if len(ns) < 2 :
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    smallVal = []
    sameVal = []
    bigVal = []

    if asc:
        for n in ns:
            if n < midVal:
                smallVal.append(n)
            elif n == midVal:
                sameVal.append(n)
            else:
                bigVal.append(n)

        return qSort(smallVal, asc=asc) + sameVal + qSort(bigVal, asc=asc)

    else:
        for n in ns:
            if n < midVal:
                smallVal.append(n)
            elif n == midVal:
                sameVal.append(n)
            else:
                bigVal.append(n)

        return qSort(bigVal, asc=asc)+ sameVal + qSort(smallVal, asc=asc)


print(qSort(var,asc=False))
