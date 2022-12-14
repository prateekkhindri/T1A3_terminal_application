import time
import termcolor
from lib.utils.constants import style, game_mode_options, title, json_file_name, multi_json_file_name
from prompt_toolkit.shortcuts import yes_no_dialog, button_dialog, message_dialog
from lib.views.display import Display
from lib.models.board import Board
from lib.utils.ai import AI
from lib.utils.utils import Utils


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
            self.game_result = self.board.play()
            decision = AI.make_decision(self.game_result)
            if self.ask_save() == "yes":
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
            time.sleep(3)
            self.show_menu(decision)

    def show_menu(self, result="Game Over"):
        result = button_dialog(
            title='TicTacToe Game',
            text=f'Want to play again?',
            buttons=[
                ('New Game', True),
                ('Quit', False),
            ],
            style=style
        ).run()

        if result:
            Utils.clear()
            self.start()
        else:
            self.quit()

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

    def ask_save(self):
        while True:
            askForSave = input("\n\tSave User Data? [yes|no]:")
            if (askForSave == "yes"):
                break
            elif (askForSave == "no"):
                break
            else:
                termcolor.cprint(
                    "\n\tPlease select one of the available options", color="red")
                continue
        return askForSave

    def quit(self):
        message_dialog(
            title=title,
            text='Press ENTER to quit',
            style=style
        ).run()
        exit(0)
