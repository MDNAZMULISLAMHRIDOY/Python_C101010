class Complex:
    def __init__ (self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j") 
        
    def add(self,c2):
        newReal=self.real+c2.real
        newImg=self.img+c2.img
        
        return Complex(newReal,newImg)
    
    def __sub__(self,c2):      #dender method for subtraction  
        newReal=self.real-c2.real
        newImg=self.img-c2.img
        return Complex(newReal,newImg)
    
    
    def __mod__(self,c2):
        newReal=self.real%c2.real
        newImg=self.img%c2.img
        return Complex(newReal,newImg)

c1=Complex(2,3)
c1.showNumber()   
c2=Complex(4,5)
c2.showNumber()        
    
c3=c1.add(c2)
print("After addition:")
c3.showNumber()


c4=c1-c2 #change
print("After subtraction:")
c4.showNumber()

d5=c1%c2
print("After modulus:")
d5.showNumber()