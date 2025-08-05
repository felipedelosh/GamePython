"""
FelipedelosH
2025
"""
from src.UI.IUIRenderer import IUIRenderer
import tkinter as tk

class TkinterRenderer(IUIRenderer):
    def __init__(self, canvas: tk.Canvas, imgIntro, FPS, configuration, gameStateManager, player, world):
        self.canvas = canvas
        self.imgIntro = imgIntro
        self.FPS = FPS
        self.configuration = configuration
        self.gameStateManager = gameStateManager
        self.player = player
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
            
            self.gamePauseOptionsAndCoors["currentOption"] = self.gameStateManager.getStateMachine("pause").pointer

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
            self._reset_game_pause_menu()
        except:
            self.gamePauseOptionsAndCoors["title"] = "ERROR"
            self.gamePauseOptionsAndCoors["menuCoords"] = [320, 0, 480, 640]
            self.gamePauseOptionsAndCoors["items"] = ["ERROR"]

    def _reset_game_pause_menu(self):
        self.gamePauseOptionsAndCoors["currentOption"] = ""
    
    def _delete_no_game_items(self):
        self._clear_by_tag("intro")
        self._clear_by_tag("mainMenu")
        self._clear_by_tag("gamePause")
        self._clear_by_tag("gamePause:title")

    def _clear_by_tag(self, tag):
        self.canvas.delete(tag)
