"""
FelipedelosH
2026
"""
import os
import json
from os import scandir
from PIL import Image as imgConvert
from tkinter import PhotoImage
from src.controllers.FolderController import FolderController

class Controller:
    def __init__(self, path) -> None:
        self.path = path
        FolderController.createInitalFolders(self.path)
        self.dataToConverArray = self._loadDataToConvert()

    def _loadDataToConvert(self):
        return ["test"]

    def _convert(self, key):
        try:
            pass
        except:
            pass
