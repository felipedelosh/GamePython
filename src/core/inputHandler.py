"""
FelipedelosH
2025

Input Key EXCUTOR Controller
"""
class InputHandler:
    def __init__(self, palyer, config, stateMachineGame):
        self.player = palyer
        self.control = config
        self.stateMachineGame = stateMachineGame


    def handleKeypress(self, keycode):
        if self.stateMachineGame.pointer == "gameStart":
            if keycode == self.control.key_UP:
                self.player.player_mouve_up()
            if keycode == self.control.key_RIGTH:
                self.player.player_mouve_rigth()
            if keycode == self.control.key_DOWN:
                self.player.player_mouve_down()
            if keycode == self.control.key_LEFT:
                self.player.player_mouve_left()    
            if keycode == self.control.key_B:
                print("B")
            if keycode == self.control.key_A:
                print("A")
            if keycode == self.control.key_Y:
                print("Y")
            if keycode == self.control.key_X:
                print("X")
            if keycode == self.control.key_SELECT:
                print("Select")
            if keycode == self.control.key_START:
                print("Start")
            if keycode == self.control.key_L:
                print("L")
            if keycode == self.control.key_R:
                print("R")
