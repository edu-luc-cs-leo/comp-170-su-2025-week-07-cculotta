class Vehicle:
    """
    Base class for all vehicle types, holding name and mpg,
    and providing methods to compute fuel needed and description.
    """
    def __init__(self, name: str, mpg: float):
        self.name = name
        self.mpg = mpg  # miles per gallon

    def fuel_needed(self, distance: float) -> float:
        """Return gallons of fuel needed to travel the given distance."""
        return distance / self.mpg

    def description(self) -> str:
        """Return a formatted description string for the vehicle."""
        return f"{self.name} gets {self.mpg} miles per gallon."

class Car(Vehicle):
    def __init__(self):
        super().__init__("Car", 30)

class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", 15)

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle", 50)

class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 8)


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 