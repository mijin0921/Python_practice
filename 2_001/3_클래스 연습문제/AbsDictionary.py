from abc import ABCMeta
from abc import abstractmethod

class AbsDictionary(metaclass=ABCMeta):

    def __init__(self):
        self.wordDic={} #단어가 저장될 딕셔너리

    @abstractmethod
    def registWord(self, w1, w2):  #단어를 등록하는 함수 만들기
        pass
    # @abstractmethod
    # def removeWord(self,w1):
    #     pass
    # @abstractmethod
    # def updateWord(self,w1,w2):
    #     pass
    # @abstractmethod
    # def searchWord(self,w1):
    #     pass


class KorToEng(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registWord(self,w1,w2):
        print(f'[KorToEng] 등록 : {w1} to {w2}')
        self.wordDic[w1]= w2

    def print(self):
        for k in self.wordDic.keys():
            print(f'{k} : {self.wordDic[k]}')

# class KorToJpa(AbsDictionary):
#
#     def



