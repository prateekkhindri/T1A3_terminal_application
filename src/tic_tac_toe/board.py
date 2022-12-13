
from lib.display import Display
from player import Player


class Board:
    def __init__(self, game_mode):
        if game_mode == 1:
            self.player = Player()

    def play(self, mode):
        if mode == 1:
            return self.play_with_computer()

    def play_with_computer(self):
        Display.fancy_print("Playing With Computer")
