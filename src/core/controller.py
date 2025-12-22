"""
FelipedelosH
This is the main controller to my videogame
"""
import sys
# LOGs
from src.core.gameLoger import GameLogger
# CONFIG
from src.core.TextPaginator import TextPaginator
from src.core.GameConfig import GameConfig
from src.core.control import Control
from src.core.inputHandler import InputHandler
from src.core.gameState import (
    IntroState,
    AdvisoryState,
    MainMenuState,
    GameState,
    GameTextDisplayedState,
    GamePauseState,
    GameOptionsState
)
from src.core.gameStateManager import GameStateManager
from src.core.assetManager import AssetManager
from src.UI.TkinterRenderer import TkinterRenderer
from src.UI.UIManager import UIManager
# Entities
from src.entities.player import Player
from src.entities.world import World
# Components
from src.ecs.components import IdentityComponent
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
        self.logger.info(f"CONTROLLERGAME::MEMORY::DATA::SIZE:{self.config.get_config_memory_kb():.2f}KB")
        self.logger.info(f"CONTROLLERGAME::GAME::STATE_MACHINES::{self.config.get("statesMachines").keys()}")
        if self.logger.enabled:
            print(self.config.get("statesMachines"))
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
            "gameTextDisplayed": GameTextDisplayedState(self),
            "gamePause": GamePauseState(self),
            "gameOptions": GameOptionsState(self)
        }
        self.change_state("intro")
        self.gameStateManager = GameStateManager(self.config.get("statesMachines"), self.control)
        self.inputHandler = InputHandler(self.player, self.control, self.gameStateManager, self)
        # TEXTS
        self.isLastPageRead = False
        self.textPaginator = TextPaginator(
            self.config.get("DIALOG_LOREM"),
            self.config.get("displayed_words_counter")
        )
        # World
        self.world = World(self.config)
        self.world.load_map(f"assets/world/{self.config.get("playerLocation")}.json")
        # GRAPHICS
        self.renderer = TkinterRenderer(self.canvas, self.assetManager, self.FPS, self.config, self.gameStateManager, self.player, self.world)
        self.UImanager = UIManager(self.renderer)
        # Systems
        self.timeSystem = TimeSystem(time_scale=60)
        self.bodySystem = BodySystem(self.config)
        self.movementSystem = MovementSystem(self.config.get("displayW"), self.config.get("displayH"))
        self.collisionSystem = CollisionSystem(self.player, self.world)
        self.statisticsSystem = StatisticsSystem(self.config)
        self.sensesSystem = SensesSystem(self.player.senses)
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
        self.logger.info(f"CONTROLLERGAME::PLAYER::DATA::IDENTITY::{self.player.get_component(IdentityComponent).get_json()}")
        self.logger.info(f"CONTROLLERGAME::PLAYER::DATA::DEATH::>>{self.player.death_cause}<<")
        self.logger.info(f"CONTROLLERGAME::PLAYER::DATA::STATISTICS::{self.statisticsSystem.get_stats_as_json(self.player)}")
        self.logger.info(f"CONTROLLERGAME::PLAYER::DATA::SENSES::{self.player.senses.get_json()}")


    def change_state(self, new_state_name):
        if self.current_state:
            self.current_state.exit()
        
        self.current_state = self.states[new_state_name]
        self.current_state.enter()

        if new_state_name == "gamePause":
            self.player.clearCurrentDirections() # Force to Stop Player
            self.renderer._reset_game_pause_menu()
            self.renderer._updates_game_pause_player_menu_info()

        if new_state_name == "gameTextDisplayed":
            self.player.clearCurrentDirections() # Force to Stop Player
            text = self.textPaginator.current_page()
            totalPages = self.textPaginator.total_pages()
            self.renderer._updates_game_text_displayed(text, totalPages)

        self.logger.info(f"CONTROLLERGAME::GAME::CHANGE::{new_state_name}")

    def _text_paginator_next_page(self):
        text = self.textPaginator.next_page()
        totalPages = self.textPaginator.total_pages()
        self.renderer._updates_game_text_displayed(text, totalPages)

        if self.textPaginator.is_last_page():
            if self.isLastPageRead:
                self.gameStateManager.getStateMachine("game").mouvePointer("g")
            self.isLastPageRead = True

        self.logger.info(f"CONTROLLERGAME::GAME::CHANGE::TEXT")

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
        self.assetManager.save_images_group("intro" , f"assets/images/{self.config.get("displayH")}/intro.gif")
        self.assetManager.save_images_group("advisory" , f"assets/images/{self.config.get("displayH")}/advisory.gif")
        self.assetManager.save_images_group("mainMenu" , f"assets/images/{self.config.get("displayH")}/mainMenu.gif")

        _animated_sprite_group = {}
        for itterStateAnimated in self.config.get("statesMachines")["animatedEntity"]["states"]:
            _sprite = itterStateAnimated
            _pathSprite = f"assets/images/{self.config.get("displayH")}/skins/player/{_sprite}.png"
            _animated_sprite_group[_sprite] = _pathSprite

        try:
            self.assetManager.save_sprite_group("animated", _animated_sprite_group)
        except Exception as e:
            self.logger.error(f"CONTROLLER::GAME::CREATE_SPRITES::FAILED_GROUP::{_animated_sprite_group}")
            self.logger.error(f"CONTROLLERGAME::GAME::CREATE_SPRITES::ASSET_MANAGER_ERROR::{type(e).__name__}::{e}")

    def _exitGame(self, data):
        self.logger.info(f"CONTROLLERGAME::GAME::{data}::EXIT")
        try:
            root = self.canvas.winfo_toplevel()
            root.destroy()
        except Exception:
            sys.exit(0)
