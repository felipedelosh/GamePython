"""
FelipedelosH
This is the main controller to my videogame
"""
from src.core.GameConfig import GameConfig
from src.core.assetManager import AssetManager
from src.UI.TkinterRenderer import TkinterRenderer
from src.UI.UIManager import UIManager
from tkinter import NW
from tkinter import LAST
from tkinter import PhotoImage
from src.core.inputHandler import InputHandler
from src.core.gameStateManager import GameStateManager
from src.core.control import Control
from src.entities.player import Player
from src.entities.world import World
from time import sleep


class Controller:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.config = GameConfig()
        self.config.load('config/config.json')
        self.FPS = int(1000/int(self.config.get("FPS")))
        self.control = Control(
            self.config.get('key_UP'),
            self.config.get('key_RIGTH'),
            self.config.get('key_DOWN'),
            self.config.get('key_LEFT'),
            self.config.get('key_SELECT'),
            self.config.get('key_START'),
            self.config.get('key_B'),
            self.config.get('key_A'),
            self.config.get('key_Y'),
            self.config.get('key_X'),
            self.config.get('key_L'),
            self.config.get('key_R')
        )
        # Sprites & IMAGES
        self.assetManager = AssetManager.get_instance()
        self.imgIntro =  PhotoImage(file="assets/images/intro.gif")
        # Player
        self.player = Player()
        self._setPlayer() # Refactor>>TO DELETE 
        self._load_assets()
        self.gameStateManager = GameStateManager(self.config.get("statesMachines"), self.control)
        self.SMgame = self.gameStateManager.getStateMachine("game")
        self.mainMenuSM = self.gameStateManager.getStateMachine("mainMenu")
        self.inputHandler = InputHandler(self.player, self.control, self.mainMenuSM, self.SMgame)
        self.world = World()
        # GRAPHICS
        self.renderer = TkinterRenderer(self.canvas, self.config, self.player, self.world)
        self.UImanager = UIManager(self.renderer)
        self.UImanager.set_intro_image(self.imgIntro)
        self.UImanager.set_game_state_manager(self.gameStateManager)
        # VARS
        self.intro_shown_time = 0

    def keyPressed(self, keycode):
        self.inputHandler.handleKeypress(keycode)

    def showIntro(self):
        self.UImanager.showIntro()
        
    def showMainMenu(self):
        self.UImanager.showMainMenu()

    def showGame(self):
        self.UImanager.showGame()

    def _load_assets(self):
        player_sprites = {
            "up": f"assets/images/player/{self.config.get("player_look_up")}",
            "left": f"assets/images/player/{self.config.get("player_look_left")}",
            "right": f"assets/images/player/{self.config.get("player_look_right")}",
            "down": f"assets/images/player/{self.config.get("player_look_down")}"
        }
        self.assetManager.load_sprite_group("player", player_sprites)

    def _setPlayer(self):
        # Refactor... LOAD ALL from CONFIG.
        self.player.max_pos_x = int(self.config.get("displayW"))
        self.player.max_pos_y = int(self.config.get("displayH"))
        self.player.posX = 100
        self.player.posY = 100
        self.player.velocity = int(self.config.get("playerVelocity"))
