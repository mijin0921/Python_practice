# goods1 = int(input('구매 개수 : '))
# goods2 = int(input('구매 개수 : '))
# goods3 = int(input('구매 개수 : '))
# goods4 = int(input('구매 개수 : '))
# goods5 = int(input('구매 개수 : '))
# totalP = (goods1+goods2+goods3+goods4+goods5) * 900

#
# class GoodsInt(Exception):
#
#     def __init__(self,n):
#         super().__init__(f'상품 : {n}')
#
#
#
#
# nuM=[]
# total = 0
#
#
# def NotInt():
#     for i in range(1,6):
#         goods = int(input('구매 개수 : '))
#         nuM.append(goods)
#         print(f'goods{i} 구매 개수 : {goods}')
#
#
#
# for idx,goods in enumerate(nuM):
#         if int(goods) != True:
#                 raise GoodsInt(goods)
#         else:
#                 total += goods
#
#
# print('-'*20)
# try:
#     NotInt()
#     for idx, goods in enumerate(nuM):
#         if int(goods) != True:
#             raise GoodsInt(goods)
#         else:
#             total += goods
# except GoodsInt as g:
#     print(g)
#
# finally:
#     print('-' * 20)
#     print(f'총 구매 금액 : {format((total*900), ',')}원')
#     print('-' * 5 + '미결제 항목' + '-' * 5)







# try:
#     print(f'goods1 구매 개수 : {goods1}')
#     print(f'goods2 구매 개수 : {goods2}')
#     print(f'goods3 구매 개수 : {goods3}')
#     print(f'goods4 구매 개수 : {goods4}')
#     print(f'goods5 구매 개수 : {goods5}')
#
# except Exception as e:
#     print(e)
#
# finally:
#     print('-'*20)
#     print(f'총 구매 금액 : {format(totalP,   ',')}원')
#     print('-' * 5 + '미결제 항목'+ '-'*5)


# 풀이

g1Price = 1200 ; g2Price = 1000; g3Price = 800; g4Price = 2000; g5Price = 900

def calculator(*gcs): #매개변수가 몇개가 올지 모를 떄

    gcsDic ={}
    againCntInput={}

    for idx, gc in enumerate(gcs):
        try:
            gcsDic[f'g{idx+1}'] = int(gc)
        except Exception as e:
            againCntInput[f'g{idx+1}'] = gc
            print(e)

    totalP = 0
    for g in gcsDic.keys():
        totalP += globals()[f'{g}Price'] * gcsDic[g] #globals 함수는 변수명을 참조하는 함수

    print('-' * 20)
    print(f'총 구매 금액 : {format(totalP, ',')}원')
    print('-' * 5 + '미결제 항목' + '-' * 5)
    for g in againCntInput.keys():
        print(f'상품 : {g} , 구매 개수 : {againCntInput[g]}')
    print('-' * 20)





goods1 = input('구매 개수 : ')
goods2 = input('구매 개수 : ')
goods3 = input('구매 개수 : ')
goods4 = input('구매 개수 : ')
goods5 = input('구매 개수 : ')

calculator(goods1,goods2,goods3,goods4,goods5)