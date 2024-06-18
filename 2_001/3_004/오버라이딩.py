# 매서드를 재정의 한다!

# 응용

class Triangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h

    def area(self):
        return (self.width * self.height)/2

class NewTriangle(Triangle):
    def __init__(self,w,h):
        super().__init__(w,h)

    def area(self): #오버라이딩
        return str(super().area()) + 'cm'



tri=NewTriangle(2,5)

print(tri.area())