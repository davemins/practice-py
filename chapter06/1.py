# exception 
try:
    print("division only calculator")
    nums = []
    nums.append(int(input("Enter the first digit : ")))
    nums.append(int(input("Enter the second digit : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error!")
except ZeroDivisionError as err:
    print(err)
except:
    print("Unknown error occurrence!!"2)