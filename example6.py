class Car:
    def __init__(self,brand,speed):
       self.brand = brand
       self.speed = speed

    def accelerate(self,value):
        self.speed += value

    def show_speed(self):
        print(f"{self.brand} is running at {self.speed}km/h")

#object creation
c = Car('BMW',60)
c.accelerate(20)
c.show_speed()


