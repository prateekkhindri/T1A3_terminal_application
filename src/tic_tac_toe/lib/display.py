import termcolor
import rich
import emoji
from rich.table import Table
from rich.padding import Padding
from rich.prompt import Prompt
from constants import console, text_color


class Display:
    @classmethod
    def rich_input(self, text, options):
        text = rich.text.Text(text, style=text_color.get('input_text'))
        return Prompt.ask(text, choices=options)

    @classmethod
    def show_game_mode_select_screen(self):
        print("\t---------------------------------------------------")
        termcolor.cprint(
            "\t|        Welcome To Unbeatable Tictactoe          |", color="white", attrs=["bold"])
        print("\t---------------------------------------------------")
        print("\t              Developed with 💜 by ", end=" ")
        termcolor.cprint("\n\n                        Prateek Khindri",
                         color="green", attrs=["bold"])
        print("\t---------------------------------------------------\n")

        table = Table(title="Select Game Mode",
                      title_justify="center", width=50)
        table.add_column("S.No", style="cyan", no_wrap=True)
        table.add_column("Game Mode", style="magenta")

        table.add_row("1", "Player Vs Computer")
        table.add_row("2", "MultiPlayer")

        console.print(Padding(table, pad=(2, 0, 1, 8)))

    @classmethod
    def show_select_symbol_screen():
        table = Table(title="Select Symbol", title_justify="center", width=50)
        table.add_column("S.No", style="cyan", no_wrap=True)
        table.add_column("Symbol", style="magenta")

        table.add_row("1", "X")
        table.add_row("2", "O")

        console.print(Padding(table, pad=(2, 0, 1, 8)))

    @classmethod
    def fancy_print(self, text):
        print("\t---------------------------------------------------")
        termcolor.cprint(
            f"\t|              {text}              |", color="white")
        print("\t---------------------------------------------------")

    @classmethod
    def show_player_info(self, player, mode):
        print("\t---------------------------------------------------")
        termcolor.cprint(
            f"\t|                      {mode}                 |", color="white")
        print("\t---------------------------------------------------")
        print(emoji.emojize(
            "\tPlayer X :heavy_equals_sign: " + str(player.X)+""))
        print(emoji.emojize("\tPlayer O :heavy_equals_sign: "+str(player.O)))
        print("\t---------------------------------------------------\n")
