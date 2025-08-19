"""
FelipedelosH
2025
Attribs
"""
import random

STAT_LIMITS = {
    "time": (0, None),
    "attack": (1, 100),
    "defense": (1, 100),
    "energy": (0, 100),
    "hunger": (0, 100),
    "intelligence": (70, 220),
    "strength": (0, 150),
    "mental_health": (0, 100),
    "physical_health": (0, 100),
    "social_skills": (0, 100),
    "job_performance": (0, 100),
    "velocity": (1, 100)
}

class Statistics:
    def __init__(self, initial_stats=None, use_random=True):
        self.time = 0
        for stat, (low, high) in STAT_LIMITS.items():
            if initial_stats and stat in initial_stats:
                value = initial_stats[stat]
            elif use_random:
                value = random.randint(low, high if high else 100)
            else:
                value = low
            setattr(self, stat, value)

    def get_attr(self, stat_name):
        if not hasattr(self, stat_name):
            return None
        
        return getattr(self, stat_name)

    def update_stat(self, stat_name, value, mode="add"):
        if not hasattr(self, stat_name):
            raise ValueError(f"Statistic '{stat_name}' does not exist.")
        current = getattr(self, stat_name)
        if mode == "add":
            new_value = current + value
        elif mode == "set":
            new_value = value
        elif mode == "mult":
            new_value = current * value
        else:
            raise ValueError(f"Unsupported mode '{mode}'.")
        
        min_val, max_val = STAT_LIMITS.get(stat_name, (0, 100))
        if max_val is not None:
            new_value = max(min_val, min(new_value, max_val))
        setattr(self, stat_name, new_value)

    def get_json(self):
        return dict(self.__dict__)

    def __repr__(self):
        stats = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"Statistics({stats})"
