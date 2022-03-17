# NormalUnit
class Unit:
    def __init__(self, name, hp, damage): # init is constructor
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} unit is created.".format(self.name))
        print("HP {}, Damage {}".format(self.hp, self.damage))

#AttackUnit
class AttackUnit:
    def __init__(self, name, hp, damage): # init is constructor
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{} : Attack the enemy at {}. [Damage {}]"\
        .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{} : Present HP is {}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : Destroted.".format(self.name))

# Firebat : attack unit, flame thrower
firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack("5'o clock")

firebat1.damaged(25)
firebat1.damaged(25)