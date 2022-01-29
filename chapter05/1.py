def open_account():
    print("A new account has been created.")

def deposit(balance, money):
    print("The deposit has been completed. The balance is {0} won.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("The withdraw has been completed. The balance is {0} won.".format(balance - money))
        return balance - money
    else:
        print("The withdraw has not been completed. The balance is {0} won.".format(balance, money))
        return balance

def with_draw_night(balance, money):
    commission = 100
    balance = balance - money - commission
    print("The commission is {0} won. And the balance is {1} won.".format(commission, balance))
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 2000)
balance = withdraw(balance, 1000)
commition, balance = with_draw_night(balance, 500)
