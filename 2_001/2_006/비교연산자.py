# 비교 연산자
num3 =10; num4=5

result = num3 > num4
print(result)

result = num3 < num4
print(result)

result = num3 == num4
print(result)

# result = num3 != num4
# print(result)
#
# max1 = 5200
# max2 = 1850
# userInputNumber1=int(input('전장 길이 : '))
# userInputNumber2=int(input('전폭 길이 : '))
#
# print('전장 세차 가능여부 : {}'.format(userInputNumber1<=max1))
# print('전폭 세차 가능여부 : {}'.format(userInputNumber2<=max2))


# 아스키 코드를 활용한 문자 비교연산

cha1= "A" #65
cha2= "S" #83

print('\'{}\' > \'{}\' : \'{}\''.format(cha1,cha2,(cha1>cha2)))

# ord 함수,chr 함수

print('\'A\'-> {}'.format(ord('A')))

print('77-> {}'.format(chr(77)))

# 문자열 자체 비교 == 또는 !=

str1 = 'Hello'
str2 = 'World'

print(str1 == str2)
print(str1 != str2)


