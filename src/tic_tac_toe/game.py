from constants import style, game_mode_options, title
from prompt_toolkit.shortcuts import yes_no_dialog
from lib.display import Display


class Game:
    def __init__(self):
        self.game_mode_choice = None

    def start(self):
        start_game = self.welcome_screen()
        if start_game:
            self.game_mode_choice = self.select_game_mode()

    def welcome_screen(self):
        return yes_no_dialog(
            title='Welcome to Tic Tac Toe ',
            text='Created by Prateek Khindri\n\nWould you like to play a game?', style=style
        ).run()

    def select_game_mode(self):
        Display.show_game_mode_select_screen()

        user_option = Display.rich_input(
            "\n\tSelect a mode from the options above", game_mode_options
        )

        return int(user_option)
