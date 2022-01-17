
cabinet = {3:"Anna", 100:"David"}
print(cabinet[3])

print(cabinet.get(3))
print(cabinet.get(4, "Available"))

print(3 in cabinet)
print (5 in cabinet)

# Newbie
print(cabinet)
cabinet[4] = "Jhon"
print(cabinet)

# Del
del cabinet[3]
print(cabinet)

# just ouput key 
print(cabinet.keys())

# just output value
print(cabinet.values())

# output pair of data
print(cabinet.items())