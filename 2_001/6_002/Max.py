#최댓값

nums = [-2,-4,5,7,10,0,8,20,-11]

class MaxAlgo:
    def __init__(self,ns):
        self.nums= ns
        self.maxNum = 0

    def getMaxNum(self):
        self.maxNum = self.nums[0]

        for i in self.nums:
            if self.maxNum < i:
                self.maxNum = i

        return self.maxNum



class MaxAsCode(MaxAlgo):

    def __init__(self,ns):
        super().__init__(ns)

    def getMaxNum(self):
        self.maxNum = self.nums[0]

        for i in self.nums:
            if ord(self.maxNum) < ord(i):
                self.maxNum = i

        return self.maxNum

    def printResult(self):

        print(f'result : {self.maxNum}')
        print(f'codeNum : {ord(self.maxNum)}')

    def printAll(self):
        for i in self.nums:
            print(f'code : {i} -> {ord(i)}')




