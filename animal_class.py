#Create an Animal class and give it the below attributes and methods. 
# Extend the Animal class to two child classes, Dog and Dragon.
#The objective of this assignment is to help you understand inheritance.

#parent class animal
class Animal(object):
    def __init__(self, name, health):
        #attributes
        self.name = name
        self.health = health
        self.message = ""
    #methods
    def walk(self):
        self.health = self.health - 1
        print "walking"
        return self
    def run(self):
        self.health = self.health - 1
        print "running"
        return self
    def displayHealth(self):
        print "Name " + str(self.name)
        print "Strangth " + str(self.health)
        return self

#class dog inharits from parent animal class
class Dog(Animal):
    #methods   
    def pet(self):
        self.health = 150
        self.health = self.health + 5
        return self

#dog class calls
dog1 = Dog("Lose", 0)
dog1.walk().walk().walk().run().run().pet().displayHealth()

#class Dragon inharits from parent animal class
class Dragon(Animal):  
    #methods
    def fly(self):
        self.health = 170
        self.health = self.health - 10
        return self
    #methods
    def display_health(self):
        print "I am a Dragon"
        self.displayHealth()
        return self

#dragon class calls
dragon1 = Dragon("Ragor", 0)
dragon1.fly().display_health()

#class Shark inharits from parent animal class
class Shark(Animal): 
    #methods   
    def swim(self):
        self.health = 170
        self.health = self.health - 4
        return self
    #methods
    def display_health(self):
        #print self.health
        print "Great White Shark"
        self.displayHealth()
        return self

#shark class calls
shark1 = Shark("Casper", 0)
shark1.swim().display_health()
    