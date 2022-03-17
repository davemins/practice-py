# NormalUnit
from turtle import speed


class Unit:
    def __init__(self, name, hp, speed): # init is constructor
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[Ground Unit move]")
        print("{} : Move to {}. [Speed {}]"\
            .format(self.name, location, self.speed))

#AttackUnit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # init is constructor
        Unit.__init__(self, name, hp, speed)
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

# Building
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

