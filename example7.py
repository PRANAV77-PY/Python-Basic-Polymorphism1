class Mobile:
    def __init__(self,model,battery):
        self.model = model
        self.battery = battery

    def Charge(self,percent):
        self.battery = min(100,self.battery + percent)

    def Show_battery(self):
        print(f"{self.model}  Battery: {self.battery}%")


m = Mobile('SAMSUNG',50)
m.Charge(30)
m.Show_battery()

        

    