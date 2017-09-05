#Create a new class called Bike with the following properties/attributes:

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print self.price
        print self.max_speed
        print str(self.miles) +"miles"
    def ride(self):
        print "Riding"
        self.miles += 10
        return self 
    def reverse(self): 
        print "Reversing"
        self.miles -= 5
        return self

bike = Bike(200, "25mph")
bike.ride().ride().ride().reverse().displayInfo()
bike.ride().ride().reverse().reverse().displayInfo()
bike.reverse().reverse().reverse().displayInfo()