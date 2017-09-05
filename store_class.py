#class store

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_products(self, item):
        self.item = item
        #print item
        self.products.append(item)
        return self

    def remove_products(self, item):
        self.item = item
        #print item
        self.products.remove(item)
        return self

    def inventory(self):
        print "Store inventory " + str(self.products)
        print "Store location " + self.location
        print "Store owner " + self.owner
        return self

        

store = Store(["apple", "potato", "pepper"], "2276, westburg northfork Mn", "John Wetherbe")  

store.add_products("meat").remove_products("potato").inventory() 
