"""
FelipedelosH
"""
import os
import json
from os import scandir
from PIL import Image as imgConvert
from tkinter import PhotoImage

class Controller:
    def __init__(self) -> None:
        self.path = str(os.path.dirname(os.path.abspath(__file__)))
        self.OUTPUT_DATA = {}
        self.dataToConverArray = self._loadDataToConvert()
        self.dataToConverDict = {}
        self.imgCollider = None
        self.imgColor = None
        self.json_template = {
            "id": 0,
            "collider": [],
            "color": []
        }


    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info
        
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


    def rtnArchieveFilesNames(self):
        """
        Return all files names of data folder
        """
        try:
            path = f"{self.path}/INPUT"

            filesNames = []
            for i in scandir(path):
                if i.is_file():
                    if ".gif" in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return None
        

    def _loadImages(self):
        _data = []

        _data = self.rtnArchieveFilesNames()
        _data = [str(x).replace(".gif", "") for x in _data]

        return _data
    
    def _loadDataToConvert(self):
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
            self.json_template["id"] = key
            _path_collider = f"{self.path}/INPUT/{key}/collider.gif"
            self.imgCollider = PhotoImage(_path_collider)
            toConverCollider = imgConvert.open(_path_collider)

            _path_color = f"{self.path}/INPUT/{key}/color.gif"
            self.imgColor = PhotoImage(_path_color)
            toConverColor = imgConvert.open(_path_color)

            _isfinalDataOk = True

            if toConverCollider.size == (84, 48):
                data = list(toConverCollider.getdata())

                data = str(data)
                data = data.replace("[", "")
                data = data.replace("]", "")

                # Generater collider
                _collider = []
                _aux_collider = []
                count_break = 0
                for i in data.split(","):
                    if int(i) > 50:
                        _aux_collider.append(1)
                    else:
                        _aux_collider.append(0)

                    count_break = count_break + 1
                    if count_break == 84:
                        _collider.append(_aux_collider.copy())
                        _aux_collider = []
                        count_break = 0
            
                self.json_template["collider"] = _collider
            else:
                _isfinalDataOk = _isfinalDataOk and False

            if toConverColor.size == (84, 48):
                im = toConverColor.convert("RGBA")
                pixels = im.load()
                count_break = 0

                _color = []
                _aux_color = []
                for y in range(48):
                    for x in range(84):
                        r, g, b, a = pixels[x, y]

                        if a == 0:
                            _aux_color.append(str("#000000"))
                        else:
                            _aux_color.append(str(f"#{r:02x}{g:02x}{b:02x}"))

                        count_break = count_break + 1
                        if count_break == 84:
                            _color.append(_aux_color.copy())
                            _aux_color = []
                            count_break = 0

                self.json_template["color"] = _color
            else:
                _isfinalDataOk = _isfinalDataOk and False

            if _isfinalDataOk:
                self._save_collider_json(f"{self.path}/OUTPUT/{key}.json", self.json_template)
            return True
        except:
            return False

    def _save_collider_json(self, path, json_template):
        with open(path, "w", encoding="utf-8") as f:
            f.write('{\n')
            f.write(f'    "id": "{json_template["id"]}",\n')
            f.write(f'    "collider": [\n')
            for i, row in enumerate(json_template["collider"]):
                line = "        [" + ", ".join(str(cell) for cell in row) + "]"
                if i < len(json_template["collider"]) - 1:
                    line += ","
                f.write(line + "\n")
            f.write('    ],\n')

            f.write(f'    "color": [\n')
            for i, row in enumerate(json_template["color"]):
                line = "        [" + ", ".join(f'"{cell}"' for cell in row) + "]"
                if i < len(json_template["color"]) - 1:
                    line += ","
                f.write(line + "\n")
            f.write('    ]\n')

            f.write('}\n')
