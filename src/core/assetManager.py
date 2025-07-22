"""
FelipdelosH
2025

Load Sprites, ...
"""
from tkinter import PhotoImage
from typing import Dict

class AssetManager:
    _instance = None

    def __init__(self):
        self._assets = {} # Control of duplicated: key = Entity_LOOK, VALUE = PhotoImage(Path)
        self._sprite_groups: Dict[str, Dict[str, str]] = {} # Relation Entity>>PhotoImage using self._assets

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def load_sprite_group(self, entity_type: str, paths: Dict[str, str]):
        if entity_type not in self._sprite_groups:
            self._sprite_groups[entity_type] = {}

        for key, path in paths.items():
            asset_key = f"{entity_type}_{key}"
            _sprite = PhotoImage(file=path)
            self._assets[asset_key] = _sprite
            self._sprite_groups[entity_type][key] = asset_key

    def get_sprite(self, entity_type: str, state: str) -> PhotoImage:
        asset_key = self._sprite_groups[entity_type][state]
        return self._assets[asset_key]

    def unload_entity_sprites(self, entity_type: str):
        if entity_type in self._sprite_groups:
            for asset_key in self._sprite_groups[entity_type].values():
                del self._assets[asset_key]
            del self._sprite_groups[entity_type]
