#yesterday's revision

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
def add(a,b):
    c = a + b
    return c

def difference(a,b):
    c = a - b
    return c

def product(a,b):
    c = a * b
    return c

def quotient(a,b):
    c = a / b
    return c

def calculator(a, b):
    print(f"sum = {add(a, b)}")
    print(f"difference = {difference(a, b)}")
    print(f"product = {product(a, b)}")
    print(f"quotient = {quotient(a, b)}")

calculator(a, b)

# Grade calculator
marks = int(input("Enter your marks: "))
def grade_calculator(marks):
    if marks >= 80:
        return "Grade is A"
    elif marks >= 70:
        return "Grade is B"
    elif marks >= 60:
        return "Grade is C"
    elif marks >= 50:
        return "Grade is D"
    else:
        return "Grade is F"
    
print(grade_calculator(marks))

# leap year
year = int(input("Enter a year: "))
def is_leap_year(year):
    if (year % 4 == 0 and  year % 100 != 0 or year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
print(is_leap_year(year))

# largest of 3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
def largest_of_three(num1, num2, num3):
    if num2 < num1 > num3:
        return f"{num1} is the largest number"
    elif num1 < num2 > num3:
        return f"{num2} is the largest number"
    else:
        return f"{num3} is the largest number"
print(largest_of_three(num1, num2, num3))

# vowel/consonant
alpha = input("Enter a letter: ")
letter = alpha.lower()
vowel = ["a", "e", "i", "o", "u"]
def is_vowel_or_consonant(letter):
    if (letter in vowel):
        return f"{letter} is a vowel"
    else:
        return f"{letter} is a consonant"
print(is_vowel_or_consonant(letter))

# password rule checker
password = input("Enter a password: ")
symbols = ["@", "#", "$", "%", "&", "*", "!", "?"]
def password_rule_checker(password):
    if len(password) >= 8:
        if (any(char.isupper()) for char in password) and (any(char.islower()) for char in password) and (any(char.isdigit()) for char in password):
            if (any(char in symbols for char in password)):
                return "Password is valid"
            else:
                return "Password is invalid"       
        else:
            return "Password is invalid"
    else:
        return "Password is invalid"
print(password_rule_checker(password))

# Reverse string
string = input("Enter a string: ")
def reverse_string(string):
    return string[::-1]
print(reverse_string(string))

# palindrome
def is_palindrome(string):
    if string == reverse_string(string):
        return f"{string} is a palindrome"
    else:
        return f"{string} is not a palindrome"
print(is_palindrome(string))

# word count
word = input("Enter a word: ").lower().strip()
word_count = {}
def count_of_word(text):
    for letter in text:
        if(letter in word_count):
            word_count[letter] += 1
        else:
            word_count[letter] = 1
    return word_count
print(f"word count: {count_of_word(word)}")

# frequency of a character
word = input("Enter a word:").strip()
frequency_character_no = {}
def frequency_character(char):
    for letter in char: 
        if ( letter in frequency_character_no ):
            frequency_character_no[letter] += 1
        else:
            frequency_character_no[letter] = 1
    return frequency_character_no;
print(f"frequency of character: {frequency_character(word)}")

# remove spaces
text = "  shreya is a girl  "
text = text.replace(" ", "")
print(text)

# capitalize words
text = text.capitalize()
print(text)

# Mini project 
username = input("Enter a username: ")
symbols = ["@", "#", "$", "%", "&", "*", "!", "?"]
def rules(user):
    if len(user) >= 8 :
        if (any(char.isupper() for char in user)):
            return "valid"
        elif (any(char.islower() for char in user)):
            return "valid"
        elif  (any(char.isdigit() for char in user)):
            return "valid"
        elif  (any(char in symbols for char in user)):
            return "valid"
        else:
                return "invalid"
    else:
        return "invalid"
print(rules(username))