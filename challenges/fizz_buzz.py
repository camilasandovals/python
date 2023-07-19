a = 15
b = str(15)
if a > 10: 
  print(a, "is bigger than 10")
if b == "15":
  print(b, "is an string")

array = [1, 2, 3 , 4, 5, 6]

for element in array: 
  if element == 1:
    print(element)


for x in range(1, 6, 3):
  print(array[x])

print("--------------------------------------------------")
a = 15
result = "a is equal to 15" if a == "15" else "a is different"
print(result)
print("a is equal to 15" if a == "15" else "a is different")

for name in ["Sergio", "Camila", "Sandra"]:
  if name.startswith("S"):
    continue
  print(name)