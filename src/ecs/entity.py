"""
FelipedelosH
2025

BASE ENTITY IN ECS PATTERN
"""
from src.ecs.components import PositionComponent

class Entity:
    _id_counter = 1

    def __init__(self):
        self.id = Entity._id_counter
        Entity._id_counter += 1
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def get_component(self, comp_type):
        return self.components.get(comp_type, None)

    def has_components(self, *comp_types):
        return all(ct in self.components for ct in comp_types)

    @property
    def x(self):
        pos = self.get_component(PositionComponent)
        return pos.x if pos else None

    @property
    def y(self):
        pos = self.get_component(PositionComponent)
        return pos.y if pos else None
