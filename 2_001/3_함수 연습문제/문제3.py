# 재귀함수...? : 내가 나를 다시 호출하는 것
#
# user = int(input('정수를 입력하시오 : '))
# def fac(n):
#    for i in range(n-1):
#       n -=1
#       n *= n
#
#    print(n)
#
# fac(user)

# 풀이

def recursionfun(n):

      if n == 1:
         return n

      return n * recursionfun(n - 1)  # 이걸 어떻게 생각해내지????


inputNum=int(input('input number : '))
print(recursionfun(inputNum))


def one(n1,n2,n3):
   print('='*20)
   print(f'예치금 : {n1}원')
   print(f'예치기간 : {n2}년')
   print(f'연 이율 : {n3}%')
   print('-'*20)
   print(f'3년 후 총 수령액 : {n1*(n3*0.01*n2)+n1}원')
   print('=' * 20)

   def two(n1,n2,n3):

      for i in range(1,n2):
         n1+=n1*(n3*0.01)

      print('=' * 20)
      print(f'예치금 : {n1}원')
      print(f'예치기간 : {n2}년')
      print(f'연 이율 : {n3}%')
      print('-' * 20)
      print(f'3년 후 총 수령액 : {n1}')
      print('=' * 20)

   two(n1,n2,n3)

while True:
   money = int(input('예치금 : '))
   term = int(input('기간 : '))
   rate = int(input('연 이율 : '))

   one(money,term,rate)















