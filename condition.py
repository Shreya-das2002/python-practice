x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")
    
num = int(input("Enter a number: "))
if num > 60 and num < 70:
    print("your grade is C")
else:
    print("your grade is not C")

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
def is_evenor_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(is_evenor_odd(num))

fruit = input("Enter a fruit name: ")

match fruit:   
    case "apple":
        print("Apple is red")
    case "banana":
        print("Banana is yellow")
    case _:
        print("I don't know about this fruit")