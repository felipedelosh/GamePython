"""
FelipedelosH

The worls is representate in 84x48
"""
class World:
    def __init__(self, config) -> None:
        self.idWorld = ""
        self.config = config
        self.timeSpaceNow = []
        self.w = int(self.config.get("floorW"))
        self.h = int(self.config.get("floorH"))
        self.initTheTimeSpaceNow()

    def initTheTimeSpaceNow(self):
        self.idWorld = "0"
        for i in range(0, self.h):
            self.timeSpaceNow.append([])
            for j in range(0, self.w):
                self.timeSpaceNow[i].append(0)
