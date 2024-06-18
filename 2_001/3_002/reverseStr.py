#문자열을 거꾸로 하는 모듈

def reverseStr(str):
    resultString = ''

    for i in str:
        resultString = i + resultString

    return resultString

