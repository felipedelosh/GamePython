"""
FelipedelosH
This is my first MotorVideoGame
"""
from tkinter import *
from src.core.controller import *

class Software:
    def __init__(self) -> None:
        self.display = Tk()
        self.canvas = Canvas(self.display)
        self.canvas.bind_all("<Key>", self.keyPressed)
        self.controller = Controller(self.canvas)

        self.VizualizedAndRun()


    def VizualizedAndRun(self):
        self.display.title(self.controller.config.get("gameTitle"))
        self.display.geometry(f"{self.controller.config.get("displayW")}x{self.controller.config.get("displayH")}")
        self.canvas['height']=int(self.controller.config.get("displayH"))
        self.canvas['width']=int(self.controller.config.get("displayW"))
        self.canvas.place(x=0, y=0)
        
        self.display.resizable(0,0)
        self.display.after(0, self.refreshGame)
        self.display.mainloop()


    def refreshGame(self):
        if self.controller.SMgame.pointer == "intro":
            self.controller.intro_shown_time = self.controller.intro_shown_time + self.controller.FPS
            if self.controller.intro_shown_time >= self.controller.config.get("intro_duration"):
                self.controller.SMgame.mouvePointer("t")
            self.controller.showIntro()

        if self.controller.SMgame.pointer == "mainMenu":
            self.controller.showMainMenu()

        if self.controller.SMgame.pointer == "gameStart":
            self.controller.showGame()
        
        if self.controller.SMgame.pointer == "gameOptions":
            pass

        self.display.after(self.controller.FPS, self.refreshGame)


    def keyPressed(self, Event):
        if Event.keycode in self.controller.control.keyResult:
            self.controller.keyPressed(Event.keycode)


s = Software()
