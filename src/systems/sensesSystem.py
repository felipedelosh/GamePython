"""
FelipedelosH
2025

SensesSystem
"""
from src.ecs.system import System
from src.ecs.components import SensesComponent

class SensesSystem(System):
    def __init__(self, config):
        self.cfg = config

    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(SensesComponent):
                stats = entity.get_component(SensesComponent)
                # ...

    def get_senses(self, entity):
        if entity.has_components(SensesComponent):
            return entity.get_component(SensesComponent)
        return None
    

    def get_stats_as_json(self, entity):
        if entity.has_components(SensesComponent):
            senses = self.get_senses(entity)
            return senses.get_json() if senses else None
        return None
