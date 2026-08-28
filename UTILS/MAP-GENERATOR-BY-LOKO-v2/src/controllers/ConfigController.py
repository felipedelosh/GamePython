"""
FelipedelosH
2026

Read all config from: .env
"""
import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        self.config = {}
        self.loadConfig()

    def loadConfig(self):
        try:
            load_dotenv()

            # CONFIG ENV VARS
            # self.config[""] = os.getenv("")
            self.config["MAX_IMAGE_PIXELS"] = os.getenv("MAX_IMAGE_PIXELS")

            # END CONFIG ENV VARS
        except:
            pass

    def getConfig(self, key):
        try:
            return self.config.get(key)
        except:
            return None