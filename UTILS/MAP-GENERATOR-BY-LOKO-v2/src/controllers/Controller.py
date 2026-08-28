"""
FelipedelosH
2026
"""
import os
import json
from os import scandir
from PIL import Image as imgConvert
from PIL import PngImagePlugin
from src.controllers.FolderController import FolderController
from src.controllers.ConfigController import Config

class Controller:
    def __init__(self, path) -> None:
        self.path = path
        FolderController.createInitalFolders(self.path)
        self.config = Config()
        try:
            MAX_IMAGE_PIXELS = self.config.getConfig("MAX_IMAGE_PIXELS")
            imgConvert.MAX_IMAGE_PIXELS = MAX_IMAGE_PIXELS
            print(f"Controller::__init__::MAX_IMAGE_PIXELS::{MAX_IMAGE_PIXELS}")
        except:
            imgConvert.MAX_IMAGE_PIXELS = 300_000_000
            print("Controller::__init__::ERR_SET_MAX_IMAGE_PIXELS::SET_DEFAULT::300_000_000")
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
            print(f"Controller::_convert::OPEN::{key}")
            _id = key
            _path_file =  f"{self.path}/INPUT/{key}/map.png"
            exitstPngFile = os.path.isfile(_path_file)
            if not exitstPngFile:
                print(f"Controller::_convert::PNG_DONT_EXISTS::{key}")
                return False

            print(f"Controller::_convert::FILE_SIZE::{os.path.getsize(_path_file)}")

            with open(_path_file, "rb") as file:
                header = file.read(16)
            print(f"Controller::_convert::HEADER::{header}")

            _image = PngImagePlugin.PngImageFile(_path_file) # USE to generate a colors
            print(f"Controller::_convert::FORMAT::{_image.format}")
            print(f"Controller::_convert::MODE::{_image.mode}")
            print(f"Controller::_convert::SIZE::{_image.size}")
            isValidSizeImg = self._validateImgChunkeableSize(_image)
            if not isValidSizeImg:
                width, height = _image.size
                print(f"Controller::_convert::ERR_IMG_PNG_SIZE::ERR::{width}::ERR::{height}")
                return False

            # Convert B&W
            _collider = _image.convert("L")


            return True
        except Exception as e:
            print(f"Controller::_convert::ERROR::{str(e)}")
            return False

    def _validateImgChunkeableSize(self, _image):
        try:
            width, height = _image.size

            if width % 84 != 0:
                print(f"Controller::_validateImgChunkeableSize::INVALID_WIDTH::{width}::MUST_BE_MULTIPLE_OF_84")
                return False

            if height % 48 != 0:
                print(f"Controller::_validateImgChunkeableSize::INVALID_HEIGHT::{height}::MUST_BE_MULTIPLE_OF_48")
                return False

            return True
        except:
            return False
