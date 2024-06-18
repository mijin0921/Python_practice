#알고리즘? : 어떤 문제를 풀어내기 위한 일련의 절차나 방법
#파이썬의 편리한 기능들이 어떤 절차에 의해서 만들어지는지 확인하는 챕터

# 선형검색 : 선형으로 나열된 데이터를 순차적으로 스캔하여 원하는 값을 찾는다

datas = [3,2,5,7,9,1,0,8,6,4,11]
# searchData = int(input('찾으려는 숫자 입력 : '))
#
# searchRsult = -1
#
# n =0
#
# while True:
#
#     if n == len(datas):
#         searchRsult = -1
#         break
#
#     elif datas[n] == searchData:
#         searchRsult = n
#         break
#
#     n += 1
#
# print(searchRsult)


# 보초법 : 마지막 인덱스에 찾는 겂을 추가해서 찾는 과정을 간략화 한다(검색 성공: 마지막 이전에 검색된 경우/실패 : 마지막에 검색된 경우)
searchData1 = int(input('찾으려는 숫자 : '))

searchRsult = -1

n =0
while True:
    if datas[n] == searchData1:
        if n != len(datas)-1:
            searchRsult = n
            break


print(searchRsult)


