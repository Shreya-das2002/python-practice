class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return "A student"
        
    def student_value(self):
        print(f"{self.name} age is {self.age}")
        print(self)

def get_student():
    name = input("Enter Your Name ")
    age= input("Enter Your Age ")
    new_student = Student(name, age)
    return new_student

my_student = get_student()
my_student.student_value()

import random
class fruit:
    fruits = ["apple", "banana", "orange", "watermelon"]
    @classmethod
    def sort(frt, name):
        print(random.choice(frt.fruits), "is fav of", name)
fruit.sort("shreya")

class v_mart:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Vagetables(v_mart):
    def __init__(self, name,price, colour ):
        super().__init__(name, price)
        self.colour = colour
        
        ...
        
class Super_market(v_mart):
    def __init__(self,price, name, item):
        super().__init__(price, name)
        self.item = item
        
        ...
        
potato = Vagetables("Potato", 30, "Brown")
print(f"Item: {potato.name}, Price: {potato.price}, Colour: {potato.colour}")

store = Super_market("V-Mart Main Store", 500, "Grocery Basket")
print(f"Store: {store.name}, Total Price: {store.price}, Item Type: {store.item}")