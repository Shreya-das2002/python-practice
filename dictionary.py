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

student_bio = {
    "Name" : "Shreya Das",
    "Age" : 23,
    "Qualification" : "B.tech",
    "Hobby" : "Dance & drawing",
    "Gender": "Female"
    }

print(student_bio["Name"])
del student_bio["Hobby"]
print(student_bio)
student_bio["Hobby"] = "Doing Nothing"
print(student_bio)
print(student_bio.keys())
print(student_bio.values())
print(student_bio.items())
print(student_bio.get("Gender"))

for i in student_bio:
    print(i)
for i in student_bio.values():
    print(i)
    
for name, vales in student_bio.items():
    print(f"{name} : {vales}" )