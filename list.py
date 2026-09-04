flowers =  ["rose", "lily", "marigold", "lotus"]
colours = ["red", "white", "yellow", "pink"]
print(flowers[3])
print(len(flowers))

for i in range(len(flowers)):
    print(i, flowers[i])
    
for i in range(len(flowers)):
    print(f"{flowers[i]}: {colours[i]} ")
    
flowers[2] = "orchid"
print(flowers)
flowers.append("marigold")
print(flowers)
flowers.extend("rose")
print(flowers)
flowers.insert(2,"sunflower")
print(flowers)
flowers.remove("r")
print(flowers)
flowers.pop()
print(flowers)
flowers.sort()
print(flowers)
flowers.reverse()
print(flowers)
print(flowers[1:5])
for flowers, colours in zip(flowers, colours):
    print(f"{flowers}: {colours}")
    
y = []
for i in range(5):
    y.append(i * 2)
print(y)

