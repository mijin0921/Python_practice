scores = [8.9, 7.6, 8.2, 9.1, 8.8 ,8.1, 7.9, 9.4, 7.2, 8.7]

ranks =[9.12,8.95, 8.12, 7.90, 7.88]

total =0

for s in scores:
    total += s

avr = round(total / len(scores),2)
ranks.append(avr)

#순위 알고리즘 사용!

# rankIdx = [0 for i in range(len(ranks))]
#
# for idx,n1 in enumerate(ranks):
#     for n2 in ranks:
#         if n1 < n2:
#             rankIdx[idx] +=1

# 삽입정렬 알고리즘 사용
for n1 in range(1,len(ranks)):
    n2 = n1 - 1
    cnt = ranks[n1]

    while ranks[n2] > cnt and n2 >=0:
        ranks[n2+1] = ranks[n2]
        n2 -=1

    ranks[n2+1] = cnt

print(ranks)



# print(avr)
# for idx,r in enumerate(rankIdx):
#     print(f'순위 : {r+1}  점수 : {ranks[idx]}')


