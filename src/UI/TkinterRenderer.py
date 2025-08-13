"""
FelipedelosH
2025
"""
from src.UI.IUIRenderer import IUIRenderer
import tkinter as tk

from src.ecs.components import (
    IdentityComponent,
    HealthComponent,
    CurrencyComponent
)

class TkinterRenderer(IUIRenderer):
    def __init__(self, canvas: tk.Canvas, imgIntro, FPS, configuration, gameStateManager, player, world):
        self.canvas = canvas
        self.imgIntro = imgIntro
        self.FPS = FPS
        self.configuration = configuration
        self.gameStateManager = gameStateManager
        self.player = player
        self.identity = self.player.get_component(IdentityComponent)
        self.health = self.player.get_component(HealthComponent)
        self.currency = self.player.get_component(CurrencyComponent)
        self.world = world
        self.IdTempWorldToPaint = ""
        self.IdTempPlayerToPaint = ""
        self.currentSpriteDisplayed = 0
        self.animating = False
        self.animatingCounter = 0
        self.sprites = [
            (0, 0, 50, 100),
            (50, 0, 50, 100),
            (100, 0, 50, 100),
            (150, 0, 50, 100)
        ]
        # VARS
        self.gamePauseOptionsAndCoors = {}
        self._defineGamePauseMenuElements()
        self._defineGamePausePlayerMenuElements()

    def render_image(self, image, x, y, anchor="nw", tag=None):
        return self.canvas.create_image(x, y, image=image, anchor=anchor, tag=tag)

    def render_line(self, x1, y1, x2, y2, fill="black", arrow=None, tag=None):
        return self.canvas.create_line(x1, y1, x2, y2, fill=fill, arrow=arrow, tag=tag)

    def render_rectangle(self, x1, y1, x2, y2, fill="", tag=None):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, tag=tag)
    
    def render_circle(self, x, y, r, color, tag):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, tag=tag)

    def render_text(self, x, y, text, tag=None):
        return self.canvas.create_text(x, y, text=text, tag=tag)
    
    def render_progress_bar(self, x1, y1, x2, y2, percent, tag=""):
        _baseColor = "blue"
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=_baseColor, tag=tag)
        if percent < 0.5:
            _color = "red"
        elif percent >= 0.5:
             _color = "green"

        if percent == 0 or percent >= 1: 
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=_color, tag=tag)
        else:
            x2 = x2 * percent
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=_color, tag=tag)
        
    
    def render_player(self):
        # WIP: NEEDs Optimization
        if self.animatingCounter > 1000:
            self.animatingCounter = 0
            self.currentSpriteDisplayed = self.currentSpriteDisplayed + 1
            if self.currentSpriteDisplayed > 3:
                self.currentSpriteDisplayed = 0

        sprite_x, sprite_y, w, h = self.sprites[self.currentSpriteDisplayed]
        _player_img = self.player.getPlayerSprite()
        _x, _y = self.player.getSpriteRenderCoords()
        IdTempPlayerToPaint = f"{sprite_x}:{sprite_y}:{_player_img}"
        sprite_img = tk.PhotoImage()
        sprite_img.tk.call(sprite_img, 'copy', _player_img, '-from', sprite_x, sprite_y, sprite_x+w, sprite_y+h, '-to', 0, 0)
        if IdTempPlayerToPaint != self.IdTempWorldToPaint:
            self.IdTempPlayerToPaint = IdTempPlayerToPaint
            self._clear_by_tag("player")

        self.render_image(sprite_img, _x, _y, anchor="nw", tag="player")
        self.render_circle(self.player.x, self.player.y, 5, "green", "player")
        
        # Render
        if hasattr(self, '_last_sprite_img'):
            del self._last_sprite_img
        self._last_sprite_img = sprite_img # Dont KIll by Garbage Collector

        self.animatingCounter = self.animatingCounter + self.FPS

    def render_game_main_menu(self):
        try:
            _x = int(self.canvas['width']) * 0.5
            _y = int(self.canvas['height']) * 0.5
            _text = self.gameStateManager.getStateMachine("mainMenu").pointer
        except:
            _x = 200
            _y = 200
            _text = "ERROR"

        
        self._delete_no_game_items()
        self.render_line(_x, _y-5, _x, _y-35, fill="red", arrow="last", tag="mainMenu")
        self.render_line(_x, _y+15, _x, _y+35, fill="red", arrow="last", tag="mainMenu")
        self.render_rectangle(_x-50, _y-20, _x+50, _y+20, fill="snow",tag="mainMenu")
        self.render_text(_x, _y, text=_text, tag="mainMenu")

    def render_game_intro(self):
        try:
            _x = int(self.canvas['width']) * 0.2
        except:
            _x = 200
            
        self.render_image(self.imgIntro, _x, 20, anchor="nw", tag="intro")

    def render_game_pause(self):
        if self.gamePauseOptionsAndCoors["currentOption"] != self.gameStateManager.getStateMachine("pause").pointer:
            self.gamePauseOptionsAndCoors["currentOption"] = self.gameStateManager.getStateMachine("pause").pointer
            self._delete_no_game_items()
            self.render_rectangle(self.gamePauseOptionsAndCoors["menuCoords"][0],
                                self.gamePauseOptionsAndCoors["menuCoords"][1],
                                self.gamePauseOptionsAndCoors["menuCoords"][2],
                                self.gamePauseOptionsAndCoors["menuCoords"][3],
                                fill="snow",tag="gamePause")
            
            self.render_text(self.gamePauseOptionsAndCoors["menuCoords"][0]*1.25,
                             self.gamePauseOptionsAndCoors["menuCoords"][3]*0.05,
                             self.gamePauseOptionsAndCoors["title"],
                             tag="gamePause:title")
            
            for i in self.gamePauseOptionsAndCoors["itemsCoords"]:
                _x = self.gamePauseOptionsAndCoors["itemsCoords"][i][0]
                _y = self.gamePauseOptionsAndCoors["itemsCoords"][i][1]
                self.render_text(_x,_y,i,tag="gamePause:option")

            _x = self.gamePauseOptionsAndCoors["itemsCoords"][self.gamePauseOptionsAndCoors["currentOption"]][0] * 0.9
            _y = self.gamePauseOptionsAndCoors["itemsCoords"][self.gamePauseOptionsAndCoors["currentOption"]][1]
            self.render_circle(_x, _y, 10, "red", "gamePause:currentOption")
            
    def render_game_pause_player_menu(self): # WIP
        if self.gamePauseOptionsAndCoors["isUpdateInformationInPlayer"]:
            self._delete_no_game_items()
            self.render_rectangle(
                self.gamePauseOptionsAndCoors["playerPanelCoords"][0],
                self.gamePauseOptionsAndCoors["playerPanelCoords"][1],
                self.gamePauseOptionsAndCoors["playerPanelCoords"][2],
                self.gamePauseOptionsAndCoors["playerPanelCoords"][3],
                fill="snow",
                tag="gamePause:player"
            )
            self.render_text(self.gamePauseOptionsAndCoors["playerNameCoords"][0], self.gamePauseOptionsAndCoors["playerNameCoords"][1], self.gamePauseOptionsAndCoors["playerName"], tag="gamePause:player")
            self.render_rectangle(
                self.gamePauseOptionsAndCoors["playerAvatarCoords"][0],
                self.gamePauseOptionsAndCoors["playerAvatarCoords"][1],
                self.gamePauseOptionsAndCoors["playerAvatarCoords"][2],
                self.gamePauseOptionsAndCoors["playerAvatarCoords"][3],
                "blue",
                "gamePause:player"
            )
            self.render_text(self.gamePauseOptionsAndCoors["playerHPCoords"][0], self.gamePauseOptionsAndCoors["playerHPCoords"][1], f"HP: {self.health.hp}/{self.health.hp_max}", tag="gamePause:player")
            self.render_progress_bar(
                self.gamePauseOptionsAndCoors["playerHPProgressBarCoords"][0],
                self.gamePauseOptionsAndCoors["playerHPProgressBarCoords"][1],
                self.gamePauseOptionsAndCoors["playerHPProgressBarCoords"][2],
                self.gamePauseOptionsAndCoors["playerHPProgressBarCoords"][3],
                self.health.hp/self.health.hp_max,
                "gamePause:player"
            )
            self.render_text(self.gamePauseOptionsAndCoors["playerCurrencyCoords"][0], self.gamePauseOptionsAndCoors["playerCurrencyCoords"][1], f"{self.currency}", tag="gamePause:player")

            self.gamePauseOptionsAndCoors["isUpdateInformationInPlayer"] = False


    def render_floor(self):
        # WIP: currently only render collider
        if self.world.id != self.IdTempWorldToPaint:
            self._clear_by_tag("world")
            _x = float(self.configuration.get("displayW"))/self.world.w
            _y = float(self.configuration.get("displayH"))/self.world.h

            for i in range(0, self.world.h):
                for j in range(0, self.world.w):
                    _data = self.world.collider[i][j]
                    if _data:
                        self.canvas.create_rectangle(_x*j,_y*i,_x*(j+1),_y*(i+1), fill="black", tags="world")
                    else:
                        self.canvas.create_rectangle(_x*j,_y*i,_x*(j+1),_y*(i+1), fill="red", tags="world")

            self.IdTempWorldToPaint = self.world.id

    def _defineGamePauseMenuElements(self):
        try:
            _x = int(self.configuration.get("displayW"))
            _y = int(self.configuration.get("displayH"))
            self.gamePauseOptionsAndCoors["title"] = "Game Pause"
            self.gamePauseOptionsAndCoors["menuCoords"] = [_x * 0.65, 0, _x, _y]
            self.gamePauseOptionsAndCoors["items"] = [i for i in self.configuration.get("statesMachines")["pause"]["states"]]

            self.gamePauseOptionsAndCoors["itemsCoords"] = {}

            counter = 1
            _dy = (_y * 0.6) / len(self.gamePauseOptionsAndCoors["items"])
            for i in self.gamePauseOptionsAndCoors["items"]:
                self.gamePauseOptionsAndCoors["itemsCoords"][i] = [(_x * 0.82), ((_dy * counter) + (_y * 0.09))]
                counter = counter + 1

            self._reset_game_pause_menu()
        except:
            self.gamePauseOptionsAndCoors["title"] = "ERROR"
            self.gamePauseOptionsAndCoors["menuCoords"] = [320, 0, 480, 640]
            self.gamePauseOptionsAndCoors["items"] = ["ERROR"]


    def _defineGamePausePlayerMenuElements(self):
        try:
            _x = int(self.configuration.get("displayW"))
            _y = int(self.configuration.get("displayH"))
            self.gamePauseOptionsAndCoors["playerPanelCoords"] = [_x * 0.2, _y * 0.1, _x * 0.8, _y * 0.9]
            self.gamePauseOptionsAndCoors["playerName"] = f"{self.identity.first_name} {self.identity.second_name} {self.identity.family_name} {self.identity.second_family_name}"
            self.gamePauseOptionsAndCoors["playerNameCoords"] = [_x * 0.48, _y * 0.14]
            self.gamePauseOptionsAndCoors["playerAvatarCoords"] = [_x * 0.23, _y * 0.13, _x * 0.35, _y * 0.35]
            self.gamePauseOptionsAndCoors["playerHPCoords"] = [_x * 0.42, _y * 0.2]
            self.gamePauseOptionsAndCoors["playerHPProgressBarCoords"] = [_x * 0.49, _y * 0.19, _x * 0.76, _y * 0.21]
            self.gamePauseOptionsAndCoors["playerCurrencyCoords"] = [_x * 0.41, _y * 0.24]

            self._updates_game_pause_player_menu_info()
        except:
            self.gamePauseOptionsAndCoors["playerName"] = "ERROR"
            self.gamePauseOptionsAndCoors["playerPanelCoords"] = [128, 48, 512, 432]

    def _reset_game_pause_menu(self):
        self.gamePauseOptionsAndCoors["currentOption"] = ""

    def _updates_game_pause_player_menu_info(self):
        self.gamePauseOptionsAndCoors["isUpdateInformationInPlayer"] = True
    
    def _delete_no_game_items(self):
        self._clear_by_tag("intro")
        self._clear_by_tag("mainMenu")
        self._clear_by_tag("gamePause")
        self._clear_by_tag("gamePause:title")
        self._clear_by_tag("gamePause:option")
        self._clear_by_tag("gamePause:currentOption")
        self._clear_by_tag("gamePause:player")

    def _clear_by_tag(self, tag):
        self.canvas.delete(tag)
