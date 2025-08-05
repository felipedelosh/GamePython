"""
FelipedelosH
2025

Render Scenes and draw elements.
"""
from src.UI.IUIRenderer import IUIRenderer

class UIManager:
    def __init__(self, renderer: IUIRenderer):
        self.renderer = renderer

    def showIntro(self):
        self.renderer.render_game_intro()

    def showMainMenu(self):
        self.renderer.render_game_main_menu()

    def showGame(self):
        self.renderer.delete_no_game_items()
        self.renderer.render_floor()
        self.renderer.render_player()

    def showPauseGame(self):
        self.renderer.render_game_pause()
