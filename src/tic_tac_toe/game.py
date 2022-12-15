import termcolor
from constants import style, game_mode_options, title, json_file_name, multi_json_file_name
from prompt_toolkit.shortcuts import yes_no_dialog
from lib.display import Display
from board import Board
from lib.ai import AI
from lib.utils import Utils


class Game:
    def __init__(self):
        self.board = None
        self.game_result = None
        self.game_mode_choice = None

    def start(self):
        start_game = self.welcome_screen()
        if start_game:
            self.game_mode_choice = self.select_game_mode()
            self.board = Board(self.game_mode_choice)
            self.game_result = self.board.play(self.game_mode_choice)
            decision = AI.make_decision(self.game_result)
            if Utils.ask_save() == "yes":
                termcolor.cprint(
                    "\n\tSuccessfully saved user data in the data directory", color="green")

            if self.game_mode_choice == 1:
                Utils.save_json(
                    name=json_file_name,
                    data=self.game_result.computer_json_data,
                    decision=decision,
                    key=self.game_result.player.name,
                    player=self.game_result.current_player_symbol)
            elif self.game_mode_choice == 2:
                Utils.save_multi_data_json(
                    name=multi_json_file_name,
                    data=self.game_result.multi_json_data,
                    decision=decision,
                    user1=self.game_result.player2.name,
                    user2=self.game_result.player1.name)

    def welcome_screen(self):
        return yes_no_dialog(
            title='UNBEATABLE TIC TAC TOE',
            text='Created by Prateek Khindri\n\nWould you like to play a game?', style=style
        ).run()

    def select_game_mode(self):
        Display.show_game_mode_select_screen()

        user_option = Display.rich_input(
            "\n\tSelect a mode from the options above", game_mode_options
        )

        return int(user_option)
