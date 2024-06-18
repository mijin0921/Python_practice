#유클리드 호제법 : 최대공약수 구하기

def gcd(n1,n2):

    if n1 % n2 == 0:
        return n2 #최대공약수가 나옴!

    else:
        return gcd(n2,n1 % n2)


print(f'최대공약수 : {gcd(82,32)}')
print(f'최대공약수 : {gcd(96,40)}')

# 최대공약수 구하는 단순 반복문

def gcd2(n1,n2):

    maxNum =0

    for i in range(1,(n1+1)):
        if n1 % i == 0 and n2 % i ==0:
            maxNum = i

    return maxNum

print(f'최대공약수 : {gcd2(82,32)}')
print(f'최대공약수 : {gcd2(96,40)}')