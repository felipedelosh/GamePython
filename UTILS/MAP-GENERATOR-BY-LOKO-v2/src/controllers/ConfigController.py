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
            self.config["MAX_IMAGE_PIXELS"] = int(self.config["MAX_IMAGE_PIXELS"])

            self.config["VALIDATION_IMAGE_SIZE_WIDTH_CHUNK"] = os.getenv("VALIDATION_IMAGE_SIZE_WIDTH_CHUNK")
            self.config["VALIDATION_IMAGE_SIZE_WIDTH_CHUNK"] = int(self.config["VALIDATION_IMAGE_SIZE_WIDTH_CHUNK"])

            self.config["VALIDATION_IMAGE_SIZE_HEIGHT_CHUNK"] = os.getenv("VALIDATION_IMAGE_SIZE_HEIGHT_CHUNK")
            self.config["VALIDATION_IMAGE_SIZE_HEIGHT_CHUNK"] = int(self.config["VALIDATION_IMAGE_SIZE_HEIGHT_CHUNK"])

            # END CONFIG ENV VARS
        except:
            pass

    def getConfig(self, key):
        try:
            return self.config.get(key)
        except:
            return None