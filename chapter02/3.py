# Tuple

menu = ("Pork cutlet", "Cheeze cutlet")
print(menu[0])
print(menu[1])

name, age, hobby = "Jhon", 30, "Coding"

print(name, age, hobby)

# Set -> No duplicates
my_set = {1,2,3,4,4}
print(my_set)

# Intersection
java = {"A", "B"}
python = set(["A", "C", "D"])
print(java & python)
print(java.intersection(python))

# Combination
print(java | python)

# Difference
print (java - python)
print(java.difference(python))

# Add
python.add("K")
print(python)

# Remove
python.remove("C")
print(python)