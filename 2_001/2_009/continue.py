#반복 실행 중 continue를 만나면 밑의 실행문으로 넘어가지 않고 다시 위의 실행문으로 올라간다.

# 7의 배수만 출력하는 프로그램
for i in range(1,100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수입니다.'.format(i))

# else의 실행문은 반복문이 종료된 후 실행된다.

cnt=0
for i in range(1,100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수입니다.'.format(i))
    cnt +=1

else:
    print('7의 배수의 숫자는 {}개 입니다.'.format(cnt))


