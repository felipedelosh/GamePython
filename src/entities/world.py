"""
FelipedelosH

The worls is representate in 84x48
"""
from src.levels.mapLoader import MapLoader

class World:
    def __init__(self, config) -> None:
        self.config = config # config\config.json
        self.w = int(self.config.get("floorW"))
        self.h = int(self.config.get("floorH"))
        # VARS
        self.id = "0"
        self.collider = []

    def load_map(self, path: str):
        data = MapLoader.load(path)
        self.id = data["id"]
        self.collider = data["collider"]
