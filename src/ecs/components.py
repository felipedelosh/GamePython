from src.ecs.component import Component

class PositionComponent(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class SizeComponent(Component):
    def __init__(self, w, h):
        self.w = w
        self.h = h

class VelocityComponent(Component):
    def __init__(self, velocity=0):
        self.velocity = velocity

class DirectionComponent(Component):
    def __init__(self):
        self.current_directions = set()
        self.last_direction = "down"

class SpriteCoordsComponent(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
