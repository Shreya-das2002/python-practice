# create student
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def student_value(self):
        print(f"{self.name} : {self.grade}")
    
def student_list():
    name = input("Enter your name: ")
    grade = input("Enter your Grade: ")
    new_student = Student(name, grade)
    return new_student

new_student_list = student_list()
new_student_list.student_value()

# BankAccount
class Bank():
    def __init__(self, acc_holder, balance= 0):
        self.acc_holder = acc_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be more than 0")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient amount")
        elif amount <= 0:
            print("withdrawal amount always positive")
        else:
            self.balance -= amount
            print(f"Withdraw {amount}. New Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.acc_holder} | Balanace: {self.balance}")
        
def my_account():
    name= input("Enter Account_holder name: ").strip()
    return Bank(name)

def bank_option(account):
    while True: # Added a loop so the menu keeps running until you choose to exit
        print("\n--- Choose a Option (1-4): ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        check = input("choose a option: ").strip()
        
        if check == "1":
            amt = int(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif check == "2":
            amt = int(input("Enter amount to withdraw: "))
            account.withdraw(amt) 
        elif check == "3":
            account.display_balance()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        
if __name__ == "__main__":
    bank_account = my_account()
    bank_option(bank_account) 

# Employee classes
class Employee:
    def __init__(self, emp_name, salary, job_title, emp_id):
        self.emp_name = emp_name
        self.salary = salary
        self.job_title = job_title
        self.emp_id = emp_id
        
    def display_details(self):
        print("\n--- Employee Profile ---")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Role: {self.job_title}")
        print(f"Salary: ₹{self.salary}")
        
def employee_details():
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Emp ID: ")
    salary = input("Enter Your Salary: ")
    job_title = input("Enter Job Title: ")
    return Employee(name, salary, job_title, emp_id)

if __name__ == "__main__":
    my_employee = employee_details()
    my_employee.display_details()
    
# Mini Project 
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
                    print(f"Roll_no: {roll}, Name: {info['Name']}, Age: {info['Age']}, Grade: {info['Grade']}")
                    
        elif choice == "3":
            print("Your data successfully saved") 
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()