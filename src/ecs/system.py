"""
FelipedelosH
2025

To garantized every entity hav systems (interface)
"""
from abc import ABC, abstractmethod

class System(ABC):
    @abstractmethod
    def update(self, entities, dt):
        pass
