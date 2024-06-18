#복리 계산기
# money=int(input('금액을 입력하시오 : '))
# interstRatio=float(input('이율을 입력하시오: '))
# period=int(input('기간을 입력하시오 : '))
# total=money
#
#
# for i in range(period):
#     total += total*interstRatio*0.01
#
# totalMoney=int(total)
#
# print('-'*30)
# print('이율 : {}%\n원금 : {}원\n{}년 후 금액 : {}원'.format(interstRatio,format(money,   ','),period,format(totalMoney,   ',')))
# print('-'*30)

# 백신 접종 프로그램

age=int(input('나이를 입력하시오 : '))

if age >=65 or age <=19:
    yearEnd=int(input('출생년도 끝자리를 입력하시오 : '))
    if yearEnd ==4:
        print('목요일 접종 가능')
    elif yearEnd ==2:
        print('화요일 접종 가능')
    elif yearEnd ==0:
        print('금요일 접종 가능')
else:
    print('하반기 일정 확인')

# inch 환산 프로그램

length=int(input('길이(mm)를 입력하시오 : '))
inch=0.039

print('인치로 환산한 길이 : {}inch'.format(length*inch))