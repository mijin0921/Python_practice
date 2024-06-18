#선택 정렬 : 가장 작은 데이터를 찾아 그 값을 맨 앞에 위치한 값과 교체하여 정렬

nums = [4,2,5,1,3]

for i in range(len(nums)-1): #인덱스 0 부터 굳이 끝까지 돌 필요없이 끝에서 앞자리까지만 반복하면 됨
    minIdx = i

    for j in range(i+1,len(nums)):
        if nums[minIdx] > nums[j]:
            minIdx = j


    tempNum = nums[i] #최소값이 있는 인덱스와 최초 기준 인덱스를 바꾸는 것!
    nums[i] = nums[minIdx]
    nums[minIdx] = tempNum
    # 간단히 표현하기 
    # nums[i] , nums[minIdx] = nums[minIdx], nums[i]

    print(nums)

