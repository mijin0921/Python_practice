#lambda 키워드를 이용하면 함수 선언을 보다 간단하게 할 수 있다.

#간단한 함수일 경우 lamda함수를 쓰면 효율적임

# def calculator(n1,n2):
#     return n1+ n2
#
# value=calculator(1,2)

calcul = lambda n1,n2: n1 + n2 #위의 함수식과 똑같음
result = calcul(1,2) #함수호출은 변수로 할당

print(result)

