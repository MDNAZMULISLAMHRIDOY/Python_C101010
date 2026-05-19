
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

mylist.get("Nazmul Islam").pop("Strudent Id")

print("After poping data from dictionary: ")
print(mylist)

mylist.popitem()

print("\nAfter poping last item from dictionary: ")
print(mylist)

mylist.get("Nazmul Islam").clear()

print("\nAfter clearing data from dictionary: ")
print(mylist)



    
    




