import numpy as np
import termcolor
import emoji
import time
from lib.display import Display
from player import Player
from rainbow_highlighter import rainbow
from rich.prompt import Prompt
from constants import *
from lib.ai import AI
from lib.utils import Utils
from rich.text import Text


class Board:
    def __init__(self, game_mode):
        self.board_array = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.computer_json_data = Utils.load_json(
            name=json_file_name, data=computer_json_data
        )
        self.multi_json_data = Utils.load_json(
            name=multi_json_file_name, data=multi_json_data
        )
        self.game_mode = game_mode
        self.session_file = None
        self.map_value = None
        self.map_value_file = None
        self.current_player_symbol = None
        self.txt_file_name = None
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
        self.txt_file_name = f"{history}/{self.player.name}.txt"
        self.session_file = open(self.txt_file_name, "w", encoding="utf-8")

        print(f"\n\t Welcome {self.player.name}!")

        Display.show_select_symbol_screen()

        self.current_player_symbol = int(Display.rich_input(
            "\n\tEnter one of the above options", options=symbol_options))

        if self.current_player_symbol == 1:
            self.player.X = self.player.name
            self.player.O = "Computer"

            self.map_value = {
                -1: '<ansigreen>X</ansigreen>',
                1: '<ansiyellow>O</ansiyellow>',
                0: " "
            }

            self.map_value_file = {
                -1: 'X',
                1: 'O',
                0: " "
            }

            Display.show_player_info(self.player, mode=f"Player Information")

            print("\n\tX goes first....")
            print(emoji.emojize("\n\tLets get started :red_heart:",
                                variant="emoji_type"))
            time.sleep(2)

            for i in range(0, 9):
                if (AI.analyze_board(self.board_array) != 0):
                    break
                self.display_board(self.player.name)
                if ((i+self.current_player_symbol) % 2 == 0):
                    self.computer_turn()
                else:
                    self.user_turn("x", name=f"{self.player.name}(X)")

            return self

        else:
            self.player.X = "Computer"
            self.player.O = self.player.name

            Display.show_player_info(self.player, mode=f"Player Information")

            self.map_value = {
                -1: '<ansigreen>O</ansigreen>',
                1: '<ansired>X</ansired>',
                0: " "
            }

            self.map_value_file = {
                -1: 'O',
                1: 'X',
                0: " "
            }

            print("\n\tX goes first....")
            print(emoji.emojize("\n\tLets get started :red_heart:",
                                variant="emoji_type"))
            time.sleep(3)

            for i in range(0, 9):
                if (AI.analyze_board(self.board_array) != 0):
                    break
                self.display_board(self.player.name)
                if ((i+self.current_player_symbol) % 2 == 0):
                    self.computer_turn()
                else:
                    self.user_turn("o", options=None,
                                   name=f"{self.player.name}(O)")
            return self

    def user_turn(self, symbol, options=None, name=None):
        while True:
            pos = self.process_position(options, name, symbol)
            if pos == -1:
                continue
            else:
                break
        self.board_array[pos-1] = -1

        return pos

    def computer_turn(self):
        pos = -1
        value = -2
        for i in range(0, 9):
            if (self.board_array[i] == 0):
                self.board_array[i] = 1
                score = -AI.minimax(self.board_array, -1)
                self.board_array[i] = 0
                if (score > value):
                    value = score
                    pos = i

        self.board_array[pos] = 1
        return pos

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

        self.map_value = {
            -1: '<ansigreen>X</ansigreen>',
            1: '<ansiyellow>O</ansiyellow>',
            0: " "
        }

        self.map_value_file = {
            -1: 'X',
            1: 'O',
            0: " "
        }

        print(f"\n\tWelcome {self.player1.name} and {self.player2.name}!")
        print("\n\tX goes first....")
        print(emoji.emojize("\n\tLets get started :red_heart:",
                            variant="emoji_type"))
        time.sleep(2)
        options = [str(i) for i in range(1, 10)]
        used_option = None

        for i in range(0, 9):
            if (AI.analyze_board(self.board_array) != 0):
                break
            if (i % 2 == 0):
                self.display_board(self.player1.name)
                used_option = self.user_turn(
                    "x", options=options, name=f"{self.player1.name}(X)")
            else:
                self.display_board(self.player2.name)
                used_option = self.multiplayer_user_turn(
                    options=options, name=f"{self.player2.name}(O)")
            if str(used_option) in options:
                options.remove(str(used_option))
        return self

    def process_position(self, options=None, name=None, player=None):
        pos = self.input_position(name, options, player)
        if pos != "" and pos.isnumeric():
            pos = int(pos)
            if pos-1 < len(self.board_array):
                if (self.board_array[pos-1] != 0):
                    termcolor.cprint(
                        "\tPlease use the available options\n", color="red")
                    return -1
                else:
                    return pos
            else:
                termcolor.cprint(
                    "\tPlease use the available options\n", color="red")
                return -1

        else:
            termcolor.cprint("\tPlease use the available options", color="red")
            return -1

    def input_position(self, name, options, player):
        text = Text()
        text.append(f'\t{name}', style=color.get(player))
        text.append(' Enter your position from [1-9]', style=color.get("text"))
        pos = Prompt.ask(text, choices=options)
        return pos

    def display_board(self, player_name, final=None):
        Display.show_board(self.map_value, player_name,
                           self.board_array, final)
        Utils.write_session_file(
            self.session_file, player_name, self.map_value_file, self.board_array)

    def multiplayer_user_turn(self, options=None, name=None):
        while True:
            pos = self.process_position(options, name, "o")
            if pos == -1:
                continue
            else:
                break
        self.board_array[pos-1] = 1
        return pos
