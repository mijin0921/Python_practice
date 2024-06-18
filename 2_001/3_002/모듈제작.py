#사용자모듈

# 파이썬 파일만 만들어 놓으면 모듈제작이 완성된다.

import calculator

calculator.add(10,20)
calculator.sub(10,20)

# 로또번호 모듈
import lottomuchine

result= lottomuchine.getNum6()
print(result)

# 문자열을 거꾸로 만드는 모듈

import reverseStr

user=input('문자를 입력하시오 ')
user=reverseStr.reverseStr(user)
print(user)