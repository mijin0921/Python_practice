#파일 모드는 파일을 어떤 목적으로 open할지 정한다.
# w: 쓰기 전용 a:쓰기 전용(기존에 내용이 있으면 덮어씌우지 않고 추가한다.)  x:쓰기 전용 (기존에 파일이 있으면 에러발생)  r:읽기 전용 (파일이 없으면 에러발생)

uri='C:/파이썬.ex/파이썬txt'

file = open(uri + '/hello.txt','w')
file.write('오늘도 화이팅,내일도')
file.close()


file = open(uri + '/hello.txt','a')
file.write('\n그다음 날도 계속 쭉 화이팅')
file.close()


# file = open(uri + '/hello_2.txt','x')
# file.write('\n그다음 날도 계속 쭉 화이팅')
# file.close()

file = open(uri + '/hello_2.txt','r')
str=file.read()
print(str)
file.close()