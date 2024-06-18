#[n:m] 을 이용하면 리스트에서 원하는 아이템을 슬라이싱 하여 뽑을 수 있다
# n <= '' < m

students = ['시노부','카나에','네즈코','기유','탄지로']

print(students[0:2])

# [n:m]으로 문자열도 슬라이싱 할 수 있다

str = 'beggyjeannct'
print(len(str))
print(f'제목 : {str[0:9]}')
print(f'가수 : {str[9:]}')
print(f'제목 : {str[0:-3]}')
print(f'가수 : {str[-3:]}')

# 슬라이싱할 떄 단계를 설정할 수 있다

print(f'{students[0::2]}')
print(f'제목 : {str[0:-3:2]}')

# 슬라이싱을 이용해서 아이템을 변경할 수 있다

students[1:4]={'히메지마','아오이','젠이츠'}
print(students)

#slice()함수 : 아이템을 슬라이싱하는 함수(범위는 [n:m]와 동일)

print(students[slice(0,3)])
print(f'제목 : {str[slice(0,9)]}')


