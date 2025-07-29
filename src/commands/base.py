"""
FelipedelosH
2025

Define INTERFACE of COMMANDs
"""
class Command:
    def execute(self, entity):
        raise NotImplementedError("Subclasses must implement execute()")
