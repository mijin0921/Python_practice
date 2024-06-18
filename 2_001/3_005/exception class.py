#Exception은 예외를 담당하는 클래스이다.

# 예를들어 except 뒤에 어떤 문장을 사용자가 직접 입력하는 경우 왜 예외가 발생했는지 모름
# 그래서 Exception 클래스로 예외 내용을 출력하게 하는 것
#
# num1 = int(input('input number1 : '))
# num2 = int(input('input number2 : '))
#
# try:
#     print(f'num1 / num2 : {num1/num2}')
#
# except:
#     print('에러입니다.')
#
#
# print(f'num1 + num2 : {num1 + num2}')
#
# # Exception 클래스 사용
#
# try:
#     print(f'num1 / num2 : {num1 / num2}')
#
# except Exception as e:
#     print(f'{e}')
#
# print(f'num1 + num2 : {num1 + num2}')
#
# # raise 키워드를 이용하면 강제로 예외를 발생시킬 수 있다.
#
def message(m):

    if len(m)<=10:
        print('SMS 발송')
    else:
        raise Exception('10글자를 초과하였습니다.')


msg=input('문자를 입력하시오 : ')

try:
    message(msg)
except Exception as e:
    print(f'{e}')
    print('MMS 발송')



# 사용자 예외 클래스
# Exception 클래스를 상속해서 사용자 예외 클래스를 만들 수 있다.
#
class NotuseZoreExcep(Exception):

    def __init__(self,n):
        super().__init__(f'{n}은 사용할 수 없습니다.')


def divcalculator(n1,n2):

    if n2 == 0:
        raise NotuseZoreExcep(n2)

    else:
        print(f'{n1}/{n2} = {n1 / n2}')

num1 = int(input('input number1 : '))
num2 = int(input('input number2 : '))

try:
    divcalculator(num1,num2)

except NotuseZoreExcep as n:
    print(n)

# 응용

class PasswordLengthShort(Exception):
    def __init__(self,str):
        super().__init__(f'{str}: 길이 5미만')

class PasswordLengthLong(Exception):
    def __init__(self,str):
        super().__init__(f'{str}: 길이 10초과')

class PasswordWorng(Exception):
    def __init__(self,str):
        super().__init__(f'{str}: 잘못된 비밀번호')

user= input(' 패스워드를 입력하시오 : ')


def password(p):

    if len(p)<5:
        raise PasswordLengthShort(p)
    elif len(p)>10:
        raise PasswordLengthLong(p)
    elif user != 'admin1234':
        raise PasswordWorng(p)
    elif user == 'admin1234':
        print('어서오세요')

try:
    password(user)

except PasswordLengthShort as p1:
    print(p1)
except PasswordLengthLong as p2:
    print(p2)
except PasswordWorng as p3:
    print(p3)