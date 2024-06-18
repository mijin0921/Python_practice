#예외란 문법적인 문제는 없으나 실행 중 발생하는 예상하지 못한 문제
# 프로그램은 실행하지만, 소프트웨어적으로 해결할 수 없는 문제

# 파이썬에는 예외마다 담당하는 클래스가 있다.

# print(10/0)

# print(int('hello'))

# 예외처리 :발생된 예외를 별도 처리함으로써 프로그램 전체의 실행에 문제가 없도록

# 예외 발생 예상 구문을 try~except로 감싼다.
#
# n1=10 ; n2=0
#
# try:  #만약 예외가 발생하지 않으면 정상 실행됨
#  print(n1 / n2)
# except:
#     print('에러가 발생했습니다')
#     print('다른 프로그램으로 넘어가겠습니다')
#
# print(n1 * n2)
# print(n1 - n2)
# print(n1 + n2)
#
# # 사용자가 숫자가 아닌 문자로 입력하면 예외처리 하는 코드
#
# nums =[]
#
# n=1 #횟수
# while n<6:
#
#     try:
#        var= int(input('숫자를 입력하시오 : ')) #반복하고 싶은 기능 입력
#     except:
#        print('문자는 숫자로 캐스팅 불가합니다')
#        continue #문자는 카운트 하지 않도록
#
#     nums.append(var)
#     n +=1  #무한루프 방지
#
# print(nums)

# try~except~else 구문
# ~else 구문 : 예외가 발생하지 않으면 실행한다 , 다만 꼭 필요한 것은 아님

eve = []
odd = []
rea = []

n =1
while n<6:
    try:
        num= float(input('숫자를 입력하시오 : '))
    except:
        print('숫자가 아닙니다.다시입력하세요.')
        continue

    else:
        if num - int(num) !=0:
            rea.append(num)
        else:
            if num % 2 == 0:
                eve.append(num)

            else:
                odd.append(num)

        n += 1


print(eve)
print(odd)
print(rea)

