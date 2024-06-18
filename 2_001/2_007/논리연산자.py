#논리연산자 and,or,not

print('{} and {} : {}'.format(True,True,(True and True)))
print('{} or {} : {}'.format(True,False,(True or True)))
print('not {} : {}'.format(True,(not True)))
print('not {} : {}'.format(False,(not False)))

#
# age = int(input('나이를 입력하세요 : '))
#
# print('백신 접종 대상자 여부 : {}'.format(age<20 or age>=65))

ko=int(input('국어 점수를 입력하세요 : '))
en=int(input('영어 점수를 입력하세요 : '))
mth=int(input('수학 점수를 입력하세요 : '))
avg=(ko+en+mth)/3

print('평균점수 : {}'.format(avg))
print("국어: {} , 영어 : {} , 수학 : {} ,평균 : {}".format((ko>=60),(en>=60),(mth>=60),(avg>=70)) )
print("결과 : {}".format((ko>=60)and(en>=60)and(mth>=60)and(avg>=70)))
