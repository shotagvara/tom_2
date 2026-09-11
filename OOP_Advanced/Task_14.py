"""Задание 14 — delegation через __getattr__
Теперь немного сложнее.
Создай:
class Speaker:
с методами:
play()
stop()
volume_up()
Создай:
class SmartSpeaker:
который хранит:
self.speaker = Speaker()
И реализуй:
__getattr__
так, чтобы неизвестные attributes делегировались объекту self.speaker.
То есть должно работать:
smart.play()
smart.stop()
хотя play и stop напрямую в SmartSpeaker не написаны."""
class Speaker:
    def play(self):
        return "speaker plays"

    def stop(self):
        return("speaker stops")

    def volume_up(self):
        return("Speaker volume up")

class SmartSpeaker():
    def __init__(self):
        self.speaker=Speaker()

    def __getattr__(self, name):
        return self.speaker.__getattribute__(name)

smart = SmartSpeaker()

print(smart.play())
print(smart.stop())