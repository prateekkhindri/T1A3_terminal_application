import emoji
from lib.display import Display
from player import Player
from rainbow_highlighter import rainbow
from rich.prompt import Prompt
from constants import *


class Board:
    def __init__(self, game_mode):
        self.game_mode = game_mode
        self.current_player_symbol = None
        if game_mode == 1:
            self.player = Player()

    def play(self, mode):
        if mode == 1:
            return self.play_with_computer()

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
