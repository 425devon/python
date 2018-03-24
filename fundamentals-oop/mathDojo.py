class MathDojo(object):
    def __init__(self):
        self.result = []
    def add(self,*args):
        val = []
        for arg in args:
            if type(arg) == int:
                val.append(arg)
            else:
                for i in arg:
                    val.append(i)
        self.result.append(sum(val))
        return self
    def subtract(self,*args):
        val = []
        for arg in args:
            if type(arg) == int:
                val.append(arg)
            else:
                for i in arg:
                    val.append(i)
        self.result.append(sum(val)* -1)
        return self
 

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3])

print sum(md.result)
