#객체를 생성하기 위해서 클래스를 만든다
# 클래스는 class키워드와 속성 그리고 기능을 이용해서 만든다

class Car:

    def __init__(self,col,len):
        self.color = col
        self.length= len

    def doStop(self):
        print('Stop')

    def doStar(self):
        print('start')

    def printCarInfo(self):
        print(f'color : {self.color}')
        print(f'length : {self.length}')


# 클래스를 만들었다고 해서 호출했을 때 값이 않는다.객체를 생성해야됌

# 객체를 생성하기 위해 클래스의 생성자를 호출한다

car1=Car('red',200) #객체가 생성된 것임
car2=Car('blue',300) #또 다른 객체가 생성된 것임

#객체가 생성되면 그 안의 속성과 기능에 접근하여 사용할 수 있음

car1.printCarInfo()
car2.printCarInfo()

car1.doStar()
car1.doStop()

# 응용

class Airplane:

    def __init__(self,col,len,wei,hu):
        self.color=col
        self.length=len
        self.weight=wei
        self.human=hu

    def printInfo(self):
        print(f'color: {self.color}')
        print(f'human : {self.human}')
        print(f'length : {self.length}')
        print(f'weight : {self.weight}')

    def printHu(self):
        print(f'이 비행기의 승객수는 {self.human}명 입니다.')



air1=Airplane('bule',1200,5000,300)

air1.printInfo()
air1.printHu()