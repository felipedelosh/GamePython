"""
FelipedelosH
2025

UPDATE entity positions
"""
from src.ecs.system import System
from src.ecs.components import (
    PositionComponent,
    VelocityComponent,
    DirectionComponent,
    NextPositionComponent
)

class MovementSystem(System):
    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height

    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(PositionComponent, VelocityComponent, DirectionComponent, NextPositionComponent):
                pos = entity.get_component(PositionComponent)
                vel = entity.get_component(VelocityComponent)
                direction = entity.get_component(DirectionComponent)
                next_pos = entity.get_component(NextPositionComponent)

                next_pos.x, next_pos.y = pos.x, pos.y

                for d in direction.current_directions:
                    if d == "up":
                        next_pos.y -= vel.velocity
                        direction.last_direction = "up"
                    elif d == "down":
                        next_pos.y += vel.velocity
                        direction.last_direction = "down"
                    elif d == "right":
                        next_pos.x += vel.velocity
                        direction.last_direction = "right"
                    elif d == "left":
                        next_pos.x -= vel.velocity
                        direction.last_direction = "left"
