print("Python", "JAVA", sep=" vs ", end=" ")

print("What would be more fun?")

import sys
print("Python", "Java", file=sys.stdout) # standard output
print("Python", "Java", file=sys.stderr) # standard error

scores = {"math":0, "English":50, "Coding":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).ljust(4), sep=": ")

# Waiting Number
for num in range(1, 21):
    print("Waiting Number : " + str(num).zfill(3))

answer = input("Input any value : ")
print("The input value is " + answer + ".")