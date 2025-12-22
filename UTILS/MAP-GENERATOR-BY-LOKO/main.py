"""
FelipedelosH
TOOL to generate a wold using image
"""
from tkinter import *
from tkinter import ttk
from controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Generate a MAP using IMAGE")
        self.lblIntroLoadImage = Label(self.canvas, text="Select image FILE: ")
        self.cmbxOptionsImagesToConvert = ttk.Combobox(self.screem, values=self.controller.dataToConverArray)
        self.cmbxOptionsImagesToConvert.current(0)
        self.btnConvert = Button(self.screem, text="CONVERT", command=self.convert)
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")
        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("Loko-MAP-GENERATOR")
        self.screem.geometry("720x480")
        self.canvas['width'] = 720
        self.canvas['height'] = 480
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=20, y=20)
        self.lblIntroLoadImage.place(x=20, y=60)
        self.cmbxOptionsImagesToConvert.place(x=140, y=60)
        self.lblFooterProgram.place(x=200, y=450)
        self.btnConvert.place(x=310, y=58)
        self.btnConvert['bg'] = 'white'
        self.screem.mainloop()


    def convert(self):
        if self.controller._convert(self.cmbxOptionsImagesToConvert.get()):
            self.btnConvert['bg'] = 'green'
        else:
            self.btnConvert['bg'] = 'red'


s = Software()
