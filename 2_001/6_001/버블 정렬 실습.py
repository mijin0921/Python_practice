import random
from bubbleMod import bubble as bb

students = []

for i in range(20):
    students.append(random.randint(170, 185))

print(students)

sortesStu=bb.bubbleSort(students,deepCopy=False)
print(students)
print(sortesStu)
