import random
from insertMod import insert as ins

nums = random.sample(range(1,1001),100)
print(f'not sorted : {nums}')


# 객체생성
sort1=ins.SortNumbers(nums,asc=True)
sort2=ins.SortNumbers(nums,asc=False)

sort1.setSort()
sortedN=sort1.getSortesNumbers()
print(sortedN)

sort2.setSort()
sortedN2=sort2.getSortesNumbers()
print(sortedN2)

print(sort1.getMinNum())
print(sort1.getMaxNum())
print(sort2.getMinNum())
print(sort2.getMaxNum())



