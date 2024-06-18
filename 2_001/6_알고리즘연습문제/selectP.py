import copy

def select(ns,deepCopy=True):

    if deepCopy:
        cns = copy.copy(ns)

    else:
        cns = ns


    for i in range(len(cns)-1):
        minIdx = i

        for j in range(i+1,len(cns)):
            if cns[minIdx] > cns[j]:
                minIdx = j

        cns[i] ,cns[minIdx] = cns[minIdx], cns[i]
        print(cns)


    return cns



