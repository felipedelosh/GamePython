"""
FelipedelosH
"""
from src.core.assetManager import AssetManager

class Player:
    def __init__(self, config) -> None:
        self.config = config # config\config.json
        self.assetManager = AssetManager.get_instance()
        self.sprite = {}
        self.player_look_to = "up"
        self.posX = 500
        self.posY = 200
        self.max_pos_x = int(self.config.get("displayW"))
        self.max_pos_y = int(self.config.get("displayH"))
        self.age = 0
        self.name = "Player"
        self.health = 100
        self.attack = 1
        self.defend = 1
        self.inteligence = 1
        self.stanmina = 10
        self.velocity = int(self.config.get("playerVelocity"))

    def player_mouve_up(self):
        if self.posY-self.velocity > 0:
            self.posY = self.posY - self.velocity
            self.player_look_to = "up"

    def player_mouve_down(self):
        if self.posY+150 < self.max_pos_y:
            self.posY = self.posY + self.velocity
            self.player_look_to = "down"

    def player_mouve_rigth(self):
        if self.posX+self.velocity < self.max_pos_x-50:#50 is w of sprite.png
            self.posX = self.posX + self.velocity
            self.player_look_to = "right"

    def player_mouve_left(self):
        if self.posX > 0:
            self.posX = self.posX - self.velocity
            self.player_look_to = "left"

    def getPlayerSprite(self):
        return self.assetManager.get_sprite("player", self.player_look_to)
