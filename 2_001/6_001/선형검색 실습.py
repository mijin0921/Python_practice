nums = [4,7,10,2,4,7,0,2,7,3,9]

# searchN= int(input('정수입력 : '))

# result = -1
#
# n=0
# while True:
#     if nums[n] == searchN:
#         result = n
#         break
#     n+=1
#
# print(result)

def idx(data):
    searchN = int(input('정수입력 : '))
    resultD = []
    n = 0
    while True:
        if data[n] == searchN:
            resultD.append(n)
            print(f'Index : {n}')

        n += 1

        if n == len(data) - 1:
            break

    print(f'개수 : {len(resultD)}')

idx(nums)