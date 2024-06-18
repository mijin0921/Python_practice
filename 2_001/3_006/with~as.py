#파일 닫기를 생략하자!

# with~as 문을 이용하면 파일 닫기를 생략할 수 있다.

# file = open(uri + '/hello.txt','a')
# file.write('\n그다음 날도 계속 쭉 화이팅')
# file.close()
uri='C:/파이썬.ex/파이썬txt'
#
# with open(uri + '/hello.txt','a') as f:
#     f.write('\n내년까지 화이팅!')
#
# # 위 문단이랑 같은 의미임. close문 생략됨
#
# with open(uri + '/hello.txt','r') as f:
#     print(f.read())

# 응용 : 로또 번호
import random

#1.함수 만들기 (텍스트 파일 안에 리스트에 담긴 번호를 쓰는 기능)

nums = random.sample(range(1,46),7)
print(nums)

def lotto(nums):
        for idx,num in enumerate(nums):
            with open(uri + '/lotto.txt', 'a') as l:
                if idx < (len(nums)-2):
                    l.write(str(num) + ',')
                elif idx == (len(nums)-2):
                    l.write(str(num))
                elif idx == (len(nums)-1):
                    l.write('\n')
                    l.write('Bonus:'+ str(num))
                    l.write('\n')

lotto(nums)






