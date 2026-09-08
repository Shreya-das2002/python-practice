# Revision
# Prime Check
number = int(input("Enter a number: "))
def prime(n):
    if (n < 1):
        return "Not Prime"
    for i in (2, n):
        if n % i == 0:
            return "NOt Prime"
        else:
            return "Prime"
    return "Not Prime"
print(prime(number))

# fibonacci
length_series = (int(input("Enter The length of this series: ")))
def fibonacci(n):
    a = 0
    b = 1
    series = [a, b]
    for i in range(n - 2):
        c = series[-1] + series[-2]
        series.append(c)
        i += 1
    return series
print(fibonacci(length_series))

# Word frequency
word = input("Write a word: ").lower().strip()
new_word = {}
def word_frequency(n):
    for i in n:
        if i  in new_word:
            new_word[i] += 1
        else:
            new_word[i] = 1
    return new_word
print(word_frequency(word))

# duplicate detection
n = int(input("Enter no of lengnth of the list: "))
new_collection = []
for i in range(n):
    x = input("create a list: ")
    new_collection.append(x)
print(new_collection)

def duplicates(a):
    duplicate = []
    seen =[]
    for i in a:
        if i not in seen:
            seen.append(i)
        else:
            duplicate.append(i)
    return duplicate
print(duplicates(new_collection))

# first non-repeating char
char = input("Enter a character: ").lower().strip()
seen_char = {}
def non_repeating_char(char):
    for i in char:
        seen_char[i] = seen_char.get(i, 0) + 1
    for i in char:
        if seen_char[i] == 1:
            return i
print(non_repeating_char(char))

# two-list intersection
list_1 = {1, 2, 3, 4, 5, 6}
list_2 = {9, 10, 13, 4, 5, 6}
print(list_1.intersection(list_2))

# group marks by grade
student = {
    "shreya" : 80,
    "rinki" : 70,
    "subhankar" : 75,
    "debjani" : 50
}
def grade_calculator(student):
    grade = {}
    for name, number in student.items():
        if 100 > number >= 80 :
            grade[name]= "Grade A"
        elif 80 > number >= 70 :
            grade[name]= "Grade B"
        elif 70 > number >= 60 :
            grade[name]= "Grade C"
        elif 60 > number >= 50 :
            grade[name]= "Grade D"
        else:
            grade[name]= "F"
    return grade
print(grade_calculator(student))

# Mini project
student = {
    "name" : "shreya", "age" : 23, "hobby" : "Dance"
}

student["Gender"] = "female"
print(student)

print(student["name"])

student["age"] = 24
print(student["age"])

del student["Gender"]
print(student)