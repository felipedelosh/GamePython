"""
FelipedelosH
2025

GameLogger to register: inputs, estados y errores.
"""
import logging
import os
from datetime import datetime

class GameLogger:
    _instance = None

    @staticmethod
    def get_instance():
        if GameLogger._instance is None:
            GameLogger()
        return GameLogger._instance

    def __init__(self):
        if GameLogger._instance is not None:
            raise Exception("GameLogger >> get_instance().")

        if not os.path.exists("logs"):
            os.makedirs("logs")

        log_filename = f"logs/game_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(
            filename=log_filename,
            level=logging.DEBUG,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S"
        )

        self.logger = logging.getLogger("GameLogger")
        GameLogger._instance = self

    def info(self, message):
        self.logger.info(message)
        print(f"[INFO] {message}")

    def warning(self, message):
        self.logger.warning(message)
        print(f"[WARNING] {message}")

    def error(self, message):
        self.logger.error(message)
        print(f"[ERROR] {message}")
