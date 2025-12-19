"""
FelipedelosH
This is the main controller to load setting of config/config.json
"""
import json
import sys

class GameConfig:
    def __init__(self):
        self.LAN = None
        self._config = {}
        self._default_config = self.defaultConfig() 

    def load(self, config_path: str) -> None:
        # LOAD CONFIG FILE
        try:
            # GENERAL CONFIG
            with open(config_path, 'r', encoding='utf-8') as f:
                self._config = json.load(f)

            # LANGUAGUE
            self.LAN = self._config["LAN"]
            text_path = f"assets/LAN/{self.LAN}/TEXT.json"

            with open(text_path, 'r', encoding='utf-8') as f:
                text_data = json.load(f)
            self._config = {**self._config, **text_data}

            # DATA
            deaths_path = f"assets/LAN/{self.LAN}/DEATHS.json"

            with open(deaths_path, 'r', encoding='utf-8') as f:
                deaths_data = json.load(f)
            self._config = {**self._config, **deaths_data}
        except:
            self._config = self._default_config.copy()


    def get(self, key: str, default=None):
        return self._config.get(key, default)
    
    def get_config_memory_kb(self) -> float:
        def deep_size(obj, seen=None):
            if seen is None:
                seen = set()
            obj_id = id(obj)
            if obj_id in seen:
                return 0
            seen.add(obj_id)
            size = sys.getsizeof(obj)
            if isinstance(obj, dict):
                size += sum((deep_size(k, seen) + deep_size(v, seen)) for k, v in obj.items())
            elif isinstance(obj, (list, tuple, set, frozenset)):
                size += sum(deep_size(i, seen) for i in obj)
            return size

        return round(deep_size(self._config) / 1024, 2)

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
            "floorW":84,
            "floorH":48,
            "LAN": "ESP",
            "FPS": 32,
            "intro_duration": 1500,
            "playerName": "Human",
            "playerAge": 0,
            "player_look_up": "player_look_up.png",
            "player_look_left": "player_look_left.png",
            "player_look_rigth": "player_look_rigth.png",
            "player_look_down": "player_look_down.png",
            "statesMachines": {
                "game": {
                "initial": "intro",
                "states": ["intro", "mainMenu", "gameStart", "gamePause", "gameOptions"],
                "conections": [
                    "intro:mainMenu:symbol:t",
                    "mainMenu:gameStart:symbol:gameStart",
                    "gameStart:gameStart:controls:direction_buttons",
                    "gameStart:gameStart:controls:action_buttons",
                    "gameStart:gamePause:controls:key_START",
                    "gamePause:gameStart:controls:key_START",
                    "gameStart:gameOptions:controls:key_SELECT",
                    "gameOptions:gameStart:controls:key_SELECT",
                    "gamePause:gameOptions:controls:key_SELECT",
                    "gameOptions:gamePause:controls:key_START"
                ]
                },
                "mainMenu": {
                "initial": "newGame",
                "states": ["newGame", "continueGame", "optionsGame", "exitGame"],
                "conections": [
                    "newGame:continueGame:controls:key_DOWN",
                    "continueGame:newGame:controls:key_UP",
                    "continueGame:optionsGame:controls:key_DOWN",
                    "optionsGame:continueGame:controls:key_UP",
                    "optionsGame:exitGame:controls:key_DOWN",
                    "exitGame:optionsGame:controls:key_UP"
                ]
                }
            }
        }
