# Attach

from re import I, S


students = list(range(1, 6))
print(students)
students = [i+100 for i in students]
print(students)

# Length
students = ["Kevin", "David", "Andrew"]
students = [len(i) for i in students]
print(students)

# Capital letters
students = ["Kevin", "David", "Andrew"]
students = [i.upper() for i in students]
print(students)