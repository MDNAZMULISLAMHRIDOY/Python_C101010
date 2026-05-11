
mylist={
    
    "Nazmul Islam":{
    "Strudent Id":"B210101020",
    "Name":"Md. Nazmul Islam",
    "Age":22,
    "Department":"CSE",
    "Subjects":["Programming","Data Structure","Algorithm"],
    "University":"Chandpur Science and Technology University"
    }
    ,
"Noor Hossain":{
    "Strudent Id":"B210101021",
    "Name":"Noor Hossain",
    "Age":23,
    "Department":"ICT",
    "Subjects":["Physics","Mathematics","Data Structure"],
    "University":"Chandpur Science and Technology University"
},

"year":2024

    }

print("Spacipic Information")

print(mylist["year"])


#use get mathod

print(mylist.get("Noor Hossain").get("Subjects"))

#index count
print(" print Spacipic Position")

print(mylist.get("Noor Hossain").get("Subjects").index("Data Structure"))


#find Key
print("print Keys")
print(mylist.get("Noor Hossain").keys())

#values

print("print Values")

print(mylist.get("Noor Hossain").values())
#length of the list
print("print Length of the list")
print(len(mylist))


print("\n\n")
print("Information of Nazmul Islam:")

for key, value in mylist["Nazmul Islam"].items():

    if type(value) == list:
        print(key, ":")
        
        for item in value:
            print(" -", item)
    else:
        print(key, ":", value)