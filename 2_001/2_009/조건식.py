# A if 조건식 (true or false) else B
#
# snowAmount = int(input('적설량 입력 : '))
# result = True if snowAmount >= 30 else False
# print('대설량 : {}mm, 대설 경보 발령'.format(snowAmount)) if result else print('대설량 : {}mm, 대설경보 해제'.format(snowAmount))
#
# print('대설량 : {}mm, 대설 경보 발령'.format(snowAmount)) if snowAmount >=30 else (
#     print('대설량 : {}mm, 대설경보 해제'.format(snowAmount)))


# 조건문 ? : 제어문 중 하나, 특정 조건에 따라 프로그램을 분기한다.

# 조건문 기본 if문

# if 10 > 5 :
#     print('10은 5보다 크다')

print('안녕 오늘도 화이팅')


# 응용

# ko=int(input('국어점수 : '))
# en=int(input('영어점수 : '))
# ma=int(input('수학점수 : '))
# avg=(ko+en+ma)/3
#
# if avg >=90 :
#     print('평균 : {}'.format(avg))
#     print('참 잘했어요~!')


# 양자택일 조건문

# passScore= 80
#
# anyScore=int(input('점수 : '))
#
# if anyScore>=passScore :
#     print('PASS')
# else:
#     print('FAIL')

# PASS 키워드 : 나중에 코딩하겠다는 뜻

# if anyScore>=passScore :
#     pass
# else:
#     pass
#
# # len함수 : 문자열의 길이
#
# print(len('안녕하세요'))

# 소수점 첫번쨰 자리에서 반올림하는 프로그램

# floatNum=float(input('숫자를 입력: '))
# num=floatNum-int(floatNum)
#
# if num >= 0.5:
#     print('올림 : {}'.format(int(floatNum)+1))
# else:
#     print('버림 : {}'.format(int(floatNum)))

# 일교차

min=int(input('최저기온 입력 : '))
max=int(input('최고기온 입력 : '))
day=max-min

if day >= 11:
    print('일교차 : {}, 감기 조심하세요'.format(day))
else:
    print('일교차 : {}, 산책하기 좋은 날씨입니다.'.format(day))