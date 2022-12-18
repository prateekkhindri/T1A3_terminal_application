import os
from lib.models.game import Game
from lib.utils.constants import history


def main():
    if not os.path.exists(history):
        os.mkdir(history)
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
