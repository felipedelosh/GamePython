"""
FelipedelosH
This is the main controller to my videogame
"""
import json
from src.core.GameConfig import GameConfig
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
        self.configuration = self.config._config
        self.FPS = int(1000/int(self.configuration["FPS"]))
        self.control = Control(
            self.config.get('key_UP', 38),
            self.config.get('key_RIGTH', 39),
            self.config.get('key_DOWN', 40),
            self.config.get('key_LEFT', 37),
            self.config.get('key_SELECT', 32),
            self.config.get('key_START', 13),
            self.config.get('key_B', 90),
            self.config.get('key_A', 88),
            self.config.get('key_Y', 67),
            self.config.get('key_X', 86),
            self.config.get('key_L', 65),
            self.config.get('key_R', 83)
        )
        # Sprites & IMAGES
        self.imgIntro =  PhotoImage(file="assets/images/intro.gif")
        # Player
        self.player = Player()
        self._setPlayer()
        self.gameStateManager = GameStateManager(self.configuration["statesMachines"], self.control)
        self.SMgame = self.gameStateManager.getStateMachine("game")
        self.mainMenuSM = self.gameStateManager.getStateMachine("mainMenu")
        self.inputHandler = InputHandler(self.player, self.control, self.mainMenuSM, self.SMgame)
        self.world = World()
        # GRAPHICS
        self.renderer = TkinterRenderer(self.canvas, self.configuration, self.player, self.world)
        self.UImanager = UIManager(self.renderer)
        self.UImanager.set_intro_image(self.imgIntro)
        self.UImanager.set_game_state_manager(self.gameStateManager)
        # VARS
        self.intro_shown_time = 0

    def keyPressed(self, keycode):
        self.inputHandler.handleKeypress(keycode)

    def setConfigDefaultOptions(self):
        self.configuration["displayW"]="1280"
        self.configuration["displayH"]="720"
        self.configuration["playerName"]="Human"
        self.configuration["playerAge"]="0"
        self.configuration["playerSpriteLookUP"]="player_look_up.png"
        self.configuration["FPS"]="30"
        self.configuration["intro_duration"]=1000

    def showIntro(self):
        self.UImanager.showIntro()
        
    def showMainMenu(self):
        self.UImanager.showMainMenu()

    def showGame(self):
        self.UImanager.showGame()

    def _deleteCanvasNotGameItems(self):
        self.canvas.delete("intro")
        self.canvas.delete("mainMenu")

    def _setPlayer(self):
        # Load all player images
        self.player.set_player_sprites(self.configuration)
        self.player.max_pos_x = int(self.configuration["displayW"])
        self.player.max_pos_y = int(self.configuration["displayH"])
        self.player.posX = 100
        self.player.posY = 100
        self.player.velocity = int(self.configuration["playerVelocity"])
