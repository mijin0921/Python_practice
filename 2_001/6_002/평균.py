# import random
#
# nums = random.sample(range(1,101),10)
#
# total = 0
# for i in nums:
#     total += i
#
# avr= total /len(nums)
#
# print(avr)

# 정수들의 평균

num = [4, 5.11, 5, 7.34, 9.1, 3.154, 11, 12, 12.19]
target =[]
total = 0
for n in num:
    if n / int(n) == 1:
        total +=n
        target.append(n)

print(total)
print(target)
avrg = total/ len(target)
print(avrg)