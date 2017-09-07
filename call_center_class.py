#Call Center
#parent class
class Call(object):
    def __init__(self, caller_id, caller_name, phone_num, time_of_call, reason):
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.phone_num = phone_num
        self.time_of_call = time_of_call
        self.reason = reason
        self.logged = True
    # def print_attr(self):
    #     print self.caller_id  
    #     print self.caller_name         
    #     print self.phone_num
    #     print self.time_of_call
    #     print self.reason
    #     return self

#call center, stores calls in a list. has methods for adding and removing
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self, call):
        self.calls.append(call)
        self.queue_size = len(self.calls)
        return self
    def remove(self, number):
        for i in self.calls:
            if i.phone_num == number:
                self.calls.remove(i)
                self.queue_size -= 1
        return self
    def info(self):
        for i in self.calls:
            print '{}, {}'.format(i.caller_name, i.phone_num)
        print self.calls
        return self
    def sort(self):
        self.calls = sorted(self.calls, key=lambda sort_time: sort_time.time_of_call)
        return self

#instances of the class 
call1 = Call("id:1","Seth","555-555-555", 3,"inquery")
call2 = Call("id:1","Seth","777-555-555",2,"inquery")
call3 = Call("id:1","Seth","666-555-555", 1,"inquery")
cc = CallCenter()
cc.add(call1).add(call2).add(call3).remove("777-555-555").sort().info()





