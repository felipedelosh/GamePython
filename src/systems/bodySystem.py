"""
FelipedelosH
2025

BodySystem
"""
from src.ecs.system import System
from src.ecs.components import BodyComponent

class BodySystem(System):
    def __init__(self, config=None):
        self.config = config

    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(BodyComponent):
                body = entity.get_component(BodyComponent)
                pass

    def get_body(self, entity):
        if entity.has_components(BodyComponent):
            return entity.get_component(BodyComponent)
        return None

    def get_body_as_json(self, entity):
        body = self.get_body(entity)
        if body and hasattr(body, "get_json"):
            return body.get_json()
        return None
