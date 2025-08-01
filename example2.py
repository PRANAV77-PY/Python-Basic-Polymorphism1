class Shape:
    def area(self):
        print("Area not defined")


class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
shapes = [Square(4),Circle(3)]
for s in shapes:
    print("Area",s.area())
        
    