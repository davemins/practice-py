class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("Only single-gidit division calculator")
    num1 = int(input("Enter the first digit : "))
    num2 = int(input("Enter the second digit : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("Entered Value : {}, {}".format(num1, num2))
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Invalid value entered")
except BigNumberError as err:
    print(err)