sum=0
for i in range (1,100):
    if(i>11):
        break
    sum=sum+1
    
    if(sum==5):
        continue
    
print(sum)