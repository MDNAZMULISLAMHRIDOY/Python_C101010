class sum:
    
    def sumation(self,a,b):
        print("Sum of a and b is : ")
        return(a+b)
     

class sub:
    
    def Subtraction(self,a,b):
        print("Subtraction of a and b is : ")
        return(a-b)
      

class mul:
    
    def multiplication(self,a,b):
        print("Multiplication of a and b is : ")
        return(a*b)
        

class div(sum,sub,mul):#multiple inheritance
    
    def division(self,a,b):
        print("Division of a and b is : ")
        return(a/b)

d1=div()
print(d1.sumation(50,40))