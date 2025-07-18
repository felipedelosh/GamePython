"""
FelipedelosH
2025
"""
from src.UI.IUIRenderer import IUIRenderer
import tkinter as tk

class TkinterRenderer(IUIRenderer):
    def __init__(self, canvas: tk.Canvas, configuration, player, world):
        self.canvas = canvas
        self.configuration = configuration
        self.player = player
        self.world = world
        self.IdTempWorldToPaint = ""

    def render_image(self, image, x, y, anchor="nw", tag=None):
        return self.canvas.create_image(x, y, image=image, anchor=anchor, tag=tag)

    def render_line(self, x1, y1, x2, y2, fill="black", arrow=None, tag=None):
        return self.canvas.create_line(x1, y1, x2, y2, fill=fill, arrow=arrow, tag=tag)

    def render_rectangle(self, x1, y1, x2, y2, fill="", tag=None):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, tag=tag)
    
    def render_text(self, x, y, text, tag=None):
        return self.canvas.create_text(x, y, text=text, tag=tag)
    
    def render_player(self):
        self.clear_by_tag("player")
        _player_img = self.player.getPlayerSprite()
        self.render_image(_player_img, self.player.posX, self.player.posY, anchor="nw", tag="player")
    
    def render_floor(self):
        if self.world.idWorld != self.IdTempWorldToPaint:
            self.clear_by_tag("world")
            _x = float(self.configuration.get("displayW"))/84
            _y = float(self.configuration.get("displayH"))/48
            for i in range(0, self.world.maxY):
                for j in range(0, self.world.maxX):
                    if i%2==0 and j%2==0:
                        self.canvas.create_rectangle(_x*j,_y*i,_x*(j+1),_y*(i+1), fill="black", tags="world")
                    else:
                        self.canvas.create_rectangle(_x*j,_y*i,_x*(j+1),_y*(i+1), fill="red", tags="world")
            
            self.IdTempWorldToPaint = self.world.idWorld
    
    def delete_no_game_items(self):
        self.clear_by_tag("intro")
        self.clear_by_tag("mainMenu")

    def clear_by_tag(self, tag):
        self.canvas.delete(tag)
