#최빈값 : 빈도수가 가장 많은 데이터를 최빈값이라 한다

# 1) 데이터에서 가장 큰 값을 찾는다
# 2) 가장 작은 값부터 최대값 사이의 개수만큼 0이 있는 리스트(indexes) 를 만든다
# 3) 기존 데이터에서 차례대로 비교하며 해당하는 인덱스 값에 +1을 해준다
# indexes에서 가장 많이 더해진 값을 찾는다 -> 이 값의 '인덱스 값'이 데이터에서 최빈값이다.

nums = [1,3,7,6,7,7,7,12,12,17]

indexes = [0 for i in range(17+1)] #0부터 17까지라서 18개

print(indexes)
print(len(indexes))

for n in nums:
    indexes[n] = indexes[n] + 1

print(indexes)

print(f'nums의 최빈값 : {indexes.index(4)}')
print(f'nums의 최빈값의 빈도수 : {max(indexes)}')

