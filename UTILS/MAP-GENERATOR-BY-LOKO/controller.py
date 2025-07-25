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
        self._images = self._loadImages()
        self.img = None
        self.json_template = {
            "id": 0,
            "collider": []
        }


    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info


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
    

    def _convert(self, img):
        try:
            _path = f"{self.path}/INPUT/{img}.gif"
            self.img = PhotoImage(_path)

            toConvert = imgConvert.open(_path)
            data = ""

            if toConvert.size == (84, 48):
                data = list(toConvert.getdata())

                data = str(data)
                data = data.replace("[", "")
                data = data.replace("]", "")

                # Generater collider
                _collider = []
                _aux_collider = []
                count_break = 0
                for i in data.split(","):
                    if int(i) > 50:
                        _aux_collider.append(0)
                    else:
                        _aux_collider.append(1)

                    count_break = count_break + 1
                    if count_break == 84:
                        _collider.append(_aux_collider.copy())
                        _aux_collider = []
                        count_break = 0
            

                self.json_template["id"] = img
                self.json_template["collider"] = _collider

                self._save_collider_json(f"{self.path}/OUTPUT/{img}.json", self.json_template)
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

            f.write('    ]\n')
            f.write('}\n')
