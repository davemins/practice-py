# score_file = open("score.txt", "w")
# print("Math : 0", file=score_file)
# print("English : 1000", file=score_file)
# score_file.close()

score_file = open("score.txt", "a")
score_file.write("\nScience : 80")
score_file.write("\nCoding : 90")
score_file.close()