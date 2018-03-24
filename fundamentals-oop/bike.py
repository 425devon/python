class Bike(object):
    def __init__(self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "Price: {}, Maximum speed: {}mph, total miles: {}".format(self.price, self.max_speed,self.miles)
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self

bike1 = Bike(250,22,35)
bike2 = Bike(425,27,20)
bike3 = Bike(700,32,2)

bike1.displayinfo().ride().displayinfo().reverse().displayinfo()
