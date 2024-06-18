# import AbsDictionary as dic
#
# word1 = dic.KorToEng()
# word1.registWord('달력','calender')
# word1.print()

import mp3

s1 = mp3.Song('드라마','에스파',4)
s2 = mp3.Song('나에게로의 초대','정경화',4)
s3 = mp3.Song('easy','르세라핌',3)
s4 = mp3.Song('Get a guitar','라이즈',4)

player = mp3.Player()

player.addSong(s1)
player.addSong(s2)
player.addSong(s3)
player.addSong(s4)

player.play()
player.suffle()
player.play()


