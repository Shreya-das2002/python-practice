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
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance
        
def deposit(self, amount):
    self.balance += amount
    print(f"{self.own}")