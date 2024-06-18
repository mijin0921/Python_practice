#2개 이상의 클래스를 상속한다.

# 다중 상속 방법 : 클래스 만들 때 () 안에 상속받고 싶은 클래스 명 나열

class Car1:

    def drive(self):
        print('drive!')

class Car2:

    def swim(self):
        print('swim~')

class Car3:

    def fly(self):
        print('fly')

class CarF(Car1,Car2,Car3):

    def __init__(self):
        pass

future=CarF()

future.drive()
future.swim()
future.fly()