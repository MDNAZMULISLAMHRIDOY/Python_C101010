class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
        
        
    def showDetails(self):
        print("Role: ",self.role)
        print("Department: ",self.department)
        print("Salary: ",self.salary)
        
        
class Engineers(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","Development",150000)   
                

e1=Engineers("Nazmul",25)   
e1.showDetails()     