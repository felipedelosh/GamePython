"""
FelipedelosH
2025

UPDATE entity positions
"""
from src.ecs.system import System
from src.ecs.components import PositionComponent, SizeComponent, VelocityComponent, DirectionComponent, SpriteCoordsComponent

class MovementSystem(System):
    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height

    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(PositionComponent, VelocityComponent, DirectionComponent, SizeComponent, SpriteCoordsComponent):
                pos = entity.get_component(PositionComponent)
                vel = entity.get_component(VelocityComponent)
                size = entity.get_component(SizeComponent)
                direction = entity.get_component(DirectionComponent)
                sprite_coords = entity.get_component(SpriteCoordsComponent)

                for d in direction.current_directions:
                    if d == "up" and sprite_coords.y - vel.velocity > 0:
                        pos.y -= vel.velocity
                        direction.last_direction = "up"

                    elif d == "down" and sprite_coords.y + size.h + vel.velocity < self.world_height:
                        pos.y += vel.velocity
                        direction.last_direction = "down"

                    elif d == "right" and sprite_coords.x + size.w + vel.velocity < self.world_width:
                        pos.x += vel.velocity
                        direction.last_direction = "right"

                    elif d == "left" and sprite_coords.x - vel.velocity > 0:
                        pos.x -= vel.velocity
                        direction.last_direction = "left"


                # Update Sprite COORDS
                sprite_coords.x = pos.x - (size.w / 2)
                sprite_coords.y = pos.y - (size.h / 2)
