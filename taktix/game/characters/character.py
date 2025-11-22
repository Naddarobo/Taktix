#
# Taktix Character Class
#

from taktix.game.items.weapon import Weapon
from taktix.game.items.accessory import Accessory

class Character:
    """Character class."""

    def __init__(
        self, 
        name: str = "Character", 
        base_health: int = 100, 
        base_attack: int = 10, 
        base_defense: int = 10,
        base_armour: int = 3,
        weapons: list[Weapon] = [],
        accessories: list[Accessory] = [],
        ):
        self.name = name
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_armour = base_armour
        self.weapons = weapons
        self.accessories = accessories

