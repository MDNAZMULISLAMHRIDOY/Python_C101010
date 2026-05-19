import math

class Student1:
  def __init__(self,math,english,science):
    self.math=math
    self.english=english
    self.science=science
    
  def average(self):
    
    return(self.math+self.english+self.science)/3
    


class Student:
    #default constructor
    def _init_(self):
      print("default constructor called...")
      pass
   
   #parameterized constructor
    def __init__(self,name,marks,roll):
        self.name=name
        self.marks=marks
        self.roll=roll
        print("adding new student database...")
        
        
        
        
class Teacher:
  
  def __init__(self,name,subject):
    self.name=name
    self.subject=subject
    print("adding new teacher database...") 
    
    
  def display(self):
      print("Hello, I am a Teacher",self.name)


class calculation:
  
   def __init__(self,a,b):
     self.a=a
     self.b=b   

   def add(self):
    return self.a+self.b
  
   def subtract(self):
    return self.a-self.b
  
   def multiply(self):
    return self.a*self.b
     
   def divide(self):
    if self.b!=0:
      return self.a/self.b
    else:
      return "Division by zero is not allowed"
    
   def area_of_circle(self):
    return math.pi*self.a*self.a   
             
        
s1=Student("John",85,101)
print(s1.name)
print(s1.marks)
print(s1.roll)

t1=Teacher("Smith","Math")
t1.display()
        
c=calculation(10,5)
print("Addition:",c.add())
print("Subtraction:",c.subtract())
print("Multiplication:",c.multiply())   
print("Division:",c.area_of_circle())

print("\n")
s2=Student1(90,85,95)
print("Average marks:",s2.average())