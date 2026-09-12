"""
Задание 9 — __len__, __getitem__, __iter__
Теперь делаем мини-контейнер:
class Playlist:
Внутри:
self._songs = []
Метод:
add_song(song)
Потом реализуй:
__len__
чтобы:
len(playlist)
работал.
Реализуй:
__getitem__
чтобы работало:
playlist[0]
playlist[1]
И потом:
__iter__
чтобы:
for song in playlist:
    print(song)
работало.
Для начала можешь сделать __iter__ самым простым способом:
return iter(self._songs)"""
class PlayList:

    def __init__(self):
        self._songs = []


    def add_song(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, key):
        return self._songs[key]

    def __iter__(self):
        return iter(self._songs)

pl = PlayList()
pl.add_song("#1")
pl.add_song("#2")
pl.add_song("#3")

print(f"len: {len(pl)}")
print(pl[0])
print(pl[1])

print("ITERATION:")
for song in pl:
    print(song)

"""len: 3
#1
#2
ITERATION:
#1
#2
#3"""