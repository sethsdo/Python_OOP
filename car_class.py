#car class
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = ".12"
        
    def displayAll(self):
        print "Price: " + str(self.price)
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        if self.price > 10000:
            self.tax = 0.15
            return "Tax: " + str(self.tax)
        else:
            return "Tax: " + str(self.tax)

car1 = Car(2000,"35mph","Full","15mph")
car2 = Car(2000,"5mph","Not Full","105mph")
car3 = Car(2000,"15mph","Kind of Full","95mph")
car4 = Car(2000,"25mph","Full","25mph")
car5 = Car(2000,"45mph","Empty","25mph")
car6 = Car(2000000,"35mph","Empty","15mph")

print car1.displayAll()
print car2.displayAll()
print car3.displayAll()
print car4.displayAll()
print car5.displayAll()
print car6.displayAll()