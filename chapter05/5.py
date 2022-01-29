gun = 10

#1 Global

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[Inside the function] left guns : {}".format(gun))
    return gun

gun = checkpoint(2)
print("[Outside the function] left guns : {}".format(gun))

#2 Parameter

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[Inside the funrion] left guns : {}".format(gun))
    return gun

gun = checkpoint_ret(gun, 2)
print("[Outside the function] left guns : {}".format(gun))
