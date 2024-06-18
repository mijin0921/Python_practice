#insert() 함수 : 특정 위치(인덱스)에 아이템을 추가할 수 있다
#insert로 아이템을 특정 위치에 추가하면 원래있던 아이템은 뒤로 한칸씩 밀려남

students = ['시노부','카나에','네즈코','기유','탄지로']

students.insert(4,'이노스케')
print(students)

# 오름차순 정렬 리스트에 숫자 추가

numbers = [1,3,6,11,45,54,62,74,85]

inputNum=int(input('정수 입력 : '))
insertIdx = 0

for idx,num in enumerate(numbers):

    if insertIdx == 0 and inputNum < num:
        insertIdx = idx
        numbers.insert(insertIdx,inputNum)

    print(f'{idx} : {num}')

print(numbers)
