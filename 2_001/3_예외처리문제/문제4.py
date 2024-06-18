#회원가입 프로그램
# 1. 예외처리 클래스 만들기
# 2. 딕셔너리 함수 만들기
# 3. try 문 사용
# 4.사용자 입력값 받기

# class MemberEmpty(Exception):
#
#     def __init__(self,s):
#         super().__init__(f'{s} is empty!')
#
#
# def membership(*mem):
#
#     infoM = {}
#
#     for idx,info in enumerate(mem):
#         if info != True:
#             MemberEmpty(f'{info} is empty!')
#         else:
#             infoM[str(idx)] = info
#
#
#     print(f'm_name : {infoM['0']}')
#     print(f'm_mail : {infoM['1']}')
#     print(f'm_pw : {infoM['2']}')
#     print(f'm_addr : {infoM['3']}')
#     print(f'm_phone : {infoM['4']}')
#
#
#
# name = input('이름 입력 : ')
# mail = input('메일 입력 : ')
# pw = input('비밀번호 입력 : ')
# addr = input('주소 입력 : ')
# phone = input('연락처 입력 : ')
#
# try:
#     membership(name, mail, pw, addr, phone)
#     print('Membership completed!!')
# except MemberEmpty as m:
#     print(m)

class MemberEmpty(Exception):
    def __init__(self, s):
        super().__init__(f'{s} is empty!')

def membership(a,b,c,d,e):
    infoM = {}

    for idx, info in enumerate(a,b,c,d,e):  # enumerate함수는 이렇게 사용할 수 없기 때문에 if~eles문으로 하나하나 코딩해야함
        if info == '':  # 정보가 비어있는 경우 예외 발생
            raise MemberEmpty(f'{info}')
        else:
            infoM[str(idx)] = info  # 정보를 딕셔너리에 할당

    print(f'm_name : {infoM["0"]}')  # 딕셔너리 키를 문자열로 사용하여 수정
    print(f'm_mail : {infoM["1"]}')
    print(f'm_pw : {infoM["2"]}')
    print(f'm_addr : {infoM["3"]}')
    print(f'm_phone : {infoM["4"]}')

name = input('이름 입력 : ')
mail = input('메일 입력 : ')
pw = input('비밀번호 입력 : ')
addr = input('주소 입력 : ')
phone = input('연락처 입력 : ')

try:
    membership(name, mail, pw, addr, phone)
    print('Membership completed!!')
except MemberEmpty as m:
    print(m)

# gpt
# enumerate함수는 이렇게 사용할 수 없기 때문에 if~eles문으로 하나하나 코딩해야함
class MemberEmpty(Exception):
    def __init__(self, s):
        super().__init__(f'{s} is empty!')

def membership(name, mail, pw, addr, phone):
    infoM = {}

    if name == '':
        raise MemberEmpty('Name')
    else:
        infoM['0'] = name

    if mail == '':
        raise MemberEmpty('Mail')
    else:
        infoM['1'] = mail

    if pw == '':
        raise MemberEmpty('Password')
    else:
        infoM['2'] = pw

    if addr == '':
        raise MemberEmpty('Address')
    else:
        infoM['3'] = addr

    if phone == '':
        raise MemberEmpty('Phone')
    else:
        infoM['4'] = phone

    print(f'm_name : {infoM["0"]}')
    print(f'm_mail : {infoM["1"]}')
    print(f'm_pw : {infoM["2"]}')
    print(f'm_addr : {infoM["3"]}')
    print(f'm_phone : {infoM["4"]}')

name = input('이름 입력 : ')
mail = input('메일 입력 : ')
pw = input('비밀번호 입력 : ')
addr = input('주소 입력 : ')
phone = input('연락처 입력 : ')

try:
    membership(name, mail, pw, addr, phone)
    print('Membership completed!!')
except MemberEmpty as m:
    print(m)
