

mylist={
    
    "Nazmul Islam":{
    "Strudent Id":"B210101020",
    "Name":["Md. Nazmul Islam"],
    "Age":22,
    "Department":"CSE",
    "Subjects":["Programming","Data Structure","Algorithm"],
    "University":"Chandpur Science and Technology University"
    }
    ,
"Noor Hossain":{
    "Strudent Id":"B210101021",
    "Name":["Noor Hossain"],
    "Age":23,
    "Department":"ICT",
    "Subjects":["Physics","Mathematics","Data Structure"],
    "University":"Chandpur Science and Technology University"
}
    }

#Iterating through dictionary

print("Iterating through dictionary: ")
for i in mylist:
    print(i)
    
#Iterating through dictionary values
print("\nIterating through dictionary values: ")      
for a in mylist.values():
    print(a)    
    
print("\nIterating through dictionary items: ")    
for key, value in mylist.items():

    if type(value) == list:
        print(key, ":")
        
        for item in value:
            print(" -", item)
    else:
        print(key, ":", value)   