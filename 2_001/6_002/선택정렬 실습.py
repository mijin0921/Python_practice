from selectSort import select
import random


score = random.sample(range(50, 101), 20)
score2 = random.sample(range(50, 101), 20)


studentsS = select.SelectSorted(score)
studentsS2 = select.SelectSorted(score2, asc= False)

studentsS.setSelectedSort()
studentsS.getScores()
studentsS.getRank()

studentsS2.setSelectedSort()
studentsS2.getScores()
studentsS2.getRank()




