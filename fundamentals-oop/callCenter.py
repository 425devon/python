import datetime
class Call(object):
    def __init__(self,id,name,phone,reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = datetime.datetime.now()
        self.reason = reason
    def display(self):
        print "ID: {}, Name: {}, Phone Number: {}, time: {}, reason: {}".format(self.id,self.name,self.phone,self.time,self.reason)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.que = 0
    def addCall(self,call):
        newCall = {'id':call.id,'name':call.name,'phone':call.phone,'time':call.time,'reason':call.reason}
        self.calls.append(newCall)
        self.que +=1
        return self
    def remove(self):
        del self.calls[0]
        if self.que > 0:
            self.que -= 1
        return self
    def info(self):
        for person in self.calls:
            print "Name: {}, Phone Number: {}".format(person['name'],person['phone'])
        print self.que
        return self

testcall = Call(1234,"Mike Baker",'555-555-5555',"fallen and cant get up")
testcall2 = Call(1234,"Jim",'555-555-5555',"fallen and cant get up")
testcall3 = Call(1234,"Fred",'555-555-5555',"fallen and cant get up")

cCenter = CallCenter()
cCenter.addCall(testcall).addCall(testcall2).addCall(testcall3).remove()
cCenter.info()

print cCenter.info()




        