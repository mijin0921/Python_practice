class SortNumbers:

    def __init__(self,ns,asc=True):
        self.nums =ns
        self.isAsc =asc

    def isAscending(self,flag):
        self.isAsc = flag

    def setSort(self):
        for i1 in range(1,len(self.nums)):
            i2 = i1 - 1
            cnt = self.nums[i1]

            if self.isAsc:
                while self.nums[i2] > cnt and i2 >= 0:
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1
            else:
                while self.nums[i2] < cnt and i2 >= 0:
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1

            self.nums[i2+1] = cnt

    def getSortesNumbers(self):
        return self.nums

    def getMinNum(self):
        if self.isAsc:
            return self.nums[0]
        else:
            return self.nums[len(self.nums)-1]

    def getMaxNum(self):
        if self.isAsc:
            return self.nums[len(self.nums)-1]
        else:
            return self.nums[0]




