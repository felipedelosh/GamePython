"""
FelipedelosH
2025
"""
from tkinter import *
from src.core.controller import Controller

class Software:
    def __init__(self) -> None:
        self.display = Tk()
        self.canvas = Canvas(self.display, highlightthickness=0, bd=0)
        self.canvas.bind_all("<KeyPress>", self.keyPressed)
        self.canvas.bind_all("<KeyRelease>", self.keyReleased)
        self.controller = Controller(self.canvas)

        self.showDisplay()


    def showDisplay(self):
        _title = f"{self.controller.config.get("gameTitle")} v{self.controller.config.get("version")}"
        self.display.title(_title)
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


    def keyReleased(self, Event):
        if Event.keycode in self.controller.control.keyResult:
            self.controller.keyReleased(Event.keycode)


s = Software()
