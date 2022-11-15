"""
FelipedelosH
This is my first MotorVideoGame
"""
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self.display = Tk()
        self.canvas = Canvas(self.display, bg="snow")
        self.canvas.bind_all("<Key>", self.keyPressed)


        self.controller = Controller()
        self.controller.gameCanvas = self.canvas


        self.VizualizedAndRun()


    def VizualizedAndRun(self):
        self.display.title(self.controller.language["gameTitle"])
        self.display.geometry(self.controller.configuration["displayW"]+"x"+self.controller.configuration["displayH"])
        self.canvas['height']=int(self.controller.configuration["displayH"])
        self.canvas['width']=int(self.controller.configuration["displayW"])
        self.canvas.place(x=0, y=0)
        
        self.display.resizable(0,0)
        self.display.after(0, self.refreshGame)
        self.display.mainloop()

    def refreshGame(self):
        
        if self.controller.SMgame.pointer == "intro":
            self.controller.showIntro(self.canvas)

        if self.controller.SMgame.pointer == "mainMenu":
            self.controller.showMainMenu(self.canvas)

        if self.controller.SMgame.pointer == "gameStart":
            self.controller.showGame(self.canvas)
        
        if self.controller.SMgame.pointer == "gameOptions":
            pass

        
        
        self.display.after(self.controller.getFPS(), self.refreshGame)


    def keyPressed(self, Event):
        if str(Event.keycode) in self.controller.control.keyResult:
            self.controller.keyPressed(Event.keycode)


s = Software()