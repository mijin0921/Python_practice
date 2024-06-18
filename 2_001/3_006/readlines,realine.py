# readlines() : 파일의 모든 데이터를 읽어서 리스트 형태로 반환한다.

# readline() : 한 행을 읽어서 문자열로 반환한다.

uri='C:/파이썬.ex/파이썬txt'

with open(uri + '/hello.txt','r') as h:
    line= h.readline()


    while line != '':
        print(f'{line}',end='')
        line = h.readline()



print('\n')


with open(uri + '/hello.txt','r') as h:
    line2= h.readlines()
    print(set(line2))


# 문자형 함수중에 split() 함수는 특정 문자열 앞뒤로 분리한 다름 '리스트'형태로 반환한다.
# 문자형 함수중에 strip() 함수는 특정 문자열을 버려준다.

print(line2[1:4])

