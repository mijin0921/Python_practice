#모듈 : 누군가 이미 만들어 놓은 훌륭한 기능
# operator : 산술 연산자 관련 함수

import operator

num1 = 8
num2 = 5

print("{} + {} : {}".format(num1,num2,operator.add(num1,num2)))
print("{} - {} : {}".format(num1,num2,operator.sub(num1,num2)))
print("{} * {} : {}".format(num1,num2,operator.mul(num1,num2)))
print("{} / {} : {}".format(num1,num2,operator.truediv(num1,num2)))
print("{} % {} : {}".format(num1,num2,operator.mod(num1,num2)))
print("{} // {} : {}".format(num1,num2,operator.floordiv(num1,num2)))
print("{} ** {} : {}".format(num1,num2,operator.pow(num1,num2)))

print("{} == {} : {}".format(num1,num2,operator.eq(num1,num2)))
print("{} != {} : {}".format(num1,num2,operator.ne(num1,num2)))
print("{} > {} : {}".format(num1,num2,operator.gt(num1,num2)))
print("{} >= {} : {}".format(num1,num2,operator.ge(num1,num2)))
print("{} < {} : {}".format(num1,num2,operator.lt(num1,num2)))
print("{} <= {} : {}".format(num1,num2,operator.le(num1,num2)))

print("{} and {} : {}".format(num1,num2,operator.and_(num1,num2)))
print("{} or {} : {}".format(num1,num2,operator.or_(num1,num2)))
print("not {} : {}".format(num1,num2,operator.not_(num1)))

# 20세 미만, 65세 이상 백신 접종

# age=int(input('나이를 입력하시오 : '))
# vaccine=operator.or_(operator.lt(age,20),operator.ge(age,65))
# print("나이 : {} , 백신 접종 : {}".format(age,vaccine))

# 응용2
# 랜덤 난수 1~100 중에 십의자리와 일의 자리가 3의 배수인지 결과 출력
import random

var=random.randint(10,100) #랜덤한 수 추출


result10=operator.floordiv(var,10) #십의 자리수 분리
result1=operator.mod(var,10) #일의 자리수 분리


print(var)
print('십의 자리는 3의 배수이다 : {}'.format(operator.mod(result10,3)==0)) #십의자리수 3의 배수인지 확인
print('일의 자리는 3의 배수이다 : {}'.format(operator.mod(result1,3)==0)) #일의 자리수 3의 배수인지 확인