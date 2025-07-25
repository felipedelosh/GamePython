"""
FelipedelosH

The worls is representate in 84x48
"""
class World:
    def __init__(self, config) -> None:
        self.id = "0"
        self.config = config
        self.w = int(self.config.get("floorW"))
        self.h = int(self.config.get("floorH"))

