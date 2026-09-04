i = 1
while i <= 3:
    print("hello")
    i += 1
    
num = [1, 2, 3, 4]
for i in num:
    print(f"{i} sequare is {i*i}")

for i in range(5):
    print("shreya Das")
    
print("meow\n" * 5, end="")

num = int(input("Enter a num: "))
print("meow \n" * num, end= "")

while num != 0:
    print("hello")
    num -= 1
    
n = 10
def guesss_number(num):
    while True:
        num = int(input("Enter a Number: "))
        if num > n:
            print("the number is less than")
            continue
        elif num < n:
            print("the number is greater than")
            continue
        else:
            break
    print("win")

guesss_number(num)