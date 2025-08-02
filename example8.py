class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.15
    
e = Employee('Vaibhav',70000)
print('Bonus: e.bonus()')