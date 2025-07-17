"""
FelipedelosH
This is the main controller to my videogame

"""
import json
from tkinter import *
from tkinter import PhotoImage
from src.core.inputHandler import InputHandler
from src.core.gameStateManager import GameStateManager
from src.core.control import Control
from src.core.player import *
from src.core.stateMachine import *
from src.core.world import *
from time import sleep


class Controller:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.configuration = {} # game configuration
        self.loadConfiguration()
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
        self.SMgame = StateMachine()
        self._initStateMachineGame()
        self.mainMenuSM = StateMachine()
        self._initStateMachineMainMenuGame()
        self.player = Player()
        self._setPlayer()
        self.world = World()

        # -------------------------------
        self.inputHandler = InputHandler(self.player, self.control, self.mainMenuSM, self.SMgame)
        self.gameStateManager = GameStateManager
        # -------------------------------


        # VARS
        self.intro_shown_time = 0
        self.IdTempWorldToPaint = ""
        

        # Game resources:
        self.imgIntro =  PhotoImage(file="assets/images/intro.gif")


    def _initStateMachineGame(self):
        self.SMgame.addNode("intro")
        self.SMgame.addNode("mainMenu")
        self.SMgame.addNode("gameStart")
        self.SMgame.addNode("gamePause")
        self.SMgame.addNode("gameOptions")
        self.SMgame.addConection("intro", "mainMenu", "t")
        self.SMgame.addConection("mainMenu", "gameStart", "gameStart")



        self.SMgame.setInitialPointer("intro")
        # To game Running
        for i in self.control.direction_buttons: 
            self.SMgame.addConection("gameStart", "gameStart", i)
        for i in self.control.action_buttons:
            self.SMgame.addConection("gameStart", "gameStart", i)
        self.SMgame.addConection("gameStart", "gamePause", self.control.key_START)
        self.SMgame.addConection("gamePause", "gameStart", self.control.key_START)
        self.SMgame.addConection("gameStart", "gameOptions", self.control.key_SELECT)
        self.SMgame.addConection("gameOptions", "gameStart", self.control.key_SELECT)
        self.SMgame.addConection("gamePause", "gameOptions", self.control.key_SELECT)
        self.SMgame.addConection("gameOptions", "gamePause", self.control.key_START)       

    def _initStateMachineMainMenuGame(self):
        self.mainMenuSM.addNode("newGame")
        self.mainMenuSM.addNode("continueGame")
        self.mainMenuSM.addNode("optionsGame")
        self.mainMenuSM.addNode("exitGame")
        self.mainMenuSM.setInitialPointer("newGame")
        self.mainMenuSM.addConection("newGame", "continueGame", self.control.key_DOWN)
        self.mainMenuSM.addConection("continueGame", "newGame", self.control.key_UP)
        self.mainMenuSM.addConection("continueGame", "optionsGame", self.control.key_DOWN)
        self.mainMenuSM.addConection("optionsGame", "continueGame", self.control.key_UP)
        self.mainMenuSM.addConection("optionsGame", "exitGame", self.control.key_DOWN)
        self.mainMenuSM.addConection("exitGame", "optionsGame", self.control.key_UP)
        self.mainMenuSM.addConection("exitGame", "newGame", self.control.key_DOWN)
        self.mainMenuSM.addConection("newGame", "exitGame", self.control.key_UP)

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
        except FileNotFoundError:
            print("¡Archivo config.json no encontrado! Usando configuración por defecto.")
            self.setConfigDefaultOptions()
        except json.JSONDecodeError:
            print("¡Error en el formato del JSON! Usando configuración por defecto.")
            self.setConfigDefaultOptions()

    def getFPS(self):
        return int(1000/int(self.configuration["FPS"]))

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

    def showIntro(self, canvas):
        try:
            _x = int(canvas['width'])*0.2
        except:
            _x = 200

        canvas.create_image(_x,20,image=self.imgIntro, anchor=NW, tag="intro")
        

    def showMainMenu(self, canvas):
        try:
            _x = int(canvas['width'])*0.5
            _y = int(canvas['height'])*0.5
        except:
            _x = 200
            _y = 200
        
        self._deleteCanvasNotGameItems(canvas)
        canvas.create_line(_x, _y-5, _x, _y-35, fill="red", arrow=LAST, tag="mainMenu")
        canvas.create_line(_x, _y+15, _x, _y+35, fill="red", arrow=LAST, tag="mainMenu")
        canvas.create_rectangle(_x-50, _y-20, _x+50, _y+20, fill="snow",tag="mainMenu")
        canvas.create_text(_x, _y, text=self.mainMenuSM.pointer, tag="mainMenu")

    def showGame(self, canvas):
        self._deleteCanvasNotGameItems(canvas)
        self._paintMatrix(canvas)
        self.paintPlayer(canvas)
        

    def _deleteCanvasNotGameItems(self, canvas):
        canvas.delete("intro")
        canvas.delete("mainMenu")

        

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
