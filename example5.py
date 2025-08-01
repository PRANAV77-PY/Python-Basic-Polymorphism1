class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def discount_price(self,discount_percent):
        return self.price - (self.price * discount_percent/100)
    

p = Product('Shoes',2000)
print("Discounted Price: ",p.discount_price(10))