# NormalUnit
class Unit:
    def __init__(self, name, hp): # init is constructor
        self.name = name
        self.hp = hp

#AttackUnit
class AttackUnit(Unit):
    def __init__(self, name, hp, damage): # init is constructor
        Unit.__init__(self, name, hp)
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
        print("{} : Flying {}. [Speed at : {}]"\
            .format(name, location, self.flying_speed))

# air attack unit class        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# Valkyrie : air attack unit
valkyrie = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3'o clock")
