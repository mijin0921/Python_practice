#재귀 알고리즘 : 나 자신을 다시 호출하는 것을 재귀라고 한다
#많이 연습해야함

def recusion(num):

    if num > 0:
        print('*'* num)
        return recusion(num - 1)
    else:
        return 1


recusion(10)

#팩토리얼에서 가장 많이 쓰인다

def fac(n):
  if n > 0:
    return n * fac(n - 1)
  else:
      return 1

print(fac(10))


