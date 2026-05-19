class sum:
    @staticmethod
    def addition(a,b):
        return (a+b)
class sub(sum):
    @staticmethod
    def subtrauction(a,b):
        return (a-b)

class mul(sub):
    @staticmethod
    def multification(a,b):
        return(a*b)
    
class div(mul):#multi-level inheritance
    
    def divission(self,a,b):
        return(a/b)            
    
  
d1=div()

print(d1.addition(10,20))
print(d1.subtrauction(10,20))
print(d1.multification(10,20))
print(d1.divission(10,20))

  