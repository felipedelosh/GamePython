"""
FelipedelosH
2025

Input Key EXCUTOR Controller
"""
from src.core.gameLoger import GameLogger
from src.commands.movementCommands import (
    MoveUpCommand, MoveDownCommand, MoveLeftCommand, MoveRightCommand,
    StopMoveUpCommand, StopMoveDownCommand, StopMoveLeftCommand, StopMoveRightCommand
)
# from src.commands.actionCommands import JumpCommand, AttackCommand

class InputHandler:
    def __init__(self, palyer, controlFromConfig, gameStateManager, controller):
        self.logger = GameLogger.get_instance()
        self.player = palyer
        self.control = controlFromConfig
        self.gameStateManager = gameStateManager
        self.controller = controller

        self.press_commands = {
            self.control.key_UP: MoveUpCommand(),
            self.control.key_DOWN: MoveDownCommand(),
            self.control.key_LEFT: MoveLeftCommand(),
            self.control.key_RIGTH: MoveRightCommand(),
            # self.control.key_A: JumpCommand(),
            # self.control.key_B: AttackCommand(),
        }

        self.release_commands = {
            self.control.key_UP: StopMoveUpCommand(),
            self.control.key_DOWN: StopMoveDownCommand(),
            self.control.key_LEFT: StopMoveLeftCommand(),
            self.control.key_RIGTH: StopMoveRightCommand(),
        }


    def handleKeypress(self, keycode):
        _pivot = self.gameStateManager.getStateMachine("game").pointer
        self.logger.info(f"INPUTHANDLER::KEYPRESS::{keycode}")
        self.logger.info(f"INPUTHANDLER::CURRENT_STATE_MACHINE_PIVOT::{_pivot}")
        if _pivot == "gameStart":
            command = self.press_commands.get(keycode)
            if command:
                command.execute(self.player)
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
                self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
            if keycode == self.control.key_L:
                print("L")
            if keycode == self.control.key_R:
                print("R")

        elif _pivot == "gamePause":
            if keycode == self.control.key_A:
                current_option = self.gameStateManager.getStateMachine("pause").pointer

                # if current_option == "continue": # WIP: ADD logic
                #     self.controller.current_state.current_pause_menu_option_selected = "main"
                #     self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
                    

                self.controller.current_state.current_pause_menu_option_selected = current_option
            if keycode == self.control.key_A:
                current_option = self.gameStateManager.getStateMachine("pause").pointer
                self.controller.current_state.current_pause_menu_option_selected = current_option
            if keycode == self.control.key_UP:
                self.gameStateManager.getStateMachine("pause").mouvePointer(self.control.key_UP)
            if keycode == self.control.key_DOWN:
                self.gameStateManager.getStateMachine("pause").mouvePointer(self.control.key_DOWN)
            if keycode == self.control.key_START:
                self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
            
        elif _pivot == "mainMenu":
            if keycode == self.control.key_UP:
                self.gameStateManager.getStateMachine("mainMenu").mouvePointer(self.control.key_UP)
            if keycode == self.control.key_DOWN:
                self.gameStateManager.getStateMachine("mainMenu").mouvePointer(self.control.key_DOWN)
            if keycode == self.control.key_START:
                self.gameStateManager.getStateMachine("game").mouvePointer("gameStart")


    def handleKeyRelease(self, keycode):
        self.logger.info(f"INPUTHANDLER::KEYRELEASE::{keycode}")
        _pivot = self.gameStateManager.getStateMachine("game").pointer
        if _pivot == "gameStart":
            command = self.release_commands.get(keycode)
            if command:
                command.execute(self.player)
