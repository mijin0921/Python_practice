# 모듈 : 함수가 선언되어 있는 파이썬 파일
# 이미 만들어진 훌륭한 기능으로 사용자는 쉽게 사용할 수 있다.
# 파이썬에서는 기본으로 계산 ,난수, 날짜/시간 모듈이 있다.

# 빅데이터 분석에 Pandas 외부 모듈이 쓰인다!

# random 모듈

import random

var=random.randint(1,10)
print(var)
print(type(var))

# random 모듈을 이용해서 0부터 100까지 난수 10개를 발생시킬 때

var2=random.sample(range(0,101),10)
print(var2)
print(type(var2))