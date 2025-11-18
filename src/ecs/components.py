from src.ecs.component import Component
from src.entities.statistics import Statistics

class IdentityComponent(Component):
    def __init__(self, nick_name, first_name, second_name, family_name, second_family_name, gender, age, species, level):
        self.nick_name = nick_name
        self.first_name = first_name
        self.second_name = second_name
        self.family_name = family_name
        self.second_family_name = second_family_name
        self.gender = gender
        self.age = age
        self.species = species
        self.level = level

class HealthComponent(Component):
    def __init__(self, hp, hp_max):
        self.hp = hp
        self.hp_max = hp_max

class StatisticsComponent(Component):
    def __init__(self, stats=None):
        if isinstance(stats, dict):
            self.statistics = Statistics(initial_stats=stats, use_random=False)
        elif isinstance(stats, Statistics):
            self.statistics = stats
        else:
            self.statistics = Statistics()

class SensesComponent(Component):
    def __init__(self, senses=None):
        defaults = {
            "vision": 1.0,
            "hearing": 1.0,
            "touch": 1.0,
            "smell": 1.0,
            "taste": 1.0,
        }

        data = {**defaults, **(senses if isinstance(senses, dict) else {})}

        for key, default_val in defaults.items():
            raw = data.get(key, default_val)
            try:
                val = float(raw)
            except (TypeError, ValueError):
                val = default_val
            setattr(self, key, max(0.0, min(1.0, val)))

    def get_json(self):
        return {
            "vision": self.vision,
            "hearing": self.hearing,
            "touch": self.touch,
            "smell": self.smell,
            "taste": self.taste,
        }
    
class BrainComponent(Component):
    def __init__(self, senses: SensesComponent | None = None):
        self.senses = senses or SensesComponent()

    def get_json(self):
        return {
            "senses": self.senses.get_json()
        }

class BodyComponent(Component):
    def __init__(self, braintComponent: BrainComponent | None = None):
        self.braintComponent = braintComponent

    def get_json(self):
        return {}

class CurrencyComponent(Component):
    def __init__(self, amount=0):
        self.amount = max(0, amount)

    def add(self, value):
        if value > 0:
            self.amount += value

    def subtract(self, value):
        if value > 0:
            self.amount = max(0, self.amount - value)

    def __str__(self):
        return f"${self.amount} LCS"

class PositionComponent(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class SizeComponent(Component):
    def __init__(self, w, h):
        self.w = w
        self.h = h

class VelocityComponent(Component):
    def __init__(self, velocity=0):
        self.velocity = velocity

class DirectionComponent(Component):
    def __init__(self):
        self.current_directions = set()
        self.last_direction = "down"

class SpriteCoordsComponent(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class NextPositionComponent(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
