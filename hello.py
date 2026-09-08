print("hello world");

name = input("what is your name? ")
print ("hello,",name)

print("user", end=" ")
print(name)

print("user", name, sep=" ")

print('"hello"')
print("\"hello\"")

a = 50
print(f"hello, {a}")

name = name.strip()
name = name.capitalize()
print(name)

name = input("what is your name? ").strip().title()
print(name)

x = input("Enter a number: ")
y = input("Enter a number: ")
z = int(x) + int(y)
print(z)

z = float(x) + float(y)
z = round(z)
print(f"{z : ,}")


def hello():
    name = input("what is your name? ")
    print("hello, ", name )
hello()

def hellos(a):
    print("hello ,", a )
    
name = input("what is your name? ")
hellos(name)

if __name__ == "__main__":
    name = ("what is your name? ")
    hellos(name)
