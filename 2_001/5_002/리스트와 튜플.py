#리스트와 튜플은 자료형 변환이 가능하다

students = ('시노부','카나에','카나오','아오이','칸로지',20,18,17,19)

print(students)
print(type(students))

students = list(students)

print(students)
print(type(students))

students = tuple(students)

print(students)
print(type(students))

#튜플은 () 생략하고 선언 가능하다

blackpink = '제니','로제','리사','지수'

print(blackpink)
print(type(blackpink))

# 실습
playerScore = (9.5,8.9,9.2,9.8,8.8,9.0)

playerScore = list(playerScore)
print(playerScore)

playerScore.sort()
print(playerScore.pop())
print(playerScore.pop(0))
print(playerScore)

totalN = 0
avgN = 0

for i in playerScore:
    print(i)
    totalN += i

print(f'총점 : {int(totalN)}')

avgN = int(totalN / len(playerScore))

print(f'평균 : {avgN}')

playerScore = tuple(playerScore)
print(type(playerScore))

