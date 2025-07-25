"""
FelipedelosH
"""
from src.core.assetManager import AssetManager

class Player:
    def __init__(self, config) -> None:
        self.config = config # config\config.json
        self.assetManager = AssetManager.get_instance()
        self.name = "Player"
        self.sprite = {}
        self.player_look_to = "up"
        self.posX = self.config.get("displayW") / 4
        self.posY = self.config.get("displayH") / 4
        self.max_pos_x = self.config.get("displayW")
        self.max_pos_y = self.config.get("displayH")
        self.w = self.config.get("player_w")
        self.h = self.config.get("player_h")
        self.age = 0
        self.health = 100
        self.attack = 1
        self.defend = 1
        self.inteligence = 1
        self.stanmina = 10
        self.velocity = int(self.config.get("playerVelocity"))

    def player_mouve_up(self):
        _, _y = self.getSpriteRenderCoords()
        if _y - self.velocity > 0:
            self.posY = self.posY - self.velocity
            self.player_look_to = "up"

    def player_mouve_down(self):
        _, _y = self.getSpriteRenderCoords()
        if _y + self.h + self.velocity < self.max_pos_y:
            self.posY = self.posY + self.velocity
            self.player_look_to = "down"

    def player_mouve_rigth(self):
        _x, _ = self.getSpriteRenderCoords()
        if _x + self.w + self.velocity < self.max_pos_x:
            self.posX = self.posX + self.velocity
            self.player_look_to = "right"

    def player_mouve_left(self):
        _x, _ = self.getSpriteRenderCoords()
        if _x - self.velocity > 0:
            self.posX = self.posX - self.velocity
            self.player_look_to = "left"

    def getPlayerSprite(self):
        return self.assetManager.get_sprite("player", self.player_look_to)
    
    def getSpriteRenderCoords(self):
        _x = self.posX - (self.w / 2)
        _y = self.posY - (self.h / 2)

        return _x, _y
