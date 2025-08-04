"""
FelipedelosH

Main states of game.
Intro, GamePlay, Exit
"""
from abc import ABC, abstractmethod

class GameState(ABC):
    def __init__(self, controller):
        self.controller = controller
    
    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def render(self):
        pass

class IntroState(GameState):
    def enter(self):
        self.controller.intro_shown_time = 0
        
    def update(self):
        self.controller.intro_shown_time = self.controller.intro_shown_time + self.controller.FPS
        if self.controller.intro_shown_time >= self.controller.config.get("intro_duration"):
            self.controller.SMgame.mouvePointer("t")
            
    def render(self):
        self.controller.UImanager.showIntro()
        
    def exit(self):
        pass


class MainMenuState(GameState):
    def enter(self):
        pass
        
    def update(self):
        pass
        
    def render(self):
        self.controller.UImanager.showMainMenu()
        
    def exit(self):
        pass


class GameState(GameState):
    def enter(self):
        pass
        
    def update(self):
        pass
        
    def render(self):
        self.controller.UImanager.showGame()
        
    def exit(self):
        pass

class GamePauseState:
    def __init__(self, controller):
        self.controller = controller

    def enter(self):
        pass

    def update(self):
        pass

    def render(self):
        self.controller.UImanager.showPauseGame()

    def exit(self):
        pass
        

class GameOptionsState(GameState):
    def enter(self):
        pass
        
    def update(self):
        pass
        
    def render(self):
        pass
        
    def exit(self):
        pass
