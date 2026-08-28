"""
FelipedelosH
2026
"""
import os
import json
import time
from os import scandir
from PIL import Image as imgConvert
from PIL import PngImagePlugin
from src.models.OutputWorld import OutputWorld
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

        # VARS
        self._CHUNK_KEYS_SET = set() # Sores all keyname_N_M
        self._CHUNKS = {} # Save a chunk in ["keyname_N_M"] = OutputWorld

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
            
            # Chunked
            _image_chunked_dict = self._splitImageInChunks(key, _image)
            _collider_chunked_dict = self._splitImageInChunks(key, _collider)
            _totalChunks = len(self._CHUNK_KEYS_SET)
            print(f"Coontroller::_convert::TOTAL_CHUNKED::{_totalChunks}")
            if _totalChunks == 0:
                print("Controller::_convert::NO_CHUNKS")
                return False

            # Display Progress
            processed_count = 0
            thresholds = [
                0.05,
                0.10,
                0.15,
                0.20,
                0.25,
                0.30,
                0.35,
                0.40,
                0.45,
                0.50,
                0.55,
                0.60,
                0.65,
                0.70,
                0.75,
                0.80,
                0.85,
                0.90,
                0.95,
                1.00
            ]
            threshold_index = 0
            start_time = time.perf_counter()
            last_threshold_time = start_time
            _isChunkedAndSaveComplete = True
            for i in self._CHUNK_KEYS_SET:
                world = OutputWorld(i)

                collider = self.convertChunktBlackAndWhiteImageInCollider(_collider_chunked_dict[i])
                if not collider:
                    _isChunkedAndSaveComplete = False
                    print(f"Controller::_convert::ERR_SAVE_CHUNK_B&W::{i}")
                    break
                world.set_collider(collider)
            
                color = self.convertChunkColorInColor(_image_chunked_dict[i])
                if not color:
                    _isChunkedAndSaveComplete = False
                    print(f"Controller::_convert::ERR_SAVE_CHUNK_COLOR::{i}")
                    break
                world.set_color(color)

                self._CHUNKS[i] = world

                # PROGRESS
                processed_count = processed_count + 1
                if threshold_index < len(thresholds):
                    progress = processed_count / _totalChunks
                    if progress >= thresholds[threshold_index]:
                        now = time.perf_counter()
                        percent = int(thresholds[threshold_index] * 100)

                        interval_seconds = now - last_threshold_time
                        total_seconds = now - start_time

                        interval_minutes = interval_seconds / 60
                        total_minutes = total_seconds / 60

                        # Average processing time per chunk
                        average_seconds_per_chunk = (total_seconds / processed_count)
                        remaining_chunks = (_totalChunks - processed_count)
                        estimated_remaining_seconds = (remaining_chunks * average_seconds_per_chunk)
                        estimated_remaining_minutes = (estimated_remaining_seconds / 60)


                        print(
                            f"Controller::_convert::PROGRESS::"
                            f"{processed_count}/{_totalChunks} "
                            f"({percent}%) | "
                            f"Interval: {interval_minutes:.2f} min | "
                            f"Total: {total_minutes:.2f} min | "
                            f"ETA: {estimated_remaining_minutes:.2f} min"
                        )

                        last_threshold_time = now
                        threshold_index = threshold_index + 1

            if not _isChunkedAndSaveComplete:
                print(f"Controller::_convert::ERR_FATAL_SAVING_CHUNKS")
                return False

            total_time = time.perf_counter() - start_time
            print(
                f"Controller::_convert::CHUNK_PROCESS_COMPLETE::"
                f"TOTAL::{_totalChunks}::"
                f"TIME::{total_time / 60:.2f}_MIN"
            )
            return True
        except Exception as e:
            print(f"Controller::_convert::ERROR::{str(e)}")
            return False
    def _validateImgChunkeableSize(self, _image):
        try:
            width, height = _image.size

            if width % self.config.getConfig("VALIDATION_IMAGE_SIZE_WIDTH_CHUNK") != 0:
                print(f"Controller::_validateImgChunkeableSize::INVALID_WIDTH::{width}::MUST_BE_MULTIPLE_OF_84")
                return False

            if height % self.config.getConfig("VALIDATION_IMAGE_SIZE_HEIGHT_CHUNK") != 0:
                print(f"Controller::_validateImgChunkeableSize::INVALID_HEIGHT::{height}::MUST_BE_MULTIPLE_OF_48")
                return False

            return True
        except:
            return False

    def _splitImageInChunks(self, key, image):
        _chunks = {}

        try:
            chunk_width = self.config.getConfig("VALIDATION_IMAGE_SIZE_WIDTH_CHUNK")
            chunk_height = self.config.getConfig("VALIDATION_IMAGE_SIZE_HEIGHT_CHUNK")
            width, height = image.size
            total_cols = width // chunk_width
            total_rows = height // chunk_height

            print(f"Controller::_splitImageInChunks::ROWS::{total_rows}::COLS::{total_cols}")
            for row in range(total_rows):
                for col in range(total_cols):
                    left = col * chunk_width
                    top = row * chunk_height

                    right = left + chunk_width
                    bottom = top + chunk_height

                    chunk_key = f"{key}_{row}_{col}"
                    self._CHUNK_KEYS_SET.add(chunk_key)

                    chunk_image = image.crop((left, top, right, bottom))
                    _chunks[chunk_key] = chunk_image

            print(f"Controller::_splitImageInChunks::TOTAL_CHUNKS::{len(_chunks)}")
            return _chunks
        except Exception as e:
            print(f"Controller::_splitImageInChunks::ERROR::{str(e)}")
            return {}

    def convertChunktBlackAndWhiteImageInCollider(self, _imageBW):
        try:
            chunk_width = self.config.getConfig("VALIDATION_IMAGE_SIZE_WIDTH_CHUNK")
            data = list(_imageBW.getdata())

            data = str(data)
            data = data.replace("[", "")
            data = data.replace("]", "")

            _collider = []
            _aux_collider = []
            count_break = 0
            for i in data.split(","):
                if int(i) < 127:
                    _aux_collider.append(1)
                else:
                    _aux_collider.append(0)

                count_break = count_break + 1
                if count_break == chunk_width:
                    _collider.append(_aux_collider.copy())
                    _aux_collider = []
                    count_break = 0

            return _collider
        except Exception as e:
            print(f"Controller::convertChunktBlackAndWhiteImageInCollider::ERR_FATAL_SAVE_CHUNK::{str(e)}")
            return None

    def convertChunkColorInColor(self, _image):
        try:
            chunk_width = self.config.getConfig("VALIDATION_IMAGE_SIZE_WIDTH_CHUNK")
            chunk_height = self.config.getConfig("VALIDATION_IMAGE_SIZE_HEIGHT_CHUNK")

            im = _image.convert("RGBA")
            pixels = im.load()

            _color = []

            for y in range(chunk_height):
                _aux_color = []

                for x in range(chunk_width):
                    r, g, b, a = pixels[x, y]

                    if a == 0:
                        _aux_color.append("#000000")
                    else:
                        _aux_color.append(
                            f"#{r:02x}{g:02x}{b:02x}"
                        )

                _color.append(_aux_color)

            return _color
        except Exception as e:
            print(f"Controller::convertChunkColorInColor::ERROR::{str(e)}")
            return None
