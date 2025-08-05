"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IUIRenderer(ABC):
    @abstractmethod
    def render_image(self, image, x, y, anchor, tag): pass

    @abstractmethod
    def render_line(self, x1, y1, x2, y2, fill, arrow, tag): pass

    @abstractmethod
    def render_rectangle(self, x1, y1, x2, y2, fill, tag): pass

    @abstractmethod
    def render_circle(self, x, y, r, color, tag): pass

    @abstractmethod
    def render_text(self, x, y, text, tag): pass

    @abstractmethod
    def render_player(self): pass

    @abstractmethod
    def render_game_main_menu(self): pass

    @abstractmethod
    def render_game_intro(self): pass

    @abstractmethod
    def render_game_pause(self): pass

    @abstractmethod
    def render_floor(self): pass

    @abstractmethod
    def delete_no_game_items(self): pass

    @abstractmethod
    def clear_by_tag(self, tag): pass
