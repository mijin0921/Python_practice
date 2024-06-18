#예외발생과 상관없이 항상 실행한다.

# 즉 예외 발생시, 예외가 발생하지 않고 정상 실행시 전부 실행되는 구문


evenlist=[]
oddlist=[]
floatlist=[]
datalist=[]

n=1
while n<6:

    try:
        num=input('input number : ')
        data=float(num)  #datalist에 문자열까지 담으려고 따로 변수를 만듬

    except:
        print('exception number!')
        continue

    else:
        if data-int(data) !=0:
            floatlist.append(data)

        else:
            if data % 2 ==0:
                evenlist.append(int(data))

            else:
                oddlist.append(int(data))

        n +=1

    finally:
        datalist.append(num)


print(evenlist)
print(oddlist)
print(floatlist)
print(datalist)

