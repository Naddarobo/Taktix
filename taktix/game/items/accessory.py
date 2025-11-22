#
# Taktix Accessory Class
#

from taktix.game.items.item import Item

class Accessory(Item):
    """Accessory class."""

    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.name = name
        self.description = description