# in, not in 키워드를 사용하면 아이템의 존재 유무 확인 가능

students = ('시노부','카나에','카나오','아오이','칸로지',20,18,17,19)

user = input('학생이름 입력 : ')

if user in students:
    print(f'{user}은 우리반 학생입니다.')
else:
    print(f'{user}은 우리반 학생이 아닙니다.')

# 위 키워드는 문자열에도 사용 가능하다

lyrics='차가운 세상. (두) 눈을 감고 침대에 누워 두 귀를 막고 어제가 오늘 (또) 오늘이 어제'\
'때늦은 자책만 가득한 채 We ll take it slow Baby baby We ll take it slow oh'\
'같은 꿈 마치 날 부르는 익숙한 노래 마침내 연결돼'\
'감싸주지 나를 Hate is on me 반복되는 매일도 괜찮다고 깊은 어둠. 위를 걸어'

print(f'{'감각'} : {'감각' in lyrics}')
print(f'{'세상'} : {'세상' in lyrics}')
print(f'{'꿈'} : {'꿈' not in lyrics}')
print(f'{'노래'} : {'노래' not in lyrics}')
