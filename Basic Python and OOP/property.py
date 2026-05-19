class Student:
    def __init__ (self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
        
    @property    
    def average(self):
        return "Average: " + str((self.phy+self.chem+self.math)/3) + " %"


s1=Student(80,90,95)
print(s1.average)
s1.math=70
print(s1.average)
        