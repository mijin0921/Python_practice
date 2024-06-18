#이진 검색 : 정렬되어 있는 데이터에서 중앙값과 크고 작음을 이용해서 검색한다(단 정렬이 되어 있어야함)

datas = [1,2,3,4,5,6,7,8,9,10,11]

print(f'lenght : {len(datas)}')

searchD = int(input('정수 입력 : '))
result = -1

staIdx = 0
endIdx = len(datas)-1
midIdx = (staIdx + endIdx) // 2
midV = datas[midIdx]
print(f'midIdx : {midIdx}')
print(f'midV : {midV}')

while searchD <= datas[len(datas)-1] and searchD >= datas[0]:
    if searchD == datas[len(datas)-1]:
        result = len(datas)-1
        break

    elif searchD > midV:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midV = datas[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midV : {midV}')


    elif searchD < midV:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midV = datas[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midV : {midV}')

    elif searchD == midV:
        result = midIdx
        break


print(f'resultIdx : {result}')




