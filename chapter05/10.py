score_file = open("score.txt", "r")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")

print("\n")

score_file = open("score.txt", "r")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

print("\n")

score_file = open("score.txt", "r")
lines = score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()
