#상위 클래스에서 하위 클래스에 매서드 구현을 강요한다.

# 즉, 상위 클래스에서 어떠한 매서드를 선언만 하고 구현하지 않는다. 그리고 하위 클래스가 동일한 매서드를 구체화 하여 구현한다.는 의미
# 방법

from abc import ABCMeta  #방법
from abc import abstractmethod #방법

class Airplane(metaclass=ABCMeta): #방법

    @abstractmethod  #방법
    def flight(self):
        pass

    def forward(self):
        print('전진')


class Airline(Airplane):

    def __init__(self,c):
        self.color =c

    def flight(self):
        print('비행')

class Jet(Airplane):

    def __init__(self,c):
        self.color =c

    def flight(self):
        print('초고속 비행 후 발사')



al = Airline('red')

al.flight()
al.forward()

# 추상클래스(Airplane)를 쓰는이유 : 특정 기능을 상속 받았을 때 하위클래스들이 각자 알아서 커스텀 해서 쓰도록

j1=Jet('blue')

j1.flight() #출력값이 다름
al.flight()