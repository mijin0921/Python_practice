# 데이터 사이언스 스쿨(AI 스쿨)

# 모든 공지사항을 꼼꼼하게 확인해주시기 바랍니다!

# 파이썬 프로그래밍 테스트
# 내용: 파이썬 활용 능력 평가
# 범위: 파이썬 강의 기반
# 문항: 1 ~ 6번, 총 6문제
# 배점: 총점 100점
# 1,2번 각 10점
# 3,4번 각 15점
# 5,6번 각 25점

# 채점 기준
# 각 문제마다, print() 값의 결과만 나오시게끔 작성하시면 됩니다.
# 코드는 어떻게 작성하셔도 상관없습니다.
# 코드 정상작동 만점 (각 배점에 맞게 만점)
# 코드 미실행(에러 발생)은 0점
# 부분 점수는 없습니다

# 숙지 사항
# 아래 각 문제에, pass 부분을 지우시고 코드를 작성해주시면 됩니다.
# 모든 코드를 작성하셨을 때, 코드가 정상적으로 실행되어야 합니다.
# 모든 문제는 print() 문으로 결과가 출력되어야 합니다.
# 제출 코드는 실행했을 때 자동으로 실행되게끔 작성해주세요(input 함수 사용 금지).


# start !

# 문제 1 (10점)
# 문제 1번은 함수가 아닌, 변수만 선언해주시면 됩니다.

print("1번 답안")
tmp = []
print(tmp)


# 문제 2 (10점)
def data_type(n):
    typeList = ['int', 'float', 'str', 'bool', 'list', 'dict', 'tuple']
    typeV = n
    result = []

    def typeL(s):
        if type(s) == int:
            result.append(typeList[0])
        elif type(s) == float:
            result.append(typeList[1])
        elif type(s) == str:
            result.append(typeList[2])
        elif type(s) == bool:
            result.append(typeList[3])

    if type(typeV) == list:
        result.append(typeList[4])
        result.append('<')
        for i in typeV:
            typeL(i)
            if type(i) == list:
                result.append(typeList[4])
                result.append('<')
                for j in i:
                    typeL(j)
                result.append('>')
            elif type(i) == tuple:
                result.append(typeList[6])
                result.append('<')
                for j in i:
                    typeL(j)
                result.append('>')

        result.append('>')


    elif type(typeV) == tuple:
        result.append(typeList[6])
        result.append('<')
        for i in typeV:
            typeL(i)
            if type(i) == list:
                result.append(typeList[4])
                result.append('<')
                for j in i:
                    typeL(j)
                result.append('>')
            elif type(i) == tuple:
                result.append(typeList[6])
                result.append('<')
                for j in i:
                    typeL(j)
                result.append('>')
        result.append('>')


    else:
        typeL(typeV)

    if len(result) == 1:
        return result[0]
    else:
        return ' '.join(result)


print("2번 답안")
print(data_type([1, 2, (1, 2), 'hello']))

# 문제 3 (15점)
import math


def calc_tips(p, t=1 / 10):
    totalTips = 0
    totalTips = math.ceil(p * (t * 1 / 100))

    if t == 1 / 10:
        totalTips = math.ceil(p * t)

    print(f'total tips : {totalTips} dollar')


print("3번 답안")
print(calc_tips(120))


# 문제 4 (15점)
def search_target(sentence, target):
    targetCnt = 0
    targetIdx = []

    # 매칭되는 문자열의 횟수 값 찾기
    targetCnt = sentence.count(target)

    # 매칭되는 문자열의 위치 값 찾기
    temp_sentence = sentence

    for i in range(targetCnt):
        sentenceIdx = temp_sentence.index(target)
        targetIdx.append(sentenceIdx)
        temp_sentence = temp_sentence[sentenceIdx + 1:]

    return str(targetCnt) + ',' + str(targetIdx)


print("4번 답안")

sentence = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
target = "than"

print(search_target(sentence, target))


# 문제 5 (25점)
def div_ab(a, b):
    floorDiv = 0
    mod = 0

    try:
        if a % int(a) != 0 or b % int(b) != 0:
            print('정수를 입력하세요')

        else:
            # 몫 : b의 등비수열에서 a와 가장 근접한 항
            standardNum = []
            n = 0
            while (b * n) <= a:
                standardNum.append(b * n)
                n += 1

            minNum = a
            # 근삿값 알고리즘
            for idx, s in enumerate(standardNum):
                absNum = a - s

                if absNum < minNum:
                    minNum = absNum
                    floorDiv = idx

            # 나머지 : 몫에서 b를 곱한다음 a를 빼면된다
            mod = a - (b * floorDiv)

            print(f"{a}나누기 {b}의 결과 : 몫 {floorDiv} , 나머지 {mod}")


    except:
        print('0은 나눌수 없습니다')


print("5번 답안")
a = 3
b = 2
print(div_ab(a, b))


# 문제 6 (25점)
def hanoi_sol(dics, startP, endP, midP="C"):
    if dics == 1:
        print(f'{startP}->{endP}')

    else:

        # 처음 - 경유 기둥으로 이동
        hanoi_sol(dics - 1, startP, midP, endP)

        print(f'{startP}->{endP}')

        # 경유기둥 - 도착 기둥으로 이동
        hanoi_sol(dics - 1, midP, endP, startP)


print("6번 답안")
hanoi_sol(3, "A", "B")

print("모든 문제가 끝났습니다")
print("수고하셨습니다 :)")

# end !

# 시험이 끝난 후에는?
# 제출 방법: 제공드린 설문지에 파일을 업로드 해주세요
# 제출 양식: [DS]python_programming_honggildong.py

# 대괄호 안에 대문자로 [DS]
# _ 언더바 사용
# 수강생분 성함(성부터 이름 순으로 모두 소문자 작성)
# 잘못된 예 -> [ds]_HongGilDong.py 또는 [ds]_HongGilDong.py.py 또는 [DS]_Hongggildong.py 등 위에 제시드린 제출 양식과 다른 모든 표현은 감점입니다.
# 파일 제출 양식 또한 감점 요인에 포함되오니, 반드시 꼼꼼하게 확인해주시기를 바랍니다.
# 제출 양식 잘못됐을 시, 전체 점수에서 3점 감점

# 해설 또는 답안 공유 안내
# 문제에 대한 해설 또는 답안은 기본적으로는 공유드리지 않을 예정입니다
# 정해진 답을 제시드리는 것 보다, 각 문제에 대해 여러분들이 작성한 답안을 서로 공유해주셨으면 좋겠습니다 :)
# 같은 기간, 같은 강의를 듣고 같이 공부하시는 다른 분들은 어떤 식으로 문제를 푸셨는지 서로 논의하실 수 있는 장이 마련됐으면 좋겠습니다.

# 왜 그렇게 하나요?
# 데이터 사이언스를 공부하시는 여러분은, 정답이 정해진 분야를 공부하고 계신 것이 아닙니다.
# 여러분이 생각하는 모든 것이 정답일 수 있습니다.
# 나의 생각을 다른 사람에게 표현하고, 설득하고, 공유하시는 방식에 익숙해지셨으면 하는 마음입니다.

# 이번 테스트 뿐만 아니라, 추후 제공드리는 강의, 과제, 프로젝트에서도 정답을 바로 찾고 이해하려 하시는 것보다
# 나라면 어떻게 할까? 이렇게 하는 게 더 좋지 않을까? 다른 사람들은 어떻게 생각할까? 나는 이렇게 생각하고 문제를 해결했는데 어떤 것 같나요?
# 문제에 대해 스스로 사유하고, 해결한 나만의 방식을 공유하시는 힘을 길렀으면 좋겠습니다.
# 남은 기간 더욱 힘내셨으면 하는 바램입니다.
