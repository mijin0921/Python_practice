#버블 정렬 : 처음부처 끝까지 인접하는 인덱스의 값을 순차적으로 비교하면서 큰 숫자를 가장 끝으로 옮기는 것
# 즉, 끝에서부터 차례대로 정렬이 이루어짐


nums = [10,2,7,21,0]
print(nums)

length = len(nums) - 1 #이미 정렬된 횟수는 차감하기 위해
for i in range(length):
    for j in range(length-i): #이미 정렬된 횟수는 차감하고 나머지 숫자들로만 비교하도록 한다
        if nums[j] > nums[j+1]:
            nums[j] , nums[j + 1] = nums[j + 1], nums[j]

        print(nums)
    print()


print(nums)