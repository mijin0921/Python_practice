#삽입 정렬 : 이미 정렬된 자료 배열과 비교하여 나의 위치를 찾아서 삽입하기

nums = [5,10,2,1,0]


for i1 in range(1,len(nums)):
    i2 = i1 -1
    ci1 = nums[i1]

    while nums[i2] > ci1 and i2 >=0:
        nums[i2 + 1] = nums[i2] #요소를 오른쪽으로 이동
        i2 -=1 #처음 설정한 ci1이 그 앞에 있는 모든 숫자와 반복해서 비교 되게 함

    nums[i2 + 1] = ci1 #이부분은 아직 모르겠다ㅠㅠ

    print(nums)



