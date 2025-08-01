#Polymorphism
class Media:
    def play(self):
        print('Playing Media')

class Audio(Media):
    def play(self):
        print('Playing Audio File')

class Video(Media):
    def play(self):
        print("Playing Video File")


for media in [Media(),Audio(),Video()]:
    media.play()