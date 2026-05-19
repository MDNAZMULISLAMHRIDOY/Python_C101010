def Recursion(n):
    if(n==0):
        return 1;
    
    else:
        return n*Recursion(n-1);
    
    
n=int(input("Enter a number: "))
 
print(Recursion(n),end=" ")