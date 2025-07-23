"""
FelipedelosH
"""
from src.core.assetManager import AssetManager
from src.core.stateMachine import *

class Player:
    def __init__(self, config) -> None:
        self.assetManager = AssetManager.get_instance()
        self.config = config # Inyect config in Player
        self.sprite = {}
        self.player_look_to = "up"
        self.posX = 500
        self.posY = 200
        self.max_pos_x = 0
        self.max_pos_y = 0
        self.age = 0
        self.name = "Player"
        self.health = 100
        self.attack = 1
        self.defend = 1
        self.inteligence = 1
        self.stanmina = 10
        self.velocity = 3
        # SET PLAYER VALUES
        self._init_player()

    def player_mouve_up(self):
        if (self.posY-self.velocity>0):
            self.posY = self.posY - self.velocity
            self.player_look_to = "up"

    def player_mouve_down(self):
        if self.posY+150 < self.max_pos_y: #150 is h of sprite.png
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
    
    def _init_player(self):
        self.max_pos_x = int(self.config.get("displayW"))
        self.max_pos_y = int(self.config.get("displayH"))
        self.posX = 200
        self.posY = 100
        self.velocity = int(self.config.get("playerVelocity"))
