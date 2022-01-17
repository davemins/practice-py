# Conditional IF

# weather = input("How is the wheather today? ")
# if weather == "rain" or "snow":
#     print("Take an umbrella.")
# elif weather == "micro dust":
#     print("Take a mask")
# else:
#     print("Don't need anything")

temp = int(input("How is the temperature today? "))
if 30 <= temp:
    print("Too hot. Better not to go out.")
elif 10 <= temp and temp < 30:
    print("The weather is nice.")
elif 0 <= temp and temp < 10:
    print("Take a coat")
else:
    print("Too cold. Better not to go out. ")