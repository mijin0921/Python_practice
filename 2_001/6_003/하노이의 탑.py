#하노이의 탑 (재귀와 관련된 게임)
# 좀 복잡함, 알고리즘 단골 문제

# 코드

def moveDisc(disCnt,fromBar,toBar,viaBar):
    if disCnt == 1:
        print(f'{disCnt}disc를 {fromBar}에서 {toBar}로 이동')

    else:
        moveDisc(disCnt-1,fromBar,viaBar,toBar) # 가장 위의 디스크를 제외한 나머지 디스크들을 viaBar로 이동

        print(f'{disCnt}disc를 {fromBar}에서 {toBar}로 이동') # 가장 큰 디스크를 목적지로 이동

        moveDisc(disCnt - 1, viaBar, toBar, fromBar) # viaBar에 있는 디스크들을 목적지로 이동



moveDisc(3,1,3,2)

# 하노이의 탑 공식(n은 원반 개수) : f(n) = 1 + 2f(n-1)=2^n -1


# 실행되는 순서 !! (위에서부터 아래로 출력됨, 즉, 경유기둥에 먼저 옮기고 도착기둥에 옮기는 순서)
# moveDisc(3, 1, 3, 2) 호출
#  else 블록 진입 (1)
# moveDisc(2, 1, 2, 3) 호출 (재귀)
#   else 블록 진입 (2)
#   moveDisc(1, 1, 3, 2) 호출 (재귀)
#     디스크 1을 1에서 3으로 이동 (3)
#   디스크 2를 1에서 2로 이동 (4)
#   moveDisc(1, 3, 2, 1) 호출 (재귀)
#     디스크 1을 3에서 2로 이동 (5)
# 디스크 3을 1에서 3으로 이동 (6)
#  moveDisc(2, 2, 3, 1) 호출 (재귀)
#   else 블록 진입 (7)
#   moveDisc(1, 2, 1, 3) 호출 (재귀)
#     디스크 1을 2에서 1로 이동 (8)
#    디스크 2를 2에서 3으로 이동 (9)
#    moveDisc(1, 1, 3, 2) 호출 (재귀)
#     디스크 1을 1에서 3으로 이동 (10)
