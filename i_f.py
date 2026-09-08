name = input("what is your name? ")


file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

with open("names.txt", "r") as file:
    lines = file.readlines() 
for i in lines:
    print("hello", i.rstrip())

names = []
    
with open("names.txt", "r") as file:
    for i in file:
        names.append(i.rstrip())
for i in sorted(names):
    print("hello", i.rstrip())

with open("names.txt", "r") as file:
    for i in sorted(file):
        print("hello", i.rstrip())

with open("names.txt", "r") as file:
    for i in sorted(file, reverse=True):
        print("hello", i.rstrip())


with open("names.csv") as file:
    for i in file:
        row = i.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]} and works as a {row[2]}")

student = []
with open("names.csv") as file:
    for i in file:
        name, colour, fruit = i.rstrip().split(",")
        student_data = {"name" : name, "colour": colour, "fruit": fruit}
        student.append(student_data)
def get_name(student): 
    return student["name"] 
    
for item in sorted(student, key= get_name):
    print(f"{item['name']} loves the color {item['colour']} and likes eating {item['fruit']}")

for item in sorted(student, key= lambda student: student["name"]):
    print(f"{item['name']} loves the color {item['colour']} and likes eating {item['fruit']}")

import csv
student = []
with open("names.csv") as file:
    reader = csv.reader(file)
    for  row in reader:
        student.append({"name": row[0], "colour": row[1], "fruit": row[0]})
for item in sorted(student, key= lambda student: student["name"]):
    print(f"{item['name']} loves the color {item['colour']} and likes eating {item['fruit']}")



student = []
with open("names.csv") as file:
    reader = csv.DictReader(file)
    for  row in reader:
        student.append({"name": row["name"], "colour": row["colour"], "fruit": row["fruit"]})
for item in sorted(student, key= lambda student: student["name"]):
    print(f"{item['name']} loves the color {item['colour']} and likes eating {item['fruit']}")


name = input("what is your name? ")
colour = input("what is your colour? ")
fruit = input("what is your fav fruit? ")

with open("names.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, colour, fruit])

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "colour", "fruit"])
    writer.writerow( {"name" : name, "colour": colour, "fruit": fruit})