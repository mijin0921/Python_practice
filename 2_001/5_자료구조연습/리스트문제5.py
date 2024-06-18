var = [12,27,4,7]

result=[]
#리스트 안에 리스트로 저장하기!

for n1 in var:
   for n2 in var:
       if n2 == n1:
           continue
       for n3 in var:
           if n1 == n3 or n2 == n3:
               continue
           result.append([n1, n2, n3])


print(result)
print(len(result))





