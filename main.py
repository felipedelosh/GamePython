"""
FelipedelosH
This is my first MotorVideoGame
"""
from tkinter import *
from src.core.controller import Controller

class Software:
    def __init__(self) -> None:
        self.display = Tk()
        self.canvas = Canvas(self.display)
        self.canvas.bind_all("<Key>", self.keyPressed)
        self.controller = Controller(self.canvas)

        self.showDisplay()


    def showDisplay(self):
        self.display.title(self.controller.config.get("gameTitle"))
        self.display.geometry(f"{self.controller.config.get("displayW")}x{self.controller.config.get("displayH")}")
        self.canvas['height']=int(self.controller.config.get("displayH"))
        self.canvas['width']=int(self.controller.config.get("displayW"))
        self.canvas.place(x=0, y=0)
        
        self.display.resizable(0,0)
        self.display.after(0, self.refreshGame)
        self.display.mainloop()


    def refreshGame(self):
        self.controller.update()
        self.controller.render()
        self.display.after(self.controller.FPS, self.refreshGame)


    def keyPressed(self, Event):
        if Event.keycode in self.controller.control.keyResult:
            self.controller.keyPressed(Event.keycode)


s = Software()
