"""
FelipedelosH
2025

Controller all time aspects
"""
class TimeSystem:
    def __init__(self, time_scale=60):
        self.time_scale = time_scale  # 1SEG REAL WORLD = 60SEG GAME
        self.current_minutes = 0  # min to init game
        self.listeners = []

    def update(self, entity, delta_ms):
        game_minutes_passed = (delta_ms / 1000.0) * self.time_scale
        self.current_minutes += game_minutes_passed
        self._check_events()

    def get_time(self):
        total_minutes = int(self.current_minutes)
        days = total_minutes // (24 * 60)
        hours = (total_minutes % (24 * 60)) // 60
        minutes = total_minutes % 60
        return {"day": days, "hour": hours, "minute": minutes}

    def subscribe(self, callback):
        self.listeners.append(callback)

    def _check_events(self):
        for callback in self.listeners:
            callback(self.get_time())
