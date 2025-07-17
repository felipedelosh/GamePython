"""
FelipedelosH
This is the main controller to my videogame

"""
from tkinter import *
from tkinter import PhotoImage
from control import Control
from player import *
from stateMachine import *
from time import sleep
import sys


class Controller:
    def __init__(self) -> None:
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
        self.menuOptionsSM = StateMachine()
        self._initStateMachineOptionsMenu()
        self.player = Player()
        self._setPlayer()

        # Game resources:
        self.imgIntro =  PhotoImage(file="resources/images/intro.gif")


    def _initStateMachineGame(self):
        self.SMgame.addNode("intro")
        self.SMgame.addNode("mainMenu")
        self.SMgame.addNode("gameStart")
        self.SMgame.addNode("gamePause")
        self.SMgame.addNode("gameOptions")
        self.SMgame.addConection("intro", "mainMenu", "t")
        self.SMgame.addConection("mainMenu", "gameStart", "gameStart")
        self.SMgame.addConection("mainMenu", "gameOptions", "gameOptions")
        self.SMgame.addConection("gameOptions", "mainMenu", "mainMenu")


        self.SMgame.setInitialPointer("intro")
        # To game Running
        for i in self.control.direction_buttons: 
            self.SMgame.addConection("gameStart", "gameStart", i)
        for i in self.control.action_buttons:
            self.SMgame.addConection("gameStart", "gameStart", i)
        self.SMgame.addConection("mainMenu", "gameOptions", self.control.key_SELECT)
        self.SMgame.addConection("gameOptions", "mainMenu", self.control.key_B)
        self.SMgame.addConection("gameStart", "gamePause", self.control.key_START)
        self.SMgame.addConection("gamePause", "gameStart", self.control.key_START)
        self.SMgame.addConection("gameStart", "gameOptions", self.control.key_SELECT)
        self.SMgame.addConection("gameOptions", "gameStart", self.control.key_SELECT)
        self.SMgame.addConection("gamePause", "gameOptions", self.control.key_SELECT)
        self.SMgame.addConection("gameOptions", "gamePause", self.control.key_START)       

    def _initStateMachineMainMenuGame(self):
        # to options Main Menu
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

    def _initStateMachineOptionsMenu(self):
        self.menuOptionsSM.addNode("mobile")
        self.menuOptionsSM.addNode("items")
        self.menuOptionsSM.addNode("clock")
        self.menuOptionsSM.addNode("save")
        self.menuOptionsSM.addNode("load")
        self.menuOptionsSM.addNode("matrix")
        self.menuOptionsSM.setInitialPointer("mobile")
        self.menuOptionsSM.addConection("mobile","items",self.control.key_DOWN)
        self.menuOptionsSM.addConection("mobile","matrix",self.control.key_UP)
        self.menuOptionsSM.addConection("items","clock",self.control.key_DOWN)
        self.menuOptionsSM.addConection("items","mobile",self.control.key_UP)
        self.menuOptionsSM.addConection("clock","save",self.control.key_DOWN)
        self.menuOptionsSM.addConection("clock","items",self.control.key_UP)
        self.menuOptionsSM.addConection("save","load",self.control.key_DOWN)
        self.menuOptionsSM.addConection("save","clock",self.control.key_UP)
        self.menuOptionsSM.addConection("load","save",self.control.key_UP)
        self.menuOptionsSM.addConection("exit","matrix",self.control.key_DOWN)
        self.menuOptionsSM.addConection("matrix","mobile",self.control.key_DOWN)


    def keyPressed(self, keycode):
        if self.SMgame.pointer == "gameStart":
            if str(keycode) == self.control.key_UP:
                #print("Arriba")
                self.player.player_mouve_up()
            if str(keycode) == self.control.key_RIGTH:
                #print("Derecha")
                self.player.player_mouve_rigth()
            if str(keycode) == self.control.key_DOWN:
                #print("Abajo")
                self.player.player_mouve_down()
            if str(keycode) == self.control.key_LEFT:
                #print("Izquierda")
                self.player.player_mouve_left()    
            if str(keycode) == self.control.key_B:
                print("B")
            if str(keycode) == self.control.key_A:
                print("A")
            if str(keycode) == self.control.key_Y:
                print("Y")
            if str(keycode) == self.control.key_X:
                print("X")
            if str(keycode) == self.control.key_SELECT:
                self.SMgame.mouvePointer()
            if str(keycode) == self.control.key_START:
                print("Start")
            if str(keycode) == self.control.key_L:
                print("L")
            if str(keycode) == self.control.key_R:
                print("R")

        if self.SMgame.pointer == "mainMenu":
            if str(keycode) == self.control.key_UP:
                self.mainMenuSM.mouvePointer(self.control.key_UP)
            if str(keycode) == self.control.key_RIGTH:
                self.executeGameConfig()
            if str(keycode) == self.control.key_DOWN:
                self.mainMenuSM.mouvePointer(self.control.key_DOWN)
            if str(keycode) == self.control.key_LEFT:
                self.mainMenuSM.mouvePointer(self.control.key_LEFT)
            if str(keycode) == self.control.key_START:
                self.executeGameConfig()

        if self.SMgame.pointer == "gameOptions":
            if str(keycode) == self.control.key_UP:
                self.menuOptionsSM.mouvePointer(self.control.key_UP)

            if str(keycode) == self.control.key_DOWN:
                self.menuOptionsSM.mouvePointer(self.control.key_DOWN)
            
            if str(keycode) == self.control.key_START:
                self.executeOptionConfig()

            if str(keycode) == self.control.key_A:
                self.executeOptionConfig()

            if str(keycode) == self.control.key_B:
                self.SMgame.mouvePointer(self.control.key_B)



    def executeGameConfig(self):
        """
        Execute a option of self.mainMenuSM
        """
       
        if self.mainMenuSM.pointer == "newGame":
            self.SMgame.mouvePointer("gameStart")

        if self.mainMenuSM.pointer == "continueGame":
            print("Hay partida guardata?")

        if self.mainMenuSM.pointer == "optionsGame":     
            self.SMgame.mouvePointer("gameOptions")

        if self.mainMenuSM.pointer == "exitGame":  
            sys.exit()

    def executeOptionConfig(self):
        if self.menuOptionsSM.pointer == "mobile":
            print("Celular Ring")
        if self.menuOptionsSM.pointer == "items":
            print("Cosas estas y aquellas")
        if self.menuOptionsSM.pointer == "clock":
            print("La hora es")
        if self.menuOptionsSM.pointer == "save":
            print("Guardar juego")
        if self.menuOptionsSM.pointer == "load":
            print("Cargar juego")
        if self.menuOptionsSM.pointer == "matrix":
            print("Matrix")
            

    def loadLanguage(self, language="ESP"):
        try:
            f = open('resources/LAN/'+language+"/game.txt", 'r')
            for i in f.read().split("\n"):
                if str(i).strip() != "":
                    info = i.split("=")
                    self.language[str(info[0])]=str(info[1])
        except:
            self.setLanguageDefault()

    def loadConfiguration(self):
        try:
            f = open('resources/config.txt', 'r')
            for i in f.read().split("\n"):
                if str(i).strip() != "":
                    info = i.split("=")
                    self.configuration[str(info[0])]=str(info[1])
        except:
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
        self._setConfigDefaultOptionsController()  
    
    def _setConfigDefaultOptionsController(self):
        self.configuration["key_U"]="38"
        self.configuration["key_RIGTH"]="39"
        self.configuration["key_DOWN"]="40"
        self.configuration["key_LEFT"]="37"
        self.configuration["key_SELECT"]="32"
        self.configuration["key_START"]="13"
        self.configuration["key_B"]="90"
        self.configuration["key_A"]="88"
        self.configuration["key_Y"]="67"
        self.configuration["key_X"]="86"
        self.configuration["key_L"]="65"
        self.configuration["key_R"]="83"


    def setLanguageDefault(self):
        self.language["gameTitle"]="LokoGame"

    def showIntro(self, canvas):
        try:
            _x = int(canvas['width'])*0.35
        except:
            _x = 200


        
        canvas.create_image(_x,20,image=self.imgIntro, anchor=NW, tag="intro")
        self.SMgame.mouvePointer("t")
        

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
        self.paintPlayer(canvas)

    def showOptions(self, canvas):
        try:
            _x = int(canvas['width'])*0.8
            _y = int(canvas['height'])*0.3
        except:
            _x = 200
            _y = 200

        _y0 = _y + (len(self.menuOptionsSM.node)*25)
        self._deleteCanvasNotGameItems(canvas)
        canvas.create_rectangle(_x*0.9, _y*0.6, _x*1.1, _y*0.85, fill="snow",tag="optionsGame")
        canvas.create_rectangle(_x*0.9, _y*0.9, _x*1.1, _y0, fill="snow",tag="optionsGame")
    

        count = 0
        self.itemPosition = {} # Save x, y of [item]
        for i in self.menuOptionsSM.node:
            if i not in self.itemPosition.keys():
                self.itemPosition[i] = [_x+30, _y+(count*25)]
            canvas.create_text(_x*0.98, _y+(count*25), text=str(i).upper(), tag="optionsGame")
            count = count + 1

        pointer_x0 = _x*0.9
        pointer_y0 = self.itemPosition[self.menuOptionsSM.pointer][1]*0.99
        pointer_x1 = _x*1.1
        pointer_y1 = self.itemPosition[self.menuOptionsSM.pointer][1]*1.01

        canvas.create_rectangle(pointer_x0,pointer_y0,pointer_x1,pointer_y1, fill="red", tag="optionsGame")
        canvas.create_text(_x*1.05, _y*0.7, text=str(self.menuOptionsSM.pointer).upper(), tag="optionsGame")


    def _deleteCanvasNotGameItems(self, canvas):
        canvas.delete("intro")
        canvas.delete("mainMenu")
        canvas.delete("optionsGame")

        

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

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
