# # Safe integer input
# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("This is not a number")
# else:
#     print(number)
    
# file word counter
text_list = []
with open("names.txt", "r") as file:
    lines = file.readlines() 
    
for items in lines:
    word = items.strip().split(" ")
    text_list.extend(word)
print(text_list)

# CSV student reader
import csv
student_list = []
with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_list.append({"name": row["name"], "grade": row["grade"]})
for items in student_list:
    print(f"{items['name']} : {items['grade']}")
    