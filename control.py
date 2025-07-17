"""
this is the player control

To mouve and interact with the video game
"""


class Control(object):
    def __init__(self, key_UP, key_RIGTH, key_DOWN, key_LEFT, key_SELECT, key_START, key_B, key_A, key_Y, key_X, key_L, key_R) -> None:
        self.key_UP = key_UP
        self.key_RIGTH = key_RIGTH
        self.key_DOWN = key_DOWN
        self.key_LEFT = key_LEFT
        self.key_SELECT = key_SELECT
        self.key_START = key_START
        self.key_B = key_B
        self.key_A = key_A
        self.key_Y = key_Y
        self.key_X = key_X
        self.key_L = key_L
        self.key_R = key_R
        self.keyResult = [key_UP, key_RIGTH, key_DOWN, key_LEFT, key_SELECT, key_START, key_B, key_A, key_Y, key_X, key_L, key_R] # Save all number code of keyboard
        self.direction_buttons = [key_UP, key_RIGTH, key_DOWN, key_LEFT]
        self.action_buttons = [key_B, key_A, key_Y, key_X, key_L, key_R]
