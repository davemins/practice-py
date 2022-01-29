absent = [2, 5]
no_book =[7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("What the..")
        break
    print("{}, Reading a book".format(student))