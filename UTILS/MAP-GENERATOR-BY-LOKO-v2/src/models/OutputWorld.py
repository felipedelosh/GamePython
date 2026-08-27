"""
FelipedelosH
2026

Generate a MAP CHUNK
"""
class OutputWorld:
    def __init__(self, world_id):
        self.id = world_id
        self.collider = []
        self.color = []

    def set_collider(self, collider):
        self.collider = collider

    def set_color(self, color):
        self.color = color

    def to_dict(self):
        return {
            "id": self.id,
            "collider": self.collider,
            "color": self.color
        }
