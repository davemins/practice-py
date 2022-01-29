def profile(name, age, *language):
    print("name : {}\tage : {} \t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("Carlos", 24, "C", "C++", "Python", "Java")
profile("Carina", 24, "Python")