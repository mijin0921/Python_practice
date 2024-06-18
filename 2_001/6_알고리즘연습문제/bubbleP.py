import copy

def bubble(ns,deepCopy=True,asc= True):

    if deepCopy:
        cns = copy.copy(ns)

    else:
        cns = ns


    length = len(ns)-1

    for i in range(length):
        for j in range(length-i):
            if asc:
                    if cns[j]> cns[j+1]:
                        cns[j] , cns[j + 1] = cns[j+1], cns[j]
                    print(cns)

            else:
                    if cns[j] < cns[j + 1]:
                        cns[j], cns[j + 1] = cns[j + 1], cns[j]
                    print(cns)


    return cns









