from src.ecs.entity import Entity
from src.ecs.components import PositionComponent, SizeComponent, VelocityComponent, DirectionComponent, SpriteCoordsComponent
from src.core.assetManager import AssetManager

class Player(Entity):
    def __init__(self, config):
        super().__init__()
        assetManager = AssetManager.get_instance()
        self.add_component(PositionComponent(config.get("displayW")/4,config.get("displayH")/4))
        self.add_component(SizeComponent(config.get("player_w"),config.get("player_h")))
        self.add_component(VelocityComponent(int(config.get("playerVelocity"))))
        self.add_component(DirectionComponent())
        self.add_component(SpriteCoordsComponent())
        self.max_pos_x = config.get("displayW")
        self.max_pos_y = config.get("displayH")
        self.assetManager = assetManager

    def getPlayerSprite(self):
        direction = self.get_component(DirectionComponent)
        if direction.current_directions:
            current_dir = next(iter(direction.current_directions))
        else:
            current_dir = direction.last_direction
        return self.assetManager.get_sprite("player", current_dir)

    def getSpriteRenderCoords(self):
        sprite_coords = self.get_component(SpriteCoordsComponent)
        return sprite_coords.x, sprite_coords.y
