class Ale:
    """
    Base class for all ale types, holding name and ABV,
    and providing methods to compute alcohol content and description.
    """
    def __init__(self, name: str, abv: float):
        self.name = name
        self.abv = abv  # alcohol by volume as a fraction

    def alcohol_content(self, volume_in_oz: float) -> float:
        """Return total alcohol amount based on ABV and volume."""
        return self.abv * volume_in_oz

    def description(self) -> str:
        """Return a formatted description string for the ale."""
        return f"{self.name}: {self.abv * 100:.1f}% ABV"


class PaleAle(Ale):
    def __init__(self):
        super().__init__("Pale Ale", 0.055)


class IPA(Ale):
    def __init__(self):
        super().__init__("IPA", 0.065)


class Stout(Ale):
    def __init__(self):
        super().__init__("Stout", 0.07)


class Porter(Ale):
    def __init__(self):
        super().__init__("Porter", 0.06)


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 