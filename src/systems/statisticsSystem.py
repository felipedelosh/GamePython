"""
FelipedelosH
2025

StatisticsSystem
"""
from src.ecs.system import System
from src.ecs.components import StatisticsComponent

class StatisticsSystem(System):
    def __init__(self, config):
        pass

    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(StatisticsComponent):
                stats = entity.get_component(StatisticsComponent).statistics

                # UPDATE
                # stats.update_stat("?", self.ABC, mode="add")

                # RULES
                # if stats.X > #:
                #     stats.update_stat("?", #, mode="?")

    def get_stats(self, entity):
        if entity.has_components(StatisticsComponent):
            return entity.get_component(StatisticsComponent).statistics
        return None
    

    def get_stats_as_json(self, entity):
        if entity.has_components(StatisticsComponent):
            stats = entity.get_component(StatisticsComponent).statistics
            return stats.get_json()
        return None