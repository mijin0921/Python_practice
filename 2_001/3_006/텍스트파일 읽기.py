#read()함수를 이용한 파일 문자열 읽기
#
file=open('C:/파이썬.ex/파이썬txt/todo.txt','w')

str=file.read()
#파일을 읽을 때는 숫자건 문자건 무조건 문자열로 읽어온다

print(str)

file.close()

import time

lt= time.localtime()

dateStr= time.strftime('%Y-%m-%d %H:%M:%S %p')
#time.strftime()함수는 시간,날짜 등은 내가 원하는 대로 조합할 수 있는 함수다

today = input('오늘의 일정 : ')

file.write(dateStr+ today)
file.close()


# 응용 : 특정 글자 다른 글자로 바꾸기 replace함수

file=open('C:/파이썬.ex/파이썬txt/todo.txt','r')

str=file.read()
#파일을 읽을 때는 숫자건 문자건 무조건 문자열로 읽어온다
file.close()

str= str.replace('스타벅스','투썸',3)

print(str)


file=open('C:/파이썬.ex/파이썬txt/todo.txt','w')

file.write(str)
file.close()


