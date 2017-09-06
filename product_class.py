#product class
class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        #self.cost = cost 
        self.status = "for sale"
        self.reason_for_return = ""
        self.tax = .015

    def Sell(self):
        self.status = "sold"
        print self.status
        return self

    def AddTax(self):
        self.price = (self.price)*self.tax + self.price
        print self.price
        return self

    def Return(self, reason_for_return):
        self.reason_for_return = reason_for_return
        if reason_for_return == "returned defective":
            self.status = "defective"
            # print self.status
            self.price = 0
            return self
        elif reason_for_return == "returned, box unopened":
            self.status = "for sale"
            # print self.status
            return self
        elif reason_for_return == "returned, box opened":
            self.status = "used"
            # print self.status
            self.price = (self.price/100)*80
            return self

    def DisplayInfo(self):
        print "$" + str(self.price)
        print self.item_name
        print str(self.weight) + "pounds"
        print self.brand
        #"$" + str(self.cost) 
        print self.status
        return self

product1 = Product(1000,"Macbook",3,"Apple")
product2 = Product(1000,"Macbook",3,"Apple")
product3 = Product(1000,"Macbook",3,"Apple")
product1.Sell().AddTax().DisplayInfo()
product2.Return("returned defective").AddTax().DisplayInfo()
product3.Return("returned, box opened").AddTax().DisplayInfo()
        
            

            
        
    
    
