bio = {
    "name": "shreya",
    "age": 23,
    "hobby": "dance" 
} 
print(bio["name"])
for i in bio:
    print(i,":", bio[i])
    
student = [{
    "name": "shreya",
    "age": 23,
    "hobby": "dance" 
},
    {"name": "rinki",
    "age": 24,
    "hobby": "tuition" }
            ]
print(student)

print("? " * 4)

def sequare(x):
    for i in range(x):
            print("###\n" * x, end= "")
            
sequare(2)