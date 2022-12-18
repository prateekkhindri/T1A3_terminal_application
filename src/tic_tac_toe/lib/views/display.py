import termcolor
import emoji
from rich.table import Table
from rich.padding import Padding
from rich.prompt import Prompt
from rich.text import Text
from lib.utils.constants import console, text_color
from prompt_toolkit import print_formatted_text, HTML
from pyfiglet import figlet_format


class Display:
    @classmethod
    def rich_input(cls, text, options):
        text = Text(text, style=text_color['input_text'])
        return Prompt.ask(text, choices=options)

    @classmethod
    def show_game_mode_select_screen(cls):
        termcolor.cprint(
            "               ---------------------------------------------------------------------", color="red", attrs=["bold"])
        termcolor.cprint(figlet_format(
            "\tUNBEATABLE Tic-Tac-Toe", font='puffy', justify="center", width=100), color="red")
        termcolor.cprint(
            "               ---------------------------------------------------------------------", color="red", attrs=["bold"])
        print("\t                            Developed with 💜 by ", end=" ")
        termcolor.cprint("\n\n                                      Prateek Khindri",
                         color="blue", attrs=["bold"])
        termcolor.cprint(
            "               ---------------------------------------------------------------------", color="red", attrs=["bold"])

        table = Table(title="Select Game Mode",
                      title_justify="center", width=50)
        table.add_column("S.No", style="cyan", no_wrap=True)
        table.add_column("Game Mode", style="magenta")

        table.add_row("1", "Player Vs Computer")
        table.add_row("2", "MultiPlayer")

        console.print(Padding(table, pad=(2, 0, 1, 8)))

    @classmethod
    def show_select_symbol_screen(cls):
        table = Table(title="Select Symbol", title_justify="center", width=50)
        table.add_column("S.No", style="cyan", no_wrap=True)
        table.add_column("Symbol", style="magenta")

        table.add_row("1", "X")
        table.add_row("2", "O")

        console.print(Padding(table, pad=(2, 0, 1, 8)))

    @classmethod
    def fancy_print(cls, text):
        print("\t---------------------------------------------------")
        termcolor.cprint(
            f"\t|              {text}              |", color="white")
        print("\t---------------------------------------------------")

    @classmethod
    def show_player_info(cls, player):
        print("\t---------------------------------------------------")
        termcolor.cprint(
            f"\t|               Player Information                |", color="white")
        print("\t---------------------------------------------------")
        print(emoji.emojize(
            "                   \tPlayer X :heavy_equals_sign:  " + str(player.X)))
        print(emoji.emojize(
            "                   \tPlayer O :heavy_equals_sign:  " + str(player.O)))
        print("\t---------------------------------------------------\n")

    @classmethod
    def show_player_info_multiplayer(cls, player1, player2):
        print("\t---------------------------------------------------")
        termcolor.cprint(
            f"\t|               Player Information                |", color="white")
        print("\t---------------------------------------------------")
        print(emoji.emojize(
            "                   \tPlayer X :heavy_equals_sign:  " + str(player1.X)))
        print(emoji.emojize(
            "                   \tPlayer O :heavy_equals_sign:  " + str(player2.O)))
        print("\t---------------------------------------------------\n")

    @classmethod
    def show_board(cls, map_value, player_name, board_values, final):
        if final == None:
            termcolor.cprint(
                f"\n\tCurrent Player: {player_name}\n", color="yellow")
        else:
            termcolor.cprint(
                f"\n\tFinal Result: {player_name}\n", color="yellow")

        termcolor.cprint("\n\tCurrent State Of Board : \n\n", color="green")
        print("\n")
        termcolor.cprint("\t     |     |", color="white")
        print_formatted_text(HTML("\t  {}  |  {}  |  {}".format(map_value.get(
            board_values[0]), map_value.get(board_values[1]), map_value.get(board_values[2]))))
        termcolor.cprint('\t_____|_____|_____', color="white")
        termcolor.cprint("\t     |     |", color="white")
        print_formatted_text(HTML("\t  {}  |  {}  |  {}".format(map_value.get(
            board_values[3]), map_value.get(board_values[4]), map_value.get(board_values[5]))))
        termcolor.cprint('\t_____|_____|_____', color="white")
        termcolor.cprint("\t     |     |", color="white")
        print_formatted_text(HTML("\t  {}  |  {}  |  {}".format(map_value.get(
            board_values[6]), map_value.get(board_values[7]), map_value.get(board_values[8]))))
        termcolor.cprint("\t     |     |", color="white")
        print("\n")
