# Define a class Bird
class Bird:
    def sound(self):
        print("chirp")


class Parrot(Bird):
    def sound(self):
        print("Squawk")


def make_sound(bird):
    bird.sound()


b1 = Bird()
p1 = Parrot()

make_sound(b1)
make_sound(p1)