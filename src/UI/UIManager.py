"""
FelipedelosH
2025

Render Scenes and draw elements.
"""
from src.UI.IUIRenderer import IUIRenderer

class UIManager:
    def __init__(self, renderer: IUIRenderer):
        self.renderer = renderer
        self.imgIntro = None
        self.gameStateManager = None

    def set_intro_image(self, image):
        self.imgIntro = image

    def set_game_state_manager(self, gameStateManager):
        self.gameStateManager = gameStateManager


    def showIntro(self):
        try:
            _x = int(self.renderer.canvas['width'])*0.2
        except:
            _x = 200
            
        self.renderer.render_image(self.imgIntro, _x, 20, anchor="nw", tag="intro")


    def showMainMenu(self):
        try:
            _x = int(self.renderer.canvas['width']) * 0.5
            _y = int(self.renderer.canvas['height']) * 0.5
            _text = self.gameStateManager.getStateMachine("mainMenu").pointer
        except:
            _x = 200
            _y = 200
            _text = "ERROR"

        
        self.renderer.delete_no_game_items()
        self.renderer.render_line(_x, _y-5, _x, _y-35, fill="red", arrow="last", tag="mainMenu")
        self.renderer.render_line(_x, _y+15, _x, _y+35, fill="red", arrow="last", tag="mainMenu")
        self.renderer.render_rectangle(_x-50, _y-20, _x+50, _y+20, fill="snow",tag="mainMenu")
        self.renderer.render_text(_x, _y, text=_text, tag="mainMenu")


    def showGame(self):
        self.renderer.delete_no_game_items()
        self.renderer.render_floor()
        self.renderer.render_player()

    def showPauseGame(self):
        self.renderer.render_game_pause()
