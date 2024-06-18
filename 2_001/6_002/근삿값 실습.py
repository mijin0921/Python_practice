def scoreG():
    score1 = int(input('kor : '))
    score2 = int(input('eng : '))
    score3 = int(input('mat : '))
    score4 = int(input('sci : '))
    score5 = int(input('his : '))

    limit = [95, 85, 75, 65, 55]

    total = score5 + score4 + score3 + score2 + score1
    avg = round(total / 5, 1)

    nearN = 0
    minN = 95

    for n in limit:
        absNum = abs(n - avg)

        if absNum < minN:
            minN = absNum
            nearN = n

    print(f'Total score : {total}')
    print(f'Avg score: {avg}')

    if nearN == 95:
        print('grade : A')

    elif nearN == 85:
        print('grade : B')

    elif nearN == 75:
        print('grade : C')

    elif nearN == 65:
        print('grade : D')

    elif nearN == 55:
        print('grade : F')







scoreG()

