#
# Taktix Item Class
#

class Item:
    """Item class."""

    def __init__(self, name: str, description: str, value: int):
        self.name = name
        self.description = description