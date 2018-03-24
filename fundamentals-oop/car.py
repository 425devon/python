class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if price > 10000:
            self.tax = 0.15
        self.display_all()
    def display_all(self):
        print("Price: {}, Speed: {}mph, Fuel {}, Mileage: {}mph, Tax: {}").format(self.price, self.speed, self.fuel, self.mileage,self.tax)
        return self

car1 = Car(2000,35,'Full',15)
car2 = Car(2000,5,'Not Full',15)
car3 = Car(2000,15,'Kind of Full',96)
car4 = Car(2000,25,'Full',15)
car5 = Car(2000,45,'Empty',25)
car6 = Car(2000000,35,'Empty',15)

