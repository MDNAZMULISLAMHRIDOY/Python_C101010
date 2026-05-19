class Student:
    def __init__(self,name,ID):
     self.name=name
     self.ID=ID

s1=Student("Nazmul","B210101020")

print("Before deleting name attribute:")
print(s1.name)
print(s1.ID)

del s1.name

print("After deleting name attribute:")
print(s1.ID)
print(s1.name)

     
     
     
     