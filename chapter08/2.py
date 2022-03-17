class Unit:
    def __init__(self, name, hp, damage): # init is constructor
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} unit is created.".format(self.name))
        print("HP {}, Damage {}".format(self.hp, self.damage))

# marine1 = Unit("marine", 40, 5)
# marine2 = Unit("marine", 40, 5)
# tank = Unit("Tank", 150, 35)

# wraith : air unit, airplane, clocking 
wraith1 = Unit("wraith", 80, 5)
print("Unit name : {}, Damage : {}".format(wraith1.name, wraith1.damage))

# mind control : Making opponent unit into my unit (steel)
wraith2 = Unit("Steeled wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{} is clocking ".format(wraith2.name))

