import copy

def bubbleSort(ns ,deepCopy = True):

    if deepCopy:
        cns = copy.copy(ns) #깊은 복사로 정렬을 할것인지
    else:
        cns = ns #얕은 복사로 정렬할 것인지

    length = len(cns) - 1
    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j+1]:
                cns[j] , cns[j + 1] = cns[j+1], cns[j]

    return cns




