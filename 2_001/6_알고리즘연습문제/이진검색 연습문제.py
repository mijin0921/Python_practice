#이진 검색 : 정렬되어 있는 데이터에서 중앙값과 크고 작음을 이용해서 검색한다(단 정렬이 되어 있어야함)

nums = [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]


staIdx = 0
endIdx = len(nums) -1

midIdx = (staIdx+endIdx) // 2
midVal = nums[midIdx]

resultIdx = -1
inputNum = int(input('inputN : '))

while inputNum >= nums[0] and inputNum <= nums[endIdx]:

    if inputNum == midVal:
        resultIdx = midIdx
        break

    elif inputNum > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif inputNum < midVal:
        endIdx = midIdx #여기서 순서 바꿔서 할댕했더니 무한루프에 빠짐...ㄷㄷ
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif inputNum == nums[endIdx]:
        result = endIdx
        break


print(resultIdx)