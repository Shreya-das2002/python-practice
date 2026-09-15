# Safe integer input
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("This is not a number")
else:
    print(number)
    
# file word counter
text_list = [] 
with open("names.txt", "r") as file:
    lines = file.readlines() 
    
for items in lines:
    word = items.strip().split(" ")
    text_list.extend(word)
print(text_list)

# CSV student reader
import csv
student_list = []
with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_list.append({"name": row["name"], "grade": row["grade"]})
for items in student_list:
    print(f"{items['name']} : {items['grade']}")

#  error logger
import logging
logging.basicConfig(
    filename="my_error.log",
    level= logging.ERROR,
    format= "%(asctime)s - %(message)s"
)

try:
    number = 10/0
except ZeroDivisionError:
    logging.exception("Math error happened!")
    print("oops, you cannot do that!")

#Mini project 
# Using json
import json
import os
Data_file = "students.json"

def load_data():
    """Loads student data from json file"""
    if not os.path.exists(Data_file):
        print("Not found")
        return {}
    try:
        with open(Data_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Data file was corrupted")
        return {}
    
def save_data(student_dics):
    try:
        with open(Data_file, "w") as file:
            json.dump(student_dics, file, indent=4)
    except IOError:
        print("Could not save")

def valid_name(name):
    while True:
        name_input = input(name).strip()
        if not name_input:
            print("Name cannot be blank")
            continue
        if not name_input.replace(" ", "").isalpha():
            print("Name should be only alphabetical letter")
            continue
        return name_input.title()

def valid_age(age):
    while True:
        age_str = input(age).strip()
        try:
            age_input = int(age_str)
            if age_input < 4 or age_input > 100:
                print("Enter valid age between 4 and 100")
                continue
            return age_input
        except ValueError:
            print("Invalid age! Please type a number.")

def valid_grade(grade):
    while True:
        grade_input = input(grade).strip().upper()
        if not grade_input:
            print("invalid grade")
            continue
        return grade_input
    
def main():
    student = load_data()
    
    while True:
        print("\n--- STUDENT DIRECTORY ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        
        choice = input("choose an option(1-3): ")
        
        if choice == "1":
            print("\n [ Adding New Student ]")
            roll_no = input("Enter Roll Number: ").strip()
            if not roll_no:
                print("Roll number cannot be blank")
                continue
            if roll_no in student:
                print("Roll no already exists")
                continue
                
            name = valid_name("Enter Student Name: ")
            age = valid_age("Enter Student Age: ")
            grade = valid_grade("Enter Student Grade: ")
            
            student[roll_no] = {
                "Name" : name,
                "Age" : age,
                "Grade" : grade
            }
            
            save_data(student)
            print(f"{name} was successfully added")
    
        elif choice == "2":
            print("\n [ Registered Students ]")
            if not student:
                print("No record found")
            else:
                for roll, info in student.items():
                    # FIXED: Using the loop's 'roll' and 'info' dictionary keys
                    print(f"Roll_no: {roll}, Name: {info['Name']}, Age: {info['Age']}, Grade: {info['Grade']}")
                    
        elif choice == "3":
            print("Your data successfully saved") # FIXED: Capital 'P' to lowercase 'p'
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()