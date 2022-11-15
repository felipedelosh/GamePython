"""
FelipedelosH

The worls is representate in 84x48
"""
class World:
    def __init__(self) -> None:
        self.idWorld = ""
        self.timeSpaceNow = []
        self.maxX = 84
        self.maxY = 48
        self.initTheTimeSpaceNow()

    def initTheTimeSpaceNow(self):
        self.idWorld = "0"
        for i in range(0, self.maxY):
            self.timeSpaceNow.append([])
            for j in range(0, self.maxX):
                self.timeSpaceNow[i].append(0)


            

