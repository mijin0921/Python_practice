import random
import copy

class SelectSorted:

    def __init__(self,ss,asc=True):
        self.scores = ss
        self.ranks = []
        self.isAsc = asc   # 수정: 생성자에서 받은 asc 값을 isAsc에 저장

    def copyScore(self):
        self.ranks = copy.deepcopy(self.scores)
        return self.ranks

    def setSelectedSort(self):
        self.copyScore()

        if self.isAsc:
            for i in range(len(self.ranks) - 1):
                minIdx = i

                for j in range(i + 1, len(self.ranks)):
                    if self.ranks[minIdx] > self.ranks[j]:
                        minIdx = j

                self.ranks[i], self.ranks[minIdx] = self.ranks[minIdx], self.ranks[i]


        else:
            for i in range(len(self.ranks) - 1):
                maxIdx = i

                for j in range(i + 1, len(self.ranks)):
                    if self.ranks[maxIdx] < self.ranks[j]:
                        maxIdx = j

                self.ranks[i], self.ranks[maxIdx] = self.ranks[maxIdx], self.ranks[i]

        return self.ranks


    def getRank(self):
        print(f'result: {self.ranks}')

    def getScores(self):
        print(f'score : {self.scores}')




