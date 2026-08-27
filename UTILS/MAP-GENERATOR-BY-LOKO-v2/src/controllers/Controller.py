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

    def getAllFoldersInInputPath(self):
        _paths = []

        try:
            path = f"{self.path}/INPUT"
            for i in scandir(path):
                if i.is_dir():
                    _paths.append(i.name)
        except:
            pass

        return _paths

    def _loadDataToConvert(self):
        """
        Read ALL folders in UTILS/MAP-GENERATOR-BY-LOKO-v2/INPUT
        """
        _dataToConvert = []
        _dataPaths = self.getAllFoldersInInputPath()

        for itterPath in _dataPaths:
            file_path_collider = f"{self.path}/INPUT/{itterPath}/collider.gif"
            file_path_color = f"{self.path}/INPUT/{itterPath}/color.gif"

            if os.path.isfile(file_path_collider) and os.path.isfile(file_path_color):
                _dataToConvert.append(itterPath)

        return _dataPaths

    def _convert(self, key):
        try:
            pass
        except:
            return False
