class Car:
    color="Red"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod   
    def stop():
        print("Car Stopped...")
    
class ToyotaCar(Car):#inheritance
    
 def __init__ (self,name):
     self.name=name
     
 
t1=ToyotaCar("Fortuner")
t2=ToyotaCar("Innova")

print(t1.start())
print(t2.stop())
print(t1.color)
     
     
         
    
        
    