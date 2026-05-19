class Car:
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("Car is starting....")
     
    @staticmethod
    
    def stop():
         print("Car is stopping....")   
            
            
class Motorcycle(Car):
     def __init__ (self,name,type):
            super(). __init__(type)
            super().start()
            self.name=name
            
            
m1=Motorcycle("FZ","Sport")
print(m1.type)
print(m1.name)
