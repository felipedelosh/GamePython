"""
FelipedelosH
2025
"""
from src.UI.IUIRenderer import IUIRenderer
import tkinter as tk

class TkinterRenderer(IUIRenderer):
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas

    def render_image(self, image, x, y, anchor="nw", tag=None):
        return self.canvas.create_image(x, y, image=image, anchor=anchor, tag=tag)

    def render_line(self, x1, y1, x2, y2, fill="black", arrow=None, tag=None):
        return self.canvas.create_line(x1, y1, x2, y2, fill=fill, arrow=arrow, tag=tag)

    def render_rectangle(self, x1, y1, x2, y2, fill="", tag=None):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, tag=tag)
    
    def delete_no_game_items(self):
        self.clear_by_tag("intro")
        self.clear_by_tag("mainMenu")

    def render_text(self, x, y, text, tag=None):
        return self.canvas.create_text(x, y, text=text, tag=tag)

    def clear_by_tag(self, tag):
        self.canvas.delete(tag)
