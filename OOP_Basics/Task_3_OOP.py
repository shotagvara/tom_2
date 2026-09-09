"""3. Сделай специально неправильный класс:
class Playlist:
    songs = []
Создай две playlist, добавь песню только в 
одну и посмотри, что произошло. Затем исправь через self.songs = []."""

class Playlist:
    songs=[]
    def __init__(self):
        self.songs=[]
    

pl1=Playlist()
pl2=Playlist()

pl1.songs.append("song for pl1")

print(pl1.songs)
print(pl2.songs)
# When weong then:
#[['song for pl1']]
#[['song for pl1']]

"""When right 
['song for pl1']
[]
"""
