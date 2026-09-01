#Greeting program
name = input("what\'s your name? ")
print ("hello,",name.title());

# simple calculator

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

c = a + b
print(f"sum = {a} + {b} = {c}")

c =  a - b
print(f"difference = {a} - {b} = {c}")

c = a * b
print(f"product = {a} * {b} = {c}")

c = a / b
print(f"quotient = {a} / {b} = {c}")

c = a % b
print(f"remainder = {a} % {b} = {c}")

c = a ** b
print(f"power = {a} ** {b} = {c}")


#Celsius/Fahrenheit converter
fahrenheit = float(input("Enter a temparature in fahrenheit:"))
celcius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} fahrenheit = {celcius} degree celcius ")

celcius = float(input("Enter a temparature in celcius:"))
fahrenheit = (celcius * 9/5) + 32
print(f"{celcius} celcius = {fahrenheit} degree fahrenheit ")


#bill/tip calculator
bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
print(f"Tip amount: {tip_amount : .2f}")
print(f"Total amount to be paid: {total_amount :.2f}")

# input/output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")
print(f"Hello, {name.title()}! You are {age} years old and your hobby is {hobby}.")

# arithmetic
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

c = a + b
print(f"sum = {a} + {b} = {c}")

c =  a - b
print(f"difference = {a} - {b} = {c}")

c = a * b
print(f"product = {a} * {b} = {c}")

c = a / b
print(f"quotient = {a} / {b} = {c}")

c = a % b
print(f"remainder = {a} % {b} = {c}")

c = a ** b
print(f"power = {a} ** {b} = {c}")


# max of 2 numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
max_num = max(num1, num2)
print(f"The maximum of {num1} and {num2} is {max_num}.")

# swap
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num1 = num2
num2 = num1
print(f"After swapping: first number = {num1}, second number = {num2}")

#simple interest
amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))
simple_interest = (amount * rate * time) / 100
print(f"Interest is {simple_interest : .2f}")

# area/perimeter
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area is {area}, perimeter is {perimeter}")

#digit sum
number = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in number)
print(digit_sum)

#optional
x = []
for digit in number:
    x.append(int(digit))
print(x)
sum_of_digits = sum(x)
print(sum_of_digits)

#Rewrite calculator using functions
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2)
print(f"sum = {num1} + {num2} = {result}")
result = sub(num1, num2)
print(f"difference = {num1} - {num2} = {result}")
result = mul(num1, num2)
print(f"product = {num1} * {num2} = {result}")
result = div(num1, num2)
print(f"quotient = {num1} / {num2} = {result}")

def bio(name, age):
    print(f"hey, i\'m {name.title()} and i\'m {age} years old")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
bio(name, age)