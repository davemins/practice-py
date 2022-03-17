# Marine : attack unit, soldier, rifleman

name = "Marine"
hp = 40 # health point
damage = 5

print("{} unit is created.".format(name))
print("HP {}, Damage {}\n".format(hp, damage))

# Tank : attack unit, tank, general mode, seige mode

tank_name = "Tank"
tank_hp = 150
tank_damage = 35

print("{} unit is created.".format(tank_name))
print("HP {}, Damage {}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{} : Attack in the direction of {}. [Attacking Power : {}]".format(name, location, damage))

attack(name, "1:00", damage)
attack(tank_name, "1:00", tank_damage)

