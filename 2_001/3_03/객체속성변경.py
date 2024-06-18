class NewPc:

    def __init__(self, name, cpu, memory, ssd):
        self.name = name #왼쪽은 객체에 속해있는 속성이고 오른쪽은 init함수의 매개변수 이다.
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print('Excel run')

    def printInfo(self):
        print(f'self.name : {self.name}')
        print(f'self.cpu : {self.cpu}')
        print(f'self.memory : {self.memory}')
        print(f'self.ssd : {self.ssd}')


mypc=NewPc('mypc','I5','16G','25G')

mypc.printInfo()

# 속성값을 변경하는 법
# 변수를 이용해서 조작한다

mypc.cpu = 'I9'
mypc.name = '미진이꺼'

mypc.printInfo()


# 객체와 메모리

# 레퍼런스 변수에는 객체의 메모리 '주소'가 저장된다.
# 예를들어 하나의 레퍼런스 주소를 또 다른 레퍼런스 주소에 할당하면 동일한 객체 메모리 주소를 두개의 변수가 가지고 있는 것이다.
# copy()함수를 사용하면 객체가 원본을 유지한 채로 복사된다.
# mypc1=mypc 이렇게 복사해도 된다

cnt = 0
for i in range(1,2):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수입니다.'.format(i))
    cnt += 1


print(cnt)

# 1부터 10까지의 숫자 중에서 5를 찾는 예시

for i in range(1, 4):
    print(i)
    if i == 5:
        print("5를 찾았습니다!")
        break
else:
    print("5를 찾지 못했습니다.")
