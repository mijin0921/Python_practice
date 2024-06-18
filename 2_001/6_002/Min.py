#최소값

nums = [-2,-4,5,7,10,0,8,20,-11]

class MinAlgo:

    def __init__(self,ns):
        self.nums = ns
        self.minNum = 0

    def getMinNum(self):
        self.minNum = self.nums[0]

        for n in self.nums:
            if self.minNum > n:
                self.minNum = n

        return self.minNum


# mi = MinAlgo(nums)
# result= mi.getMinNum()
# print(result)

class MinAsCode(MinAlgo):

    def __init__(self,ns):
        super().__init__(ns)

    def getMinNum(self):
        self.minNum = self.nums[0]

        for n in self.nums:
            if ord(self.minNum) > ord(n):
                self.minNum = n

        return self.minNum

    def printResult(self):

        self.getMinNum()
        print(f'result : {self.minNum}')
        print(f'codeNum : {ord(self.minNum)}')

    def printAll(self):
        for i in self.nums:
            print(f'code : {i} -> {ord(i)}')

