class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self,tax):
        self.price = self.price - (self.price * tax)
        print ("{} after tax is ${}").format(self.item_name, self.price)
        return self
    def returns(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box, like new":
                self.status = "used"
                self.price = self.price *.08
    def display_info(self):
        print "Item price ${}, item name: {}, item weight: {} oz, item brand: {}, item status: {}".format(self.price,self.item_name,self.weight,self.brand,self.status)
        return self
        


cereal = Product(4.99,"captain crunch", 12, "kellog")

cereal.display_info()

cereal.returns("defective")

cereal.display_info()