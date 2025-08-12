from src.ecs.component import Component
from src.entities.statistics import Statistics


class IdentityComponent(Component):
    def __init__(self, name, gender, age, species, level):
        self.name = name
        self.gender = gender
        self.age = age
        self.species = species
        self.level = level

class HealthComponent(Component):
    def __init__(self, hp, hp_max):
        self.hp = hp
        self.hp_max = hp_max

class StatisticsComponent(Component):
    def __init__(self, stats=None):
        if isinstance(stats, dict):
            self.statistics = Statistics(initial_stats=stats, use_random=False)
        elif isinstance(stats, Statistics):
            self.statistics = stats
        else:
            self.statistics = Statistics()

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

class NextPositionComponent(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
