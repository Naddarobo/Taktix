#
# Taktix Weapon Class
#
from taktix.game.item import Item

class Weapon(Item):
    """Weapon class."""

    def __init__(self, 
    name: str = "Weapon", 
    description: str = "A weapon", 
    damage: int = 1
    ):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.damage = damage