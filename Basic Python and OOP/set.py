
myset={5,1,5,2}

#no dublicate value

print(myset)


myset.add(8)
myset.add(89)

print()

myset.remove(1)

set1={100,896,37}
myset.update(set1)

for i in myset:
    
 print(i,end=" ")

print()    
print("After removing 37")
    
myset.remove(37)
print(myset)

myset.discard(100)
print("After discarding 100:")
print(myset)

myset.pop()
print("After popping an element:")
print(myset)

#Joining two sets

myset1={"Nazmul","Islam","Rafi"}
myset2={"Alice","Bob","Charlie"}

set3=myset1.union(myset2)

print("Union of myset1 and myset2:")
print(set3)

#practice

fruits={"apple","banana","orange"}
if("apple"in fruits):
    print("Apple is in the set.")
    
fruits.add("Banana")

print("After adding 'Banana':")
print(fruits)    