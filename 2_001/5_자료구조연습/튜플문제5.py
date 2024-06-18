# students = ({'cls01' : 18},
# {'cls02' : 21},
# {'cls03' : 20},
# {'cls04' : 19},
# {'cls05' : 22},
# {'cls06' : 20},
# {'cls07' : 23},
# {'cls08' : 17})
#
# students=list(students)
#
# def cal(n):
#     totalN = 0
#     avrN =0
#     minN = ''
#     max = ''
#
#     for i in n:
#         for key in i.keys():
#             totalN += i[key]
#
#
#     print(totalN)
#     avrN = int(totalN / len(n))
#     print(avrN)
#
#     n.sort()
#     print(n[0])
#     print(n[7])
#
#     for i in n:
#         for key in i.keys():
#             ven = avrN - i[key]
#             print(ven)
#
#
# cal(students)




students = [
    {'cls01': 18},
    {'cls02': 21},
    {'cls03': 20},
    {'cls04': 19},
    {'cls05': 22},
    {'cls06': 20},
    {'cls07': 23},
    {'cls08': 17}
]

def cal(n):
    totalN = 0
    avrN = 0
    minC = ''
    maxC = ''
    minN = 0
    maxN = 0

    for i in n:
        for key in i.keys():
            totalN += i[key]

            if i[key] > maxN:
                maxN = i[key]
                maxC = key

            if minN > i[key] or minN == 0:
                minN = i[key]
                minC = key



    print(f'전체 학생 수 : {totalN}')
    avrN = int(totalN / len(n))
    print(f'평균 학생 수 : {avrN}')
    print(f'최저 학생수 {minC} 학급 : {minN}명')
    print(f'최고 학생수 {maxC} 학급 : {maxN}명')

    #튜플에서 최저 최고는 그냥 비교하는 for문 쓰기

    for i in n:
        for key in i.keys():
            ven = i[key] - avrN
            print(f'{key}의 편차 : {ven}')

cal(students)

# for i in students:
#     for key in i.keys():
#         print(key)
#         print(i[key])
