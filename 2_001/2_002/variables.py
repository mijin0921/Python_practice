fNum= 3.14
fNum2= 0.123

print(fNum+fNum2)

bo=str(True)

print(bo)
print(type(bo))

# 숫자형 변환

var='100'
var2=100
print(var)
print(var2)

var=int('100')
var2=float(100)
print(type(var))
print(type(var2))

bo=int(True)

print(bo)
print(type(bo))

# 빈문자 vs 공백 문자 (공백 데이터 있음)
# 공백문자 -> 논리형

var3 =''

print(var3)
print(type(var3))

var3 =bool(var3)

print(var3)
print(type(var3))

var4=' '

print(var4)
print(type(var4))

var4=bool(var4)

print(var4)
print(type(var4))

# 문자->논리형->산술연산

a1='True'
a2='False'

print(type(a1))
print(type(a2))

a1=bool(a1)
a2=bool(a2)

print(a1)
print(a2)
print(a1+a2)

