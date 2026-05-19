import math
def adding_numbers(a,b):
    return a+b

def subtracting_numbers(a,b):
    return a-b

def multiplying_numbers(a,b):
    return a*b

def dividing_numbers(a,b):
    if b != 0:
        print("The quotient is:", a/b)
    else:
        print("Cannot divide by zero")
        
def Circle_area(a):
    return math.pi*a*a       
        
      
def perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n      
            

x=float(input("Enter a number: "))
y=float(input("Enter another number: "))

print("The sum is:", adding_numbers(x,y))

print("The difference is:", subtracting_numbers(x,y))

print("The product is:", multiplying_numbers(x,y)) 

dividing_numbers(x,y)


print("The area of the circle is:", Circle_area(x))


a=float(input("Enter a number to check if it is a perfect number: "))
if perfect_number(a):
    print(a, "is a perfect number.")
else:    print(a, "is not a perfect number.")