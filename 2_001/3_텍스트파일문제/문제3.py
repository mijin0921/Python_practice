uri = 'C:/파이썬.ex/파이썬txt/'
inputNum=int(input('정수를 입력하시오 : '))


def writeNum(n):
    nums = []
    with open(uri + 'practice3.txt', 'a') as p:
        for i in range(1, n + 1):
            if n % i == 0:
                nums.append(i)

        p.write(f'{n}의 약수 : {nums}')
        p.write('\n')
        print('divisor write complete! ')


writeNum(inputNum)

def writeMin(n):
    with open(uri+'practice3_1.txt','a') as p:
        nums=[]
        for i in range(2,n+1):
            flag = True
            for m in range(2,i):
                if i % m == 0:
                    flag = False
                    break
            if flag:  #들여쓰기 조심!!!
                nums.append(i)

        p.write(f'{n}까지의 소수 : {nums}')
        p.write('\n')
        print('prime write complete!')

# for i in range(2,var+1):
# #     flag = True
# #     for n in range(2,i):
# #         if i % n == 0:
# #             flag = False
# #             break
# #     if flag:
# #         print(f'{i}는 소수')
# #         n2.append(i)
#
#
# print(n2)


writeMin(inputNum)