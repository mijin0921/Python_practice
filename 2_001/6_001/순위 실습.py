from rankMod import rank as rm
import random

midScoreStu = list(random.sample(range(50,101),20))
endScoreStu=  list(random.sample(range(50,101),20))

result = rm.RankDeviation(midScoreStu,endScoreStu)

result.setMidRank()
result.setEndRank()

print(result.getMid())
print(result.getEnd())
result.rankDeviationResult()