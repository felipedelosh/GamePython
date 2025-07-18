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
    def render_text(self, x, y, text, tag): pass

    @abstractmethod
    def clear_by_tag(self, tag): pass
