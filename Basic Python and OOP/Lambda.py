x1=lambda x: "Even" if x % 2 == 0 else "Odd"

y=lambda n: sum(i for i in range(1, n))

print(x1(10))  
print(y(5))    