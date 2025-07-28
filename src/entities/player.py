from src.ecs.entity import Entity
from src.ecs.components import PositionComponent, SizeComponent, VelocityComponent, DirectionComponent
from src.core.assetManager import AssetManager

class Player(Entity):
    def __init__(self, config):
        super().__init__()
        assetManager = AssetManager.get_instance()
        self.add_component(PositionComponent(config.get("displayW")/4,config.get("displayH")/4))
        self.add_component(SizeComponent(config.get("player_w"),config.get("player_h")))
        self.add_component(VelocityComponent(int(config.get("playerVelocity"))))
        self.add_component(DirectionComponent("down"))
        self.max_pos_x = config.get("displayW")
        self.max_pos_y = config.get("displayH")
        self.assetManager = assetManager

    def player_mouve_up(self):
        pos = self.get_component(PositionComponent)
        vel = self.get_component(VelocityComponent)
        direction = self.get_component(DirectionComponent)

        _, _y = self.getSpriteRenderCoords()
        if _y - vel.velocity > 0:
            pos.y -= vel.velocity
            direction.direction = "up"

    def player_mouve_down(self):
        pos = self.get_component(PositionComponent)
        size = self.get_component(SizeComponent)
        vel = self.get_component(VelocityComponent)
        direction = self.get_component(DirectionComponent)

        _, _y = self.getSpriteRenderCoords()
        if _y + size.h + vel.velocity < self.max_pos_y:
            pos.y += vel.velocity
            direction.direction = "down"

    def player_mouve_rigth(self):
        pos = self.get_component(PositionComponent)
        size = self.get_component(SizeComponent)
        vel = self.get_component(VelocityComponent)
        direction = self.get_component(DirectionComponent)

        _x, _ = self.getSpriteRenderCoords()
        if _x + size.w + vel.velocity < self.max_pos_x:
            pos.x += vel.velocity
            direction.direction = "right"

    def player_mouve_left(self):
        pos = self.get_component(PositionComponent)
        vel = self.get_component(VelocityComponent)
        direction = self.get_component(DirectionComponent)

        _x, _ = self.getSpriteRenderCoords()
        if _x - vel.velocity > 0:
            pos.x -= vel.velocity
            direction.direction = "left"

    def getPlayerSprite(self):
        direction = self.get_component(DirectionComponent)
        return self.assetManager.get_sprite("player", direction.direction)

    def getSpriteRenderCoords(self):
        pos = self.get_component(PositionComponent)
        size = self.get_component(SizeComponent)
        _x = pos.x - (size.w / 2)
        _y = pos.y - (size.h / 2)
        return _x, _y
