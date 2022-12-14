import termcolor
from lib.utils.utils import Utils


class AI:
    @classmethod
    def analyze_board(cls, board):
        cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
              [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for i in range(0, 8):
            if (board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]):
                return board[cb[i][2]]
        return 0

    @classmethod
    def minimax(cls, board, player):
        x = cls.analyze_board(board)
        if (x != 0):
            return (x*player)
        pos = -1
        value = -2
        for i in range(0, 9):
            if (board[i] == 0):
                board[i] = player
                score = -cls.minimax(board, (player*-1))
                if (score > value):
                    value = score
                    pos = i
                board[i] = 0

        if (pos == -1):
            return 0
        return value

    @classmethod
    def make_decision(cls, board):
        x = cls.analyze_board(board.board_array)

        if (x == 0):
            player_name = None
            board.display_board(player_name, final=1)
            termcolor.cprint("\n\tTie!!!", color="yellow")
            if board.session_file is not None:
                board.session_file.write("\tTie!!!\n")
                board.session_file.close()
            return 0

        if (x == Utils.get_key(board.map_value_file, 'X')):
            winner = board.player1 if board.game_mode == 2 else board.player
            board.display_board(winner.name, final=1)
            termcolor.cprint("\n\t{} wins".format(winner.X), color="green")
            if board.session_file is not None:
                board.session_file.write("\n\t{} wins".format(winner.X))
                board.session_file.close()
            return 1

        if (x == Utils.get_key(board.map_value_file, 'O')):
            winner = board.player2 if board.game_mode == 2 else board.player
            board.display_board(winner.name, final=1)
            termcolor.cprint("\n\t{} wins".format(winner.O), color="green")
            board.session_file.write("\n\t{} wins".format(winner.O))
            board.session_file.close()
            return 2
