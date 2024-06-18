import copy

def insertp(ns,deepCopy=True,asc=True):

    if deepCopy:
        cns =copy.copy(ns)

    else:
        cns=ns

    if asc:
        for n1 in range(1,len(cns)):
            n2 = n1 -1
            cnt = cns[n1]

            while n2 >=0 and cns[n2] > cnt:
                cns[n2+1] = cns [n2]
                n2 -=1

            cns[n2+1] = cnt
            print(cns)

    else:
        for n1 in range(1, len(cns)):
            n2 = n1 - 1
            cnt = cns[n1]

            while n2 >= 0 and cns[n2] < cnt:
                cns[n2 + 1] = cns[n2]
                n2 -= 1

            cns[n2 + 1] = cnt
            print(cns)

    return cns







