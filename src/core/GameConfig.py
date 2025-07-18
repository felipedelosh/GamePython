"""
FelipedelosH
This is the main controller to load setting of config\config.json
"""
import json

class GameConfig:
    def __init__(self):
        self._config = {}
        self._default_config = self.defaultConfig()

    def load(self, config_path: str) -> None:
        try:
            with open(config_path, 'r') as f:
                self._config = {**self._default_config, **json.load(f)}
        except FileNotFoundError:
            print("Config file not found, using defaults")
            self._config = self._default_config.copy()
        except json.JSONDecodeError:
            print("Invalid JSON config, using defaults")
            self._config = self._default_config.copy()

    def get(self, key: str, default=None):
        return self._config.get(key, default)
    
    @property
    def controls(self) -> dict:
        return {
            'key_UP': self.get('key_UP', 38),
            'key_RIGTH': self.get('key_RIGTH', 39),
            'key_DOWN': self.get('key_DOWN', 40),
            'key_LEFT': self.get('key_LEFT', 37),
            'key_SELECT': self.get('key_SELECT', 32),
            'key_START': self.get('key_START', 13),
            'key_B': self.get('key_B', 90),
            'key_A': self.get('key_A', 88), 
            'key_Y': self.get('key_Y', 67),
            'key_X': self.get('key_X', 86),
            'key_L': self.get('key_L', 65),
            'key_R': self.get('key_R', 83)
        }

    def defaultConfig(self):
        return {
            "displayW": 640,
            "displayH": 480,
            "FPS": 30,
            "playerVelocity": 5
        }
