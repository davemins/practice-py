try:
    print("Only single-gidit division calculator")
    num1 = int(input("Enter the first digit : "))
    num2 = int(input("Enter the second digit : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Invalid value entered")