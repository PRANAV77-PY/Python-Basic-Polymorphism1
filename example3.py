class Vehicle:
    def fare(self):
        return 0
    
class Bus(Vehicle):
    def fare(self):
        return 50
    
class Train(Vehicle):
    def fare(self):
        return 100
    

#object craetion
vehicles = [Bus(),Train()]
for v in vehicles:
    print("Fare: ",v.fare())