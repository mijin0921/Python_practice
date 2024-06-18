# #if~elif문
#
# score=int(input('점수 입력 : '))
# grade = ''
#
# if score >= 90:
#     grade= 'A'
# elif score >=80:
#     grade='B'
# elif score >=70:
#     grade='C'
# else:
#     grade='F'
#
# print(grade)
#
# # 응용
#
# print('1.카페라테(3.5)\t 2.에스프레소(3.0)\t 3.아메리카노(2.0)\t 4.곡물라테(4.0)')
# menu=int(input('메뉴를 입력하시오: '))
#
# print('-'*20)
# if menu == 1:
#     print('메뉴 : 카페라테\n가격 : 3,500원')
# elif menu ==2:
#     print('메뉴 : 에스프레소\n가격 : 3,000원')
# elif menu ==3:
#     print('메뉴 : 아메리카노\n가격 : 2,000원')
# else:
#     print('메뉴 : 곡물라테\n가격 : 4,000원')
# print('-' * 20)
#
# # 다자택일 사용시 주의할 점
# # 조건식 순서가 중요
#
# # 중첩 조건문 : 조건문 안에 또 다른 조건문이 있을 수 있다. 일반적으로 2단계 까지만 사용
#
# score=int(input('시험 점수 입력 : '))
#
# if score < 60:
#     print('다시 공부하고 오세요')
# else:
#     if score >=90:
#         print('A')
#     elif score >=80:
#         print('B')

# 응용

selectU=int(input('출퇴근 대상자 인가요? 1.yes/ 2.no : '))

if selectU==1:
    mobil=int(input('교통 수단 선택 1.도보,자전거/ 2.버스,지하철/ 3.자가용 : '))
    if mobil == 1:
        print('5% 세금 감면')
    elif mobil == 2:
        print('3% 세금 감면')
    elif mobil == 3:
        print('1% 추가 세금')
else:
    print('세금변동 없음')