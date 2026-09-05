def greet (name, greet = "Hello"):
    print(f"{greet}, {name}")
greet("Shreya")

greet("Shreya", "Good Morning")

def max_min (number):
    lowest = min(number)
    highest = max(number)
    return lowest, highest

print(max_min([1, 2, 3, 6, 9]))
lowest, highest = max_min([1, 2, 3, 6, 9])
print(lowest)
print(highest)

def add_tax(price: int, tax_rate: float) -> float:
    return price + (price * tax_rate)
total = add_tax(100, 0.05)
print(total)