i=0
my_list=[45,89,56,78,90,34,23,12,67,45]

while i<len(my_list):
    if(my_list[i]%4==1):
     print(my_list[i],end=" ")
    i+=1


print("\n")

sum=0
average=0.0
j=0
while j<len(my_list):
    sum+=my_list[j]
    j+=1
    
average=sum/len(my_list)

print("Enter the sum of the list is:",sum)
print("Enter the average of the list is: ",average)
