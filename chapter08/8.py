from random import *

# Normal Unit
from turtle import speed


class Unit:
    def __init__(self, name, hp, speed): # init is constructor
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} Unit is created".format(name))

    def move(self, location):
        print("[Ground Unit move]")
        print("{} : Move to {}. [Speed {}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{} : {} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{} : Present HP is {}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : Destroted.".format(self.name))

#AttackUnit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # init is constructor
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : Attack the enemy at {}. [Damage {}]"\
        .format(self.name, location, self.damage))

# Matine
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"Marine", 40, 1, 5)

    #Steempack
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : Use stimpack (Decline 10 HP)".format(self.name))
        else:
            print("{} : Can't use stimpack.".format(self.name))
        
# Tank
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"Tank", 150, 1, 35)

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_developed == False:
            print("{} : Switch to seize mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else:
            print("{} : Switch to normal mode".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# Dropship : air unit, Transport plane, marine / firebat / tank / cant't attack

# Flyable calss
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : Flying to {}. [Speed {}]"\
            .format(name, location, self.flying_speed))

# air attack unit class        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # Ground speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[Air Unit move]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False 
    
    def clocking(self):
        if self.clocked == True:
            print("{} : Released clocking mode.".format(self.name))
            self.clocked = False
        else:
            print("{} : Unreleased clocking mode.".format(self.name))
            self.clocked = True

def game_start():
    print("[Notice] Start game")

def game_over():
    print("Player : GG")
    print("[Player] was leaved")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1'o clock")

Tank.seize_developed = True
print("[Notice] Tank's seize mode all developed")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# All attack
for unit in attack_units:
    unit.attack("1'o clock")

# All damaged
    unit.damaged(randint(5, 21))

game_over()