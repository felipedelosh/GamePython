"""
FelipedelosH
2025

CollisionSystem
"""

from src.ecs.system import System
from src.ecs.components import (
    PositionComponent,
    SizeComponent,
    SpriteCoordsComponent,
    NextPositionComponent
)

class CollisionSystem(System):
    def __init__(self, player, world):
        self.player = player
        self.world = world

    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(PositionComponent, SizeComponent, SpriteCoordsComponent, NextPositionComponent):
                pos = entity.get_component(PositionComponent)
                size = entity.get_component(SizeComponent)
                sprite_coords = entity.get_component(SpriteCoordsComponent)
                next_pos = entity.get_component(NextPositionComponent)

                if self._is_walkable(next_pos.x, next_pos.y, sprite_coords):
                    pos.x, pos.y = next_pos.x, next_pos.y
                    sprite_coords.x = pos.x - (size.w / 2)
                    sprite_coords.y = pos.y - (size.h / 2)
                else:
                    next_pos.x, next_pos.y = pos.x, pos.y  

    def _is_walkable(self, x, y, sprite_coords):
        tile_size_w = self.world.w
        tile_size_h = self.world.h

        tile_x = int(x // tile_size_w)
        tile_y = int(y // tile_size_h)

        try:
            # Screen
            if x < 0 or y < 0 or x > self.player.max_pos_x or y > self.player.max_pos_y:
                return False
            
            # Titles
            return self.world.collider[tile_y][tile_x] == 0
        except IndexError:
            return False
        