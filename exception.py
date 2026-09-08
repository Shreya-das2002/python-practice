try:
    x = int(int(input("What is x? ")))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

try:
    x = int(int(input("What is x? ")))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

while True:
    try:
        x = int(int(input("What is x? ")))
    except ValueError:
        print("x is not an integer")
    else:
        break  
print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(int(input("What is x? ")))
        except ValueError:
            print("x is not an integer")
        else:
            break  
    return x
print(get_int())

try:
    num = int(input("Enter a number: "))
    result =  10/0
except ValueError:
    print("Enter number not string")
except ZeroDivisionError:
    print("Cannot devide a number by 0")
else:
    print(f"Quotient = {result}")
finally:
    print("than you")
    
def age_check(age):
    if age <= 0:
        raise ValueError("Age cannot be a ne number")
    if age >= 12:
        print(" Apllicable ")
    else:
        print("Sorry, not applicable")
n = int(input("Enter your age: "))
try:
    age_check(n)
except ValueError as error:
    print(error)

