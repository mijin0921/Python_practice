#등차수열

def discount():
    baby=int(input('유아는 몇 명인가요? : '))
    dbaby=int(input('할인대상 유아는 몇 명인가요? : '))
    child=int(input('소아는 몇 명인가요? : '))
    dchild=int(input('할인대상 소아는 몇 명인가요? : '))
    adult=int(input('성인은 몇명인가요? : '))
    dadult=int(input('할인대상 성인은 몇 명인가요? : '))
    babyPrice = baby * 18000
    childPrice = child * 25000
    adultPrice = adult * 50000
    discountPrice1= int(18000*0.5*dbaby)
    discountPrice2=int(25000*0.5*dchild)
    discountPrice3= int(50000*0.5*dadult)
    total = baby + child + adult + dbaby +dchild + dadult
    totalPrice= babyPrice+ childPrice+ adultPrice + discountPrice1+discountPrice2+discountPrice3

    def formatNum(n):      #포맷의 반복을 효울적으로 줄이기 위해 함수 선언
        return format(n,   ',')

    print('='*25)
    print(f'유아 {baby}명 요금 : {formatNum(babyPrice)}원')
    print(f'유아 할인 대상 {dbaby}명 요금 : {formatNum(discountPrice1)}원')
    print(f'소아 {child}명 요금 : {formatNum(childPrice)}원')
    print(f'소아 할인 대상 {dchild}명 요금 : {formatNum(discountPrice2)}원')
    print(f'성인 {adult}명 요금 : {formatNum(adultPrice)}원')
    print(f'성인 할인 대상 {dadult}명 요금 : {formatNum(discountPrice3)}원')
    print('=' * 25)
    print(f'Total : {total}명')
    print(f'TotalPrice : {formatNum(totalPrice)}원')
    print('=' * 25)


discount()


