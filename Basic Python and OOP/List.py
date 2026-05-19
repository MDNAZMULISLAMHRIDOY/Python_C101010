#String Type

list=["CSE","ICT","EEE","BBA"]

list[2]="ICE"
print(list)

print(list[-1])

print(list[0:3])

list.append("MATH")

print(list)


list.insert(2,"LAW")

list.extend(["ENGLISH","PHYSICS"])
print(list)

list.remove("ICE")

print(list)

print("List Size:",len(list))

list.pop(2)

print(list)

list.sort()

print(list)

list.reverse()

if(list==list[::-1]):
    print("Palindrome")
    
else:    print("Not Palindrome")

list.clear()
print(list)

my_list=[1.5,8.5,95.8,78.5]
print(my_list)