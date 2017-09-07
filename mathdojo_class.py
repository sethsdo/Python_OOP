#Assignment: MathDojo
#Part!
#Create a Python class called MathDojo that has the methods add and subtract. 
# Have these 2 functions take at least 1 parameter.

#Math Class

class MathDojo(object):
    def __init__(self, add_sum, sub_sum, result):
        self.add_sum = 0
        self.sub_sum = 0
        self.result = 0

    #add method looks for arguments and adds them to the total
    def add(self, *arg):
        newarg = list(arg)
        result = []
        for i in newarg:
            #checks type of i
            if isinstance(i, (tuple, list, set)) == True:
                for item in list(i):
                    result.append(item)
            else:
                result.append(i) 
        print sum(result)
        print result
        self.add_sum = sum(result)      
        self.result += self.add_sum
        return self

    #subtract method looks for arguments and adds them together then sumtracts them to the total
    def subtract(self, *arg):
        newarg = list(arg)
        result = []
        for i in newarg:
            #checks type of i
            if isinstance(i, (tuple, list, set)) == True:
                for item in list(i):
                    #print type(i)
                    result.append(item)
            else:
                result.append(i) 
        print sum(result)
        print result
        self.add_sum = sum(result)
        #print self.sub_sum
        self.result -= self.add_sum
        return self

    def Result(self):
        int(self.result)
        print self.result
        return self

#method calls 
md = MathDojo(0,0,0)
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).Result()

