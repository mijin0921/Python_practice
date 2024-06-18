#객체가 생성될 때 생성자를 호출하면 __init__()가 자동 호출된다.
# __init__()가 속성을 초기화 한다.

# 상위 클래스의 __init__()호출하는 방법 :상위 클래스의 속성을 초기화 하기위해

class P_class:

    def __init__(self,pNum1,pNum2):
        print('[P_class] __init__() called')
        self.pNum1=pNum1
        self.pNum2=pNum2

class C_class(P_class):

    def __init__(self,cNum1,cNum2):
        print('[C_class] __init__() called')

        P_class.__init__(self,cNum1,cNum2) # 상속받은 클래스 매서드 호출 방법 1

        super().__init__(cNum1,cNum2) # 상속받은 클래스 매서드 호출 방법 2

        self.cNum1 = cNum1
        self.cNum2 = cNum2


c=C_class(10,20) #여기까지만 하면 상속받은 P_class의 매서드가 호출이 안됨

c.__init__(1,2)


# 객체 생성에 대해서 좀 더 자세히 알아보자!
# 생성자는 객체가 생성될 때 속성을 초기화 해주는 기능이 있다.

# 중간고사 기말고사

class Mid:

    def __init__(self,s1,s2,s3):
        print('[Mid] __init__() called')
        self.s1=s1
        self.s2=s2
        self.s3=s3

    def midSum(self):
        sum= (self.s1+self.s2+self.s3)
        print(f'midsum : {sum}')

    def midMean(self):
        mean = round((self.s1 + self.s2 + self.s3)/ 3,2)
        print(f'midmean : {mean}')


class End(Mid):

    def __init__(self,s1,s2,s3,s4,s5,s6): #기말고사 객체만 만들면 중간고사 속성까지 초기화 됨
        print('[End] __init__() called')

        super().__init__(s1,s2,s3)

        self.s4=s4
        self.s5=s5
        self.s6=s6

    def sum(self):
        super().midSum() #sum()만 호출하면 중간고사꺼 까지 같이 계산되게

        sum = (self.s4 + self.s5 + self.s6)
        print(f'enddsum : {sum}')

    def mean(self):
        super().midMean()

        mean = round((self.s4 + self.s5 + self.s6)/ 3,2)
        print(f'endmean : {mean}')



my=End(85,95,88,90,99,100)

my.sum()
my.mean()






