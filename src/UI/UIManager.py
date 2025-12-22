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

    def showAdvisory(self):
        self.renderer.render_game_advisory()

    def showMainMenu(self):
        self.renderer.render_game_main_menu()

    def showGame(self):
        self.renderer._delete_no_game_items()
        self.renderer.render_floor()
        self.renderer.render_player()

    def showGameTextDisplayed(self):
        self.renderer.render_game_text_displayed()

    def showPauseGame(self):
        self.renderer.render_game_pause()

    def render_game_pause_player_menu(self):
        self.renderer.render_game_pause_player_menu()
