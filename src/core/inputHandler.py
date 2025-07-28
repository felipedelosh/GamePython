"""
FelipedelosH
2025

Input Key EXCUTOR Controller
"""
from src.core.gameLoger import GameLogger
from src.ecs.components import DirectionComponent

class InputHandler:
    def __init__(self, palyer, config, stateMachineMainMenu, stateMachineGame):
        self.logger = GameLogger.get_instance()
        self.player = palyer
        self.control = config
        self.stateMachineMainMenu = stateMachineMainMenu
        self.stateMachineGame = stateMachineGame


    def handleKeypress(self, keycode):
        self.logger.info(f"INPUTHANDLER::KEYPRESS::{keycode}")
        if self.stateMachineGame.pointer == "gameStart":
            direction = self.player.get_component(DirectionComponent)
            if keycode == self.control.key_UP:
                direction.current_directions.add("up")
            elif keycode == self.control.key_RIGTH:
                direction.current_directions.add("right")
            elif keycode == self.control.key_DOWN:
                direction.current_directions.add("down")
            elif keycode == self.control.key_LEFT:
                direction.current_directions.add("left")  
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


        elif self.stateMachineGame.pointer == "mainMenu":
            if keycode == self.control.key_UP:
                self.stateMachineMainMenu.mouvePointer(self.control.key_UP)
            if keycode == self.control.key_DOWN:
                self.stateMachineMainMenu.mouvePointer(self.control.key_DOWN)
            if keycode == self.control.key_START:
                self.stateMachineGame.mouvePointer("gameStart")


    def handleKeyRelease(self, keycode):
        self.logger.info(f"INPUTHANDLER::KEYRELEASE::{keycode}")
        if self.stateMachineGame.pointer == "gameStart":
            direction = self.player.get_component(DirectionComponent)
            if keycode == self.control.key_UP:
                direction.current_directions.discard("up")
            elif keycode == self.control.key_RIGTH:
                direction.current_directions.discard("right")
            elif keycode == self.control.key_DOWN:
                direction.current_directions.discard("down")
            elif keycode == self.control.key_LEFT:
                direction.current_directions.discard("left")

            if not direction.current_directions:
                direction.last_direction = direction.last_direction