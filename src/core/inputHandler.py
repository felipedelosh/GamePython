"""
FelipedelosH
2025

Input Key EXCUTOR Controller
"""
from src.core.gameLoger import GameLogger

class InputHandler:
    def __init__(self, palyer, config, stateMachineMainMenu, stateMachineGame):
        self.logger = GameLogger.get_instance()
        self.player = palyer
        self.control = config
        self.stateMachineMainMenu = stateMachineMainMenu
        self.stateMachineGame = stateMachineGame


    def handleKeypress(self, keycode):
        self.logger.info(f"KEY PRESSED: {keycode}")
        if self.stateMachineGame.pointer == "gameStart":
            if keycode == self.control.key_UP:
                self.player.player_mouve_up()
            if keycode == self.control.key_RIGTH:
                self.player.player_mouve_rigth()
            if keycode == self.control.key_DOWN:
                self.player.player_mouve_down()
            if keycode == self.control.key_LEFT:
                self.player.player_mouve_left()    
            if keycode == self.control.key_B:
                print("B")
            if keycode == self.control.key_A:
                print("A")
            if keycode == self.control.key_Y:
                print("Y")
            if keycode == self.control.key_X:
                print("X")
            if keycode == self.control.key_SELECT:
                print("Select")
            if keycode == self.control.key_START:
                print("Start")
            if keycode == self.control.key_L:
                print("L")
            if keycode == self.control.key_R:
                print("R")


        if self.stateMachineGame.pointer == "mainMenu":
            if keycode == self.control.key_UP:
                self.stateMachineMainMenu.mouvePointer(self.control.key_UP)
            if keycode == self.control.key_DOWN:
                self.stateMachineMainMenu.mouvePointer(self.control.key_DOWN)
            if keycode == self.control.key_START:
                self.stateMachineGame.mouvePointer("gameStart")
