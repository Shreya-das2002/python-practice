num = (1, 2, 3, 4)
num2 = (5, 6, 7, 8)
x, *y = (5, 4, 9)
print(y, x)
print(tuple(zip(num, num2)))
print(tuple(enumerate(num2)))


