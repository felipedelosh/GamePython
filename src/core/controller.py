"""
FelipedelosH
This is the main controller to my videogame
"""
import json
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
        self.configuration = {}
        self.loadConfiguration()
        self.FPS = int(1000/int(self.configuration["FPS"]))
        self.control = Control(
            self.configuration["key_UP"],
            self.configuration["key_RIGTH"],
            self.configuration["key_DOWN"],
            self.configuration["key_LEFT"],
            self.configuration["key_SELECT"],
            self.configuration["key_START"],
            self.configuration["key_B"],
            self.configuration["key_A"],
            self.configuration["key_Y"],
            self.configuration["key_X"],
            self.configuration["key_L"],
            self.configuration["key_R"])
        self.language = {} # Containt a language
        self.loadLanguage()
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
        self.renderer = TkinterRenderer(self.canvas)
        self.UImanager = UIManager(self.renderer)
        self.UImanager.set_intro_image(self.imgIntro)
        self.UImanager.set_game_state_manager(self.gameStateManager)
        # VARS
        self.intro_shown_time = 0
        self.IdTempWorldToPaint = ""


    def keyPressed(self, keycode):
        self.inputHandler.handleKeypress(keycode)


    def loadLanguage(self, language="ESP"):
        try:
            f = open(f"assets/LAN/{language}/text.txt", 'r')
            for i in f.read().split("\n"):
                if str(i).strip() != "":
                    info = i.split("=")
                    self.language[str(info[0])]=str(info[1])
        except:
            self.setLanguageDefault()

    def loadConfiguration(self):
        try:
            with open('config/config.json', 'r') as f:
                self.configuration = json.load(f)
        except:
            self.setConfigDefaultOptions()


    def setConfigDefaultOptions(self):
        self.configuration["displayW"]="1280"
        self.configuration["displayH"]="720"
        self.configuration["playerName"]="Human"
        self.configuration["playerAge"]="0"
        self.configuration["playerSpriteLookUP"]="player_look_up.png"
        self.configuration["FPS"]="30"
        self.configuration["intro_duration"]=1000
        self._setConfigDefaultOptionsController()  
    

    def _setConfigDefaultOptionsController(self):
        self.configuration["key_U"]=38
        self.configuration["key_RIGTH"]=39
        self.configuration["key_DOWN"]=40
        self.configuration["key_LEFT"]=37
        self.configuration["key_SELECT"]=32
        self.configuration["key_START"]=13
        self.configuration["key_B"]=90
        self.configuration["key_A"]=88
        self.configuration["key_Y"]=67
        self.configuration["key_X"]=86
        self.configuration["key_L"]=65
        self.configuration["key_R"]=83


    def setLanguageDefault(self):
        self.language["gameTitle"]="LokoGame"

    def showIntro(self):
        self.UImanager.showIntro()
        
    def showMainMenu(self):
        self.UImanager.showMainMenu()

    def showGame(self):
        self.UImanager.showGame()
        #self._deleteCanvasNotGameItems()
        self._paintMatrix(self.canvas)
        self.paintPlayer(self.canvas)
        

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
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
    def paintPlayer(self, canvas):
        # Delete a player anf then paitn a sprite
        canvas.delete("player")
        canvas.create_image(self.player.posX,self.player.posY,image=self.player.getPlayerSprite(), anchor=NW, tag="player")


    def _paintMatrix(self, canvas):
        # Divide a screem in world dimensions
        if self.world.idWorld != self.IdTempWorldToPaint:
            canvas.delete("world")
            if self.SMgame.pointer == "gameStart":
                _x = float(self.configuration["displayW"])/84
                _y = float(self.configuration["displayH"])/48
                for i in range(0, self.world.maxY):
                    for j in range(0, self.world.maxX):
                        if i%2==0 and j%2==0:
                            canvas.create_rectangle(_x*j,_y*i,_x*(j+1),_y*(i+1), fill="black", tags="world")
                        else:
                            canvas.create_rectangle(_x*j,_y*i,_x*(j+1),_y*(i+1), fill="red", tags="world")

                self.IdTempWorldToPaint = self.world.idWorld
