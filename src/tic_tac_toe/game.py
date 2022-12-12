from constants import style
from prompt_toolkit.shortcuts import yes_no_dialog


class Game:
    def __init__(self):
        pass

    def start(self):
        self.welcome_screen()

    def welcome_screen(self):
        return yes_no_dialog(
            title='Welcome to Tic Tac Toe ',
            text='Created by Prateek Khindri\n\nWould you like to play a game?', style=style
        ).run()
