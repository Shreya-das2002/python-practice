# Yesterday revision
#palindrome
num = input("Enter a number: ").lower().strip()
reverse = num[::-1]
print(reverse)

def palindrome_check():
    if (num == reverse):
        print("palindrome")
    else:
        print("not palindrome")   
palindrome_check()

#  Grade calculator
n = int(input("Enter a number: "))
def grade_calculator(number):
    if 100 > number > 80 :
        print("Grade A")
    elif 80 > number > 70 :
        print("Grade B")
    elif 70 > number > 60 :
        print("Grade C")
    elif 60 > number > 50 :
        print("Grade D")
    else:
        print("Grade F")
        
grade_calculator(n)

# Factorial
num = int(input("Enter a number: "))
def factorial(num):
    if(num < 0):
        print("Negetive number does not accept")
    if (num == 0):
        return 1
    return num * factorial(num - 1)
print(factorial(num))

# Fibonacci
a = 0
b = 1
num = [a, b]
def fibonaco():
    for _ in range(6):
        c = num[-1] + num[-2]
        num.append(c)
    
fibonaco()
print(num)

# multiplication table

number = int(input("Enter a number for multiplication table: "))
i = 1
while i < 11:
    print(f"{number} * {i} = {number * i}")
    i += 1

# prime check
number = int(input("Enter a number: "))
def prime_check(n):
    if (n <= 1):
        return "Not Prime"
    else:
        for i in range(2, n):
            if n % i == 0:
                return "Not Prime"
            else:
                return "Prime"
        return "prime"
print(prime_check(number))

# sum 1-n:
n = int(input("enter a number: "))
def num(n):
        x = n*(n+1)
        y = x / 2
        return y
print(num(n))

digit = input("enter digits: ")
def count_digits(n):
    if len(n) < 11:
        n = 10 - len(n)
        int(input(f"enter {n} number more: "))
        print("accpet")
    elif len(n) > 11:
        print("Not accpet")
    else:
        print("accpet")

count_digits(digit)

# Find max/min

number = [10, 60, 90, 50, 80, 70]

def max_num (a):
    current_max = a[0]
    for i in range(len(a)):
        if (a[i] > current_max):
            current_max = a[i]
    return current_max
print(max_num(number))

def min_num (a):
    current_max = a[0]
    for i in range(len(a)):
        if (a[i] < current_max):
            current_max = a[i]
    return current_max
print(min_num(number))

# min/max
print(max(number))
print(min(number))

# remove duplicates
number = []
i = 0
x = int(input("enter the array lenth: "))
while i < x:
    n = int(input("Enter a number: "))
    number.append(n)
    i += 1
print(number)

def remove_num (n):
    new_number = []
    for i in n:
        if i not in new_number:
                new_number.append(i)
    return new_number
print(remove_num(number))

# second largest
array = [2, 6, 19, 7, 8, 10]
def first_largest(array):
    first_largest = array[0]
    for i in range(len(array)):
        if (array[i] > first_largest):
            first_largest = array[i]
    return first_largest
n = first_largest(array)
new_array = array.remove(n)

def second_largest(new_array):
    second_largest = new_array[0]
    for i in range(len(new_array)):
        if (new_array[i] > second_largest):
            second_largest = new_array[i]
    return second_largest
print(second_largest(array))

# Rotating list
a = [1, 2, 3, 5]
a.reverse()
print(a)

# even/odd
num = int(input("Enter a number: "))
def even_odd (n):
    if (n % 2 == 0):
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
        
even_odd(num)

# Mini Project 
n = int(input("Enter Your Marks: "))
def marks_manager(n):
    if (100 > n > 80):
        print("Grade A")
    elif (80 > n > 70):
        print("Grade B")
    elif (70 > n > 60):
        print("Grade c")
    elif (60 > n > 40):
        print("Grade D")
    else:
        print("F")
marks_manager(n)