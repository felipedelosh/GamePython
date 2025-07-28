"""
FelipedelosH
2025

MovementSystem - Actualiza las posiciones de entidades según velocidad y dirección.
"""

from src.ecs.system import System
from src.ecs.components import PositionComponent, SizeComponent, VelocityComponent, DirectionComponent

class MovementSystem(System):
    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height

    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(PositionComponent, VelocityComponent, DirectionComponent, SizeComponent):
                pos = entity.get_component(PositionComponent)
                vel = entity.get_component(VelocityComponent)
                size = entity.get_component(SizeComponent)
                direction = entity.get_component(DirectionComponent)

                if direction.direction == "up":
                    if pos.y - vel.velocity > 0:
                        pos.y -= vel.velocity

                elif direction.direction == "down":
                    if pos.y + size.h + vel.velocity < self.world_height:
                        pos.y += vel.velocity

                elif direction.direction == "right":
                    if pos.x + size.w + vel.velocity < self.world_width:
                        pos.x += vel.velocity

                elif direction.direction == "left":
                    if pos.x - vel.velocity > 0:
                        pos.x -= vel.velocity
