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
        self.renderer.render_game_intro(self.imgIntro)

    def showMainMenu(self):
        self.renderer.render_game_main_menu(self.gameStateManager)

    def showGame(self):
        self.renderer.delete_no_game_items()
        self.renderer.render_floor()
        self.renderer.render_player()

    def showPauseGame(self):
        self.renderer.render_game_pause()
