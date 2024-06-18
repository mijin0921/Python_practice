studentInfo = [
    { '회원번호' : 'S21-0001',
      '이름' : '최성훈',
      '성구분' : 'M',
      '전공' : '디자인',
      '연락처' : '010-1234-5678',
      '메일' : 'hun@gmail.com',
      '취미' : ['농구','음악']

    },
{
    '회원번호': 'S21-0002',
    '이름': '탁영우',
    '성구분': 'M',
    '전공': '바리스타',
    '연락처': '010-1111-5678',
    '메일': 'tak@gmail.com',
    '취미': ['축구']
}
]


for student in studentInfo:
    for i in student.keys():
        print(f'{i} : {student[i]}')

    print()
    print('-'*23)
    print()


# 풀이 : 회원번호를 key 값으로 하고 나머지를 전부 value로 하되 딕셔너리로 value값 처리

studentInfo2 = { 'S21_001' : {'이름' : '최성훈',
                              '성구분': 'M',
                              '전공': '디자인',
                              '연락처': '010-1234-5678',
                              '메일': 'hun@gmail.com',
                              '취미': ['농구', '음악']},

                'S21_002' : {'이름': '탁영우',
                             '성구분': 'M',
                             '전공': '바리스타',
                             '연락처': '010-1111-5678',
                             '메일': 'tak@gmail.com',
                             '취미': ['축구']}

                }

for k1 in studentInfo2.keys():
    print(f'학생번호 : {k1}')

    student = studentInfo2[k1]
    for k2 in student.keys():
        print(f'{k2} : {student[k2]}')

    print()
    print('-' * 23)
    print()


