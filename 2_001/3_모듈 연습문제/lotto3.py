import random

lottoChoice = []
matchNum=[]

def lotto():
    global ranLotto
    ranLotto = random.sample(range(1, 46), 7)
    return ranLotto

def choice():
    for i in range(6):
        user = int(input('번호(1~45) 입력 : '))
        lottoChoice.append(user)
    return lottoChoice


def match(n1,n2):
    global matchNum
    for idx,lotto in enumerate(n1):
        for idx2,lotto2 in enumerate(n2):
            if lotto != lotto2:
                continue

            matchNum.append(lotto)

    return matchNum

def lottoResult():
    lotto()
    choice()
    match(ranLotto, lottoChoice)

    if len(matchNum) == 6:
        print('1등 당첨!')
        print(f'기계 번호 : {ranLotto}')
        print(f'보너스 번호 : {ranLotto[6]}')
        print(f'선택 번호 : {lottoChoice}')
        print(f'일치 번호 : {matchNum}')
        
    elif len(matchNum) == 5:
        print('2등 당첨!')
        print(f'기계 번호 : {ranLotto}')
        print(f'보너스 번호 : {ranLotto[6]}')
        print(f'선택 번호 : {lottoChoice}')
        print(f'일치 번호 : {matchNum}')

    elif len(matchNum) == 4:
        print('3등 당첨!')
        print(f'기계 번호 : {ranLotto}')
        print(f'보너스 번호 : {ranLotto[6]}')
        print(f'선택 번호 : {lottoChoice}')
        print(f'일치 번호 : {matchNum}')

    elif len(matchNum) < 4 or len(matchNum) != 0:
        print('다음 기회에ㅠㅠ')
        print(f'기계 번호 : {ranLotto}')
        print(f'보너스 번호 : {ranLotto[6]}')
        print(f'선택 번호 : {lottoChoice}')
        print(f'일치 번호 : {matchNum}')





# 풀이

