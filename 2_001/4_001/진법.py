#생활에서 사용하는 10진법 외에 프로그램에서 사용하는 다양한 진법

# 파이썬에서 10진수를 X진수로 변환

num = 30

print(f'2진수 : {bin(num)}')
print(f'8진수 : {oct(num)}')
print(f'16진수 : {hex(num)}')

print('2진수 : {}'.format(format(num,'#b')))
print('8진수 : {}'.format(format(num,'#o')))
print('16진수 : {}'.format(format(num,'#x')))

print('{0:#b}, {0:#o} ,{0:#x}'.format(num))

print('2진수 : {}'.format(format(num,'b')))
print('8진수 : {}'.format(format(num,'o')))
print('16진수 : {}'.format(format(num,'x')))

# 반환 결과는 무조건 문자열

# x진수를 10진수로 변경

print('16진수 : {}'.format(int('0x1e',16)))


# 연습문제

inputNUm = int(input('숫자를 입력하시오 : '))

print(f'2진수 변환 : {bin(inputNUm)}')
print(f'8진수 변환 : {oct(inputNUm)}')
print(f'16진수 변환 : {hex(inputNUm)}')

n1 = bin(inputNUm)
n2 = oct(inputNUm)
n3 = hex(inputNUm)

print('2진수 -> 10진수 : {}'.format(int(n1,2)))
print('8진수 -> 10진수 : {}'.format(int(n2,8)))
print('16진수 -> 10진수 : {}'.format(int(n3,16)))

