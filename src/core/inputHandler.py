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
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::{keycode}")
                command.execute(self.player)
                self.gameStateManager.getStateMachine("animatedEntity").mouvePointer(str(keycode))
                self.player.updateAnimationStateMachineComponent(self.gameStateManager.getStateMachine("animatedEntity").pointer)

            if keycode == self.control.key_B:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::B::{keycode}")
            if keycode == self.control.key_A:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::A::{keycode}")
            if keycode == self.control.key_Y:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::Y::{keycode}")
            if keycode == self.control.key_X:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::X::{keycode}")
            if keycode == self.control.key_SELECT:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::SELECT::{keycode}")
            if keycode == self.control.key_START:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::START::{keycode}")
                self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
            if keycode == self.control.key_L:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::L::{keycode}")
                # WIP >> ONLY FOR TEST...
                self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_L)
                # DELETE THEM
            if keycode == self.control.key_R:
                self.logger.info(f"INPUTHANDLER::GAME_START::EXECUTE::R::{keycode}")

        elif _pivot == "gameTextDisplayed":
            if keycode == self.control.key_START:
                self.logger.info(f"INPUTHANDLER::GAME_DISPLAY_TEXT::EXECUTE::START::{keycode}")
                self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
            if keycode == self.control.key_A:
                self.logger.info(f"INPUTHANDLER::GAME_DISPLAY_TEXT::EXECUTE::A::{keycode}")
                self.controller._text_paginator_next_page()
            if keycode == self.control.key_DOWN:
                self.logger.info(f"INPUTHANDLER::GAME_DISPLAY_TEXT::EXECUTE::A::{keycode}")
                self.controller._text_paginator_next_page()


        elif _pivot == "gamePause":
            current_option = self.gameStateManager.getStateMachine("pause").pointer
            if self.controller.current_state.current_pause_menu_option_selected == "main":
                if keycode == self.control.key_A:
                    # if current_option == "continue": # WIP: ADD logic
                    #     self.controller.current_state.current_pause_menu_option_selected = "main"
                    #     self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
                        
                    self.controller.current_state.current_pause_menu_option_selected = current_option
                if keycode == self.control.key_UP:
                    self.gameStateManager.getStateMachine("pause").mouvePointer(self.control.key_UP)
                if keycode == self.control.key_DOWN:
                    self.gameStateManager.getStateMachine("pause").mouvePointer(self.control.key_DOWN)
                if keycode == self.control.key_START:
                    self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
            else:
                if keycode == self.control.key_Y:
                    self.controller.current_state.current_pause_menu_option_selected = "main"
                if keycode == self.control.key_START:
                    self.controller.current_state.current_pause_menu_option_selected = "main"
                    self.gameStateManager.getStateMachine("game").mouvePointer(self.control.key_START)
            
        elif _pivot == "mainMenu":
            if keycode == self.control.key_UP:
                self.gameStateManager.getStateMachine("mainMenu").mouvePointer(self.control.key_UP)
            if keycode == self.control.key_DOWN:
                self.gameStateManager.getStateMachine("mainMenu").mouvePointer(self.control.key_DOWN)
            if keycode == self.control.key_START and self.gameStateManager.getStateMachine("mainMenu").pointer != "exitGame":
                self.gameStateManager.getStateMachine("game").mouvePointer("gameStart")
            if keycode == self.control.key_START and self.gameStateManager.getStateMachine("mainMenu").pointer == "exitGame":
                self.controller._exitGame("mainMenu")

    def handleKeyRelease(self, keycode):
        self.logger.info(f"INPUTHANDLER::KEYRELEASE::{keycode}")
        _pivot = self.gameStateManager.getStateMachine("game").pointer
        if _pivot == "gameStart":
            command = self.release_commands.get(keycode)
            if command:
                command.execute(self.player)
