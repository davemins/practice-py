# list

# subway
subway = [10, 20, 30]
print(subway)

subway = ["Anna", "David", "Brian"]
print(subway)

# Location
print(subway.index("Brian"))

# Additional
subway.append("Wenddy")
print(subway)

# Cut in
subway.insert(1, "Jhon")
print(subway)

# Unload
print(subway.pop())
print(subway)

# research
subway.append("Jhon")
print(subway)
print(subway.count("Jhon"))

# Line
num_list = [5, 1, 2, 3, 6, 4]
num_list.sort()
print(num_list)

# Reverse
num_list.reverse()
print(num_list)

# Extend
num_list.extend(num_list)
print(num_list)