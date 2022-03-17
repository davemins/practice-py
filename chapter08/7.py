class Unit:
    def __init__(self):
        print("Unit constructor")
    
class Flyable:
    def __init__(self):
        print("Flyable constructor")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self )
        
# Drop ship
dropship = FlyableUnit()
