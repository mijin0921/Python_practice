class NomalCar:

   def drive(self):
       print('[NormalCar] drive() called!')

   def back(self):
       print('[NormalCar] back() called!')


class TurboCar(NomalCar):  #NomalCar 클래스를 상속한 것!

    def turbo(self):
        print('[TurboCar] turbo() called!')



mycar=TurboCar()

mycar.turbo()
mycar.drive()
mycar.back()

