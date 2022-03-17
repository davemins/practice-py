# Quiz Chicken restaurant
# Condition 1 : ValueError
# Condition 2 : 10 chicken

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[Remaining Chicken : {}]".format(chicken))
        order = int(input("How many chicken would you like to order? "))
        if order > chicken:
            print("We don't have enough ingredients.")
        elif order <= 0:
            raise ValueError
        else:
            print("[waiting Niumber : {}] Your order for {} chickens has been completed" \
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("Invalid value enterd.")
    except SoldOutError:
        print("We are out of stock and no longer accept orders.")
        break