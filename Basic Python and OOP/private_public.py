class Person:
    name="anonymous"
  
    def __hello(self):
         print("Hello, I am a person!")
   
   
    def Welcome(self):
        self.__hello()
      
   

class Account:
    def __init__ (self,acc_no,acc_pass):
        self.acc_no=acc_no
        self._acc_pass=acc_pass 
        
    def reset_pass(self):
         print(self._acc_pass)   


p1=Person()
print(p1.Welcome())

#acc1=Account("1234567890","password123")
#print(acc1.acc_no)
#print(acc1.reset_pass()) #protected attribute #protected attribute


        