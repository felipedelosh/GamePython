"""
FelipedelosH

Implementation of contract: src\\commands\\base.py 
To Make actions
...
"""
from src.commands.base import Command

class JumpCommand(Command):
    def execute(self, entity):
        print(f"{entity} JUMP")

class AttackCommand(Command):
    def execute(self, entity):
        print(f"{entity} ATTACK")
