"""
FelipedelosH

Implementation of contract: src\\commands\\base.py 
To mouve:
UP
DOWN
LEFT
RIGHT
"""
from src.commands.base import Command
from src.ecs.components import DirectionComponent


# --- PRESS COMMANDS ---
class MoveUpCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.add("up")
        direction.last_direction = "up"


class MoveDownCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.add("down")
        direction.last_direction = "down"


class MoveLeftCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.add("left")
        direction.last_direction = "left"


class MoveRightCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.add("right")
        direction.last_direction = "right"


# --- RELEASE COMMANDS ---
class StopMoveUpCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.discard("up")


class StopMoveDownCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.discard("down")


class StopMoveLeftCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.discard("left")


class StopMoveRightCommand(Command):
    def execute(self, entity):
        direction = entity.get_component(DirectionComponent)
        direction.current_directions.discard("right")