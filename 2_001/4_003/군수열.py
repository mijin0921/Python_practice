#군수열 : 여러 개의 항을 묶었을 떄 규칙성을 가지는 수열
#군수열에서 특정 항의 값을 구하기
# 순서 : 1.군집화 하여 규칙성 찾기 2.항의 개수로 일반항 구하기 3.수열의 합 공식 구하기
# 4. 합 공식에서 n을 대입하여 몇군의 n항 값인지 확인

# 파이썬으로 군수열 구현

# inputN = int(input('n입력 : '))
#
# n = 1 ;nCnt = 1;searchN = 1
# # 군의 순서 ; 전체 행의 순서; 사용자가 원하는 행의 값
#
# flag = True
# while flag:
#
#     for i in range(1,n+1):
#         print(f'{i} ',end = '')
#
#
#         nCnt += 1
#         if nCnt > inputN:
#             searchN = i
#             flag = False
#             break
#     print()
#     n += 1
#
# print(f'{inputN}항 : {searchN}')

# 연습 문제

# inputN = int(input('n입력 : '))

n = 1; nCnt =1; searchN = 0;searchP=0; sumN =0
flag = True

while flag:
    for i in range(1,n+1):
        var = i/(n-i+1)
        sumN += var
        print(f'{i}/{n-i+1} ',end='')

        nCnt +=1
        if sumN > 100:
            searchN = i
            searchP = n-i+1
            flag = False
            break
    print()
    n +=1

print(f'{nCnt}번째 항 까지의 합 : {round(sumN,2)}')
print(f'{nCnt}번째 항 : {searchN}/{searchP}')






