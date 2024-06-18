# #파이썬의 함수는 수학의 함수와 동일하다.
#
# def add(x,y):
#     return x + y
#
# print(add(3,4))
#
#
# #파이썬에는 기본제공된 내장함수와 사용자가 직접 선언하는 사용자 함수가 있다.
#
# #함수는 코드의 중복을 피하고 효율적으로 재사용 하기 위해서 사용한다.
#
# #함수 선언하기
# def well(name):
#     print('{}아 오늘도 화이팅!'.format(name))
#
# well('미진')
#
# def cheer():
#     ment=input('이름을 입력하시오 : ')
#     print('{},너는 세상에서 가장 아름다워'.format(ment))
#
# #함수 호출
# cheer()
# cheer()
# cheer()

def calfunc():
    n1=int(input('정수를 입력하시오 : '))
    n2=int(input('정수를 입력하시오 : '))

    print(n1*n2)
    print(round(n1/n2,2)) #소수점 자리수 정하는 함수 round

calfunc()