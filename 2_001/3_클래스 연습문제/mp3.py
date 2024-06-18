
# class Song:
#
#     def __init__(self, t, s, pt):
#         self.title = t
#         self.singer = s
#         self.play_time = pt
#
#     def printSongInfo(self):
#         print(f'title : {self.title}')
#         print(f'singer : {self.singer}')
#         print(f'play_time : {self.play_time}')
#
#
# class Player:
#
#     def __init__(self):
#         self.songlist=[]
#         self.isLoop=False
#
#     def addSong(self,s):
#         self.songlist.append(s)
#
#     def play(self):
#         if self.isLoop:
#             while self.isLoop:
#                 for s in self.songlist:
#                    print(f'title : {s.title}, singer : {s.singer}, play time : {s.play_time}')
#                    sleep(s.play_time) #재생시간만큼 프로그램을 잠시 멈추는 기능 Sleep
#
#         else:    # 루프를 돌지 않는 재생일 경우
#                 for s in self.songlist:
#                     print(f'title : {s.title}, singer : {s.singer}, play time : {s.play_time}')
#                     sleep(s.play_time)
#
#     def suffle(self):
#         shuffle(self.songlist)
#
#     def setIsLoop(self,flag):
#         self.isLoop = flag
#
#
# song1 = Song('LiSA','Homura',4)
# song2 = Song('LiSA','홍련화',3)
#
#
# playL=Player()
#
# playL.addSong(song1)
# playL.addSong(song2)
# # playL.play()
# playL.suffle()
# playL.setIsLoop(False)
# playL.play()



# 복습


# class Song:
#
#     def __init__(self,t,s,p):
#         self.title= t
#         self.singer= s
#         self.playTime= p
#
#     def printSong(self):
#         print(f'제목 : {self.title}  가수 : {self.singer}  재생시간 : {self.playTime}')
#
#
#
# class Player(Song):
#
#     def __init__(self,loop=False):
#         self.songList = []
#         self.isLoop = False
#
#
#     def addSong(self,t,s,p):
#         self.songList.append(super().__init__())
#
#     def play(self):
#         if self.isLoop:
#             while True:
#                 for s in self.songList:
#                     print(f'제목 : {s.t}  가수 : {s.s}  재생시간 : {s.p}')
#                     sleep(s.playTime)
#
#         else:
#             for s in self.songList:
#                 print(f'제목 : {s.title}  가수 : {s.singer}  재생시간 : {s.playTime}')
#                 sleep(s.playTime)
#
#
#     def suffle(self):
#         shuffle(self.songList)
#


# gpt로 교정한 결과


from time import sleep
from random import shuffle #얘네 임포트 먼저 해야함...

class Song: #Song 클래스의 객체는 굳이 Player 클래스에 상속할 필요가 없음

    def __init__(self, title, singer, playTime):
        self.title = title
        self.singer = singer
        self.playTime = playTime


    def printSong(self):
        print(f'제목 : {self.title}  가수 : {self.singer}  재생시간 : {self.playTime}')


class Player:

    def __init__(self, loop=False):
        self.songList = []
        self.isLoop = loop

    def addSong(self, s):
        self.songList.append(s)

    def play(self):
        if self.isLoop:
            while True:
                for s in self.songList:
                    print(f'제목 : {s.title}  가수 : {s.singer}  재생시간 : {s.playTime}')
                    sleep(s.playTime)
        else:
            for s in self.songList:
                print(f'제목 : {s.title}  가수 : {s.singer}  재생시간 : {s.playTime}')
                sleep(s.playTime)

    def shuffle(self):
        shuffle(self.songList)


var= Player()

song1=Song('Lisa','불꽃',3)
song2=Song('요네즈 켄시','lady',2)

var.addSong(song1)
var.addSong(song2)
var.play()

#
# class Song:
#     def __init__(self, title, singer, playTime):
#         self.title = title
#         self.singer = singer
#         self.playTime = playTime
#
# class Player:
#     def __init__(self):
#         self.songList = []
#
#     def addSong(self, title, singer, playTime):
#         # Song 객체 생성 및 self.songList에 추가
#         new_song = Song(title, singer, playTime)
#         self.songList.append(new_song)
#
#     def printSongs(self):
#         for song in self.songList:
#             # 각 Song 객체의 속성 출력
#             print(song)
#
# # Player 객체 생성
# player = Player()
#
# # 노래 추가
# player.addSong("Shape of You", "Ed Sheeran", 240)
# player.addSong("Dynamite", "BTS", 223)
# player.addSong("Blinding Lights", "The Weeknd", 200)
#
# # 노래 목록 출력
# player.printSongs()
