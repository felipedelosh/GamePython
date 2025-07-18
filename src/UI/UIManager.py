"""
FelipedelosH
2025
"""
from src.UI.IUIRenderer import IUIRenderer

class UIManager:
    def __init__(self, renderer: IUIRenderer):
        self.renderer = renderer
        self.imgIntro = None

    def set_intro_image(self, image):
        self.imgIntro = image

    def showIntro(self):
        try:
            _x = int(self.renderer.canvas['width'])*0.2
        except:
            _x = 200
            
        self.renderer.render_image(self.imgIntro, _x, 20, anchor="nw", tag="intro")

    def showMainMenu(self):
        pass

    def showGame(self):
        pass
