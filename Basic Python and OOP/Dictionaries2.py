
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
},

"year":2024

    }

#Update data in dictionary

mylist["Nazmul Islam"]["Age"]=89
mylist["Nazmul Islam"].update({"Name":["Mahmudul Hasan"]})

print("Updated Dictionary: ")
print(mylist["Nazmul Islam"])

#Add new data in dictionary

print("\nAdding new data in dictionary: ")

mylist["Nazmul Islam"]["Name"].append("Murshalin")

print(mylist["Nazmul Islam"])