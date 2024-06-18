class RankDeviation:

    def __init__(self,mss,ess):
        self.midScore = mss
        self.endScore = ess
        self.midRanks = [0 for i in range(len(mss))]
        self.endRanks = [0 for i in range(len(ess))]
        self.rankDeviation = [0 for i in range(len(mss))]

    def setRank(self,ss,rs):

        for idx,score in enumerate(ss):
            for score2 in ss:
                if score < score2:
                    rs[idx] +=1

    def setMidRank(self):
        self.setRank(self.midScore,self.midRanks)

    def setEndRank(self):
        self.setRank(self.endScore, self.endRanks)

    def getMid(self):
       return self.midScore

    def getEnd(self):
        return self.endScore

    def rankDeviationResult(self): #클래스 이름과 메서드 이름은 다르게 정의해야함!!!!
        for idx,midrank in enumerate(self.midRanks):
            deviation = midrank - self.endRanks[idx]

            if deviation < 0:
                print(f'mid_rank : {midrank} \t end_rank : {self.endRanks[idx]} \t Deviation : {'↓'+ str(abs(deviation))}')
            elif deviation > 0:
                print(f'mid_rank : {midrank} \t end_rank : {self.endRanks[idx]} \t Deviation : {'↑'+ str(abs(deviation))}')
            else:
                print(f'mid_rank : {midrank} \t end_rank : {self.endRanks[idx]} \t Deviation : {'='+ str(abs(deviation))}')

