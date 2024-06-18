nums = [4,10,22,5,0,17,7,11,9,61,88]

nums.sort()
print(nums)

searchD = int(input('정수입력 : '))
result = -1

staIdx = 0
endIdx = len(nums) -1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]

while searchD <= nums[endIdx] and searchD >= nums[0]:

    if searchD == nums[endIdx]:
        result = endIdx
        break
        
    elif searchD > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]

    elif searchD < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]

    elif searchD == midVal:
        result = midIdx
        break

print(f'resultIdx : {result}')