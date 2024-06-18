
user=int(input("cm를 입력하시오"))

def cmToMm():
    return round(user * 10,3)

def cmToInch():
    return round(user * 0.393,3)

def cmTom():
    return round(user * 0.01, 3)

def cmToFt():
    return round(user * 0.032, 3)

if __name__=='__main__':
    print(f'{user}cm : {cmToMm()}mm')
    print(f'{user}cm : {cmToInch()}inch')
    print(f'{user}cm : {cmTom()}m')
    print(f'{user}cm : {cmToFt()}ft')