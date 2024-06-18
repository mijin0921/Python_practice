#얕은 복사 : 객체 주소를 복사하는 것으로 객체 자체가 복사되지는 않는다.
#깊은 복사 : 객체 자체를 복사하는 것으로 또 하나의 객체가 만들어진다.

# 응용

scores = [8.7,9.1,8.9,9.0,7.9,9.5,8.8,8.3]

total=round(sum(scores),2)
mn =round(total/len(scores),2)
print(total)
print(mn)
print(len(scores))


scoresCopy = scores.copy()

scoresCopy.sort()
scoresCopy.pop(0)
scoresCopy.pop(6)
total2 = round(sum(scoresCopy),2)
mn2 = round(total2/len(scoresCopy),2)
print(total2)
print(mn2)
print(len(scoresCopy))



