#패키지를 이용하면 관련있는 모듈을 그룹으로 관리할 수 있다.
# 디렉토리 파일 이름을 다르게 한다 ->패키지 이름
# 특정 패키지의 파일을 쓸 때는 from~import 구문을 사용한다
#예를들어 패키지이름이 calculatorInt 이고, 그 안의 파일에 addCal이 있다
# from calculatorInt import addCal
# addCal.add()


# site-packages에 있는 모듈은 어디서나 사용할 수 있다.
# 예를들어, 어떤 패키지 안의 모듈이 너무 훌륭해서 다른 패키지에서 가져다 쓰고 싶은데 일반적으로 불가능함
# 그래서 이 모듈을 site-packages에 저장해서 여러 패키지에서 가져다 쓸 수 있도록 하는것

# import sys
#
# for path in sys.path:
#     print(path)

