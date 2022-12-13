import numpy as np
import emoji
from lib.display import Display
from player import Player
from rainbow_highlighter import rainbow
from rich.prompt import Prompt
from constants import *


class Board:
    def __init__(self, game_mode):
        self.board_array = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.game_mode = game_mode
        self.map_value = None
        self.current_player_symbol = None
        if game_mode == 1:
            self.player = Player()
        elif game_mode == 2:
            self.player1 = Player()
            self.player2 = Player()

    def play(self, mode):
        if mode == 1:
            return self.play_with_computer()
        elif mode == 2:
            return self.play_with_player()

    def play_with_computer(self):
        Display.fancy_print("Playing With Computer")
        self.player.name = Prompt.ask(
            rainbow("\n\tEnter Player Name"), default="Player")

        print(f"\n\t Welcome {self.player.name}!")

        Display.show_select_symbol_screen()

        self.current_player_symbol = int(Display.rich_input(
            "\n\tEnter one of the above options", options=symbol_options))

        if self.current_player_symbol == 1:
            self.player.X = self.player.name
            self.player.O = "Computer"

            Display.show_player_info(self.player, mode=f"Player Information")

            print("\n\tX goes first....")
            print(emoji.emojize("\n\tLets get started :red_heart:",
                                variant="emoji_type"))

        else:
            self.player.X = "Computer"
            self.player.O = self.player.name

            Display.show_player_info(self.player, mode=f"Player Information")

            print("\n\tX goes first....")
            print(emoji.emojize("\n\tLets get started :red_heart:",
                                variant="emoji_type"))

    def play_with_player(self):
        Display.fancy_print("Playing In Multiplayer")
        self.player1.name = Prompt.ask(
            rainbow("\n\tEnter Player Name X >"), default="Player X")
        self.player1.X = self.player1.name

        self.player2.name = Prompt.ask(
            rainbow("\n\tEnter Player Name O >"), default="Player O")
        self.player2.O = self.player2.name
        self.player2.X = self.player1.name
        self.player1.O = self.player2.name

        print(f"\n\tWelcome {self.player1.name} and {self.player2.name}!")
        print("\n\tX goes first....")
        print(emoji.emojize("\n\tLets get started :red_heart:",
                            variant="emoji_type"))

    def display_board(self, player_name, final=None):
        Display.show_board(self.map_value, player_name,
                           self.board_array, final)
