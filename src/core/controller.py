"""
FelipedelosH
This is the main controller to my videogame
"""
import sys
# LOGs
from src.core.gameLoger import GameLogger
# CONFIG
from src.core.GameConfig import GameConfig
from src.core.control import Control
from src.core.inputHandler import InputHandler
from src.core.gameState import (
    IntroState,
    AdvisoryState,
    MainMenuState,
    GameState,
    GamePauseState,
    GameOptionsState
)
from src.core.gameStateManager import GameStateManager
from src.core.assetManager import AssetManager
from src.UI.TkinterRenderer import TkinterRenderer
from src.UI.UIManager import UIManager
from tkinter import PhotoImage
# Entities
from src.entities.player import Player
from src.entities.world import World
# SYSTEMS
from src.systems.timeSystem import TimeSystem
from src.systems.bodySystem import BodySystem
from src.systems.movementSystem import MovementSystem
from src.systems.collisionSystem import CollisionSystem
from src.systems.statisticsSystem import StatisticsSystem
from src.systems.sensesSystem import SensesSystem


class Controller:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.config = GameConfig()
        self.config.load('config/config.json')
        self.FPS = int(1000/int(self.config.get("FPS")))
        self.dt = 1.0 / float(self.config.get("FPS"))
        self.logger = GameLogger.get_instance(self.config)
        self.logger.info(f"GAME::MEMORY::DATA::SIZE:{self.config.get_config_memory_kb():.2f}KB")
        self.logger.info(f"GAME::STATE_MACHINES::{self.config.get("statesMachines")}")
        self.control = Control(
            self.config.get('key_UP'),
            self.config.get('key_RIGTH'),
            self.config.get('key_DOWN'),
            self.config.get('key_LEFT'),
            self.config.get('key_SELECT'),
            self.config.get('key_START'),
            self.config.get('key_B'),
            self.config.get('key_A'),
            self.config.get('key_Y'),
            self.config.get('key_X'),
            self.config.get('key_L'),
            self.config.get('key_R')
        )
        # Sprites & IMAGES
        self.assetManager = AssetManager.get_instance()
        self.imgIntro =  PhotoImage(file=f"assets/images/{self.config.get("displayH")}/intro.gif")
        self.imgAdvisory = PhotoImage(file=f"assets/images/{self.config.get("displayH")}/advisory.gif")
        self.imgMainMenu = PhotoImage(file=f"assets/images/{self.config.get("displayH")}/mainMenu.gif")
        # Player
        self.player = Player(self.config)
        self._load_assets()
        # Game fun Machines
        self.current_state = None
        self.states = {
            "intro": IntroState(self),
            "advisory": AdvisoryState(self),
            "mainMenu": MainMenuState(self),
            "gameStart": GameState(self),
            "gamePause": GamePauseState(self),
            "gameOptions": GameOptionsState(self)
        }
        self.change_state("intro")
        self.gameStateManager = GameStateManager(self.config.get("statesMachines"), self.control)
        self.inputHandler = InputHandler(self.player, self.control, self.gameStateManager, self)
        # World
        self.world = World(self.config)
        self.world.load_map(f"assets/world/{self.config.get("playerLocation")}.json")
        # GRAPHICS
        self.renderer = TkinterRenderer(self.canvas, self.imgIntro, self.imgAdvisory, self.imgMainMenu, self.FPS, self.config, self.gameStateManager, self.player, self.world)
        self.UImanager = UIManager(self.renderer)
        # Systems
        self.timeSystem = TimeSystem(time_scale=60)
        self.bodySystem = BodySystem(self.config)
        self.movementSystem = MovementSystem(self.config.get("displayW"), self.config.get("displayH"))
        self.collisionSystem = CollisionSystem(self.player, self.world)
        self.statisticsSystem = StatisticsSystem(self.config)
        self.sensesSystem = SensesSystem(self.config.get("playerSenses"))
        self.systems = [
            self.timeSystem,
            self.bodySystem,
            self.movementSystem,
            self.collisionSystem,
            self.statisticsSystem,
            self.sensesSystem
        ]
        # VARS
        self.intro_shown_time = 0
        self.logger.info("CONTROLLER::GAME::INIT")
        self.logger.info(f"PLAYER::DATA::STATISTICS::{self.statisticsSystem.get_stats_as_json(self.player)}")
        self.logger.info(f"PLAYER::DATA::SENSES::{self.sensesSystem.get_stats_as_json(self.player)}")


    def change_state(self, new_state_name):
        if self.current_state:
            self.current_state.exit()
        
        self.current_state = self.states[new_state_name]
        self.current_state.enter()

        if new_state_name == "gamePause":
            self.player.clearCurrentDirections() # Force to Stop Player
            self.renderer._reset_game_pause_menu()
            self.renderer._updates_game_pause_player_menu_info()

        self.logger.info(f"CONTROLLER::GAME::CHANGE::{new_state_name}")

    def update(self):
        current_state_name = self.gameStateManager.getStateMachine("game").pointer
        if self.current_state != self.states[current_state_name]:
            self.change_state(current_state_name)

        for system in self.systems:
            system.update([self.player], self.dt)
            
        self.current_state.update()
        
    def render(self):
        self.current_state.render()

    def keyPressed(self, keycode):
        self.inputHandler.handleKeypress(keycode)

    def keyReleased(self, keycode):
        self.inputHandler.handleKeyRelease(keycode)

    def _load_assets(self):
        player_sprites = {
            "up": f"assets/images/{self.config.get("displayH")}/player/{self.config.get("player_look_up")}",
            "left": f"assets/images/{self.config.get("displayH")}/player/{self.config.get("player_look_left")}",
            "right": f"assets/images/{self.config.get("displayH")}/player/{self.config.get("player_look_right")}",
            "down": f"assets/images/{self.config.get("displayH")}/player/{self.config.get("player_look_down")}"
        }
        self.assetManager.load_sprite_group("player", player_sprites)

    def _exitGame(self, data):
        self.logger.info(f"CONTROLLER::GAME::{data}::EXIT")
        try:
            root = self.canvas.winfo_toplevel()
            root.destroy()
        except Exception:
            sys.exit(0)
