#외부 텍스트 파일을 파이썬으로 다루기
# 기본함수 : open(),read(),write(),close()

# 순서: 1.open 2.write or read 3. close

file=open('C:/파이썬.ex/파이썬txt/test.txt','w')
#w모드는 파일을 새로 생성 할 수 있음,하지만 기존의 문자열을 없애고 새로운 문자열로 덮어버림

strCnt= file.write('hello python') #반환형 변수에 저장해도되고 안해도 됨

print(strCnt)

file.close()

# 응용

import time

lt= time.localtime()

dateStr= '['+ str(lt.tm_year) + '년' + str(lt.tm_mon) + '월' +str(lt.tm_mday) + '일]'
today= input('오늘의 일정 : ')

file = open('C:/파이썬.ex/파이썬txt/todo.txt','w')
file.write(dateStr+today)
file.close()

