from typing import Self


class car():
    def __init__(self, make, model, sticker_price, discount_price):
        self.Make = make
        self.Model = model 
        self.Sticker_price = sticker_price
        self.Discount_price = sticker_price * .9

class sport():
    def __init__(self, make, model, sticker_price, discount_price,option):
        self.Make = make
        self.Model = model 
        self.Sticker_price = sticker_price
        self.Discount_price = sticker_price * .9
        self.Option = option
    
    def sportwheels(self):
        self.Option += 1000

    def sportinterior(self):
        self.Option += 2000
    
    def sportengine(self):
        self.Option += 3000
mustang = sport("ford","mustang",20000,0,0)
print(mustang.Make)
print(mustang.Model)
print(mustang.Sticker_price)
print(mustang.Discount_price)
mustang.sportengine()
print(mustang.Option)
mustang.sportinterior()
print(mustang.Option)
mustang.sportinterior()
print(mustang.Option)
