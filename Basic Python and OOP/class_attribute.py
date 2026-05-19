class Student:
    name="anonymous"
    
    def changeName(self,name):
        self.name=name
        
        
class Teacher:
    name="anonymous" 
    
    def changeName(self,name):
        Teacher.name=name   # or self.__class__.name=name
           
s1=Student()
s1.changeName("Nazmul")
print(s1.name)  

print(Student.name)  #class attribute

t1=Teacher()
t1.changeName("Hridoy")
print(t1.name)
print(Teacher.name)
