import os
import json


class Utils:
    @classmethod
    def get_key(cls, dict, val):
        for key, value in dict.items():
            if val == value:
                return key

    @classmethod
    def load_json(cls, name, data=None):
        if not os.path.exists("data/"):
            os.mkdir("data/")
        if not os.path.exists(os.path.join("data/", name)):
            f = open(os.path.join("data/", name), "w")
            json.dump(data, f, indent=4)
            f.close()

        f = open(os.path.join("data/", name))
        return json.load(f)

    @classmethod
    def save_json(cls, name, data, decision, key, player):
        if key not in data['player'].keys():
            data['player'][key] = {
                "wins": 0,
                "losses": 0,
                "draw": 0
            }

        if decision == 0:
            data['computer']['draw'] += 1
            data['player'][key]['draw'] += 1
        elif decision == player:
            data['player'][key]['wins'] += 1
            data['computer']['losses'] += 1
        else:
            data['player'][key]['losses'] += 1
            data['computer']['wins'] += 1

        with open(f"data/{name}", "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def save_multi_data_json(cls, name, data, decision, user1, user2):
        if user1 not in data['player'].keys():
            data['player'][user1] = {
                "wins": 0,
                "losses": 0,
                "draw": 0
            }
        if user2 not in data['player'].keys():
            data['player'][user2] = {
                "wins": 0,
                "losses": 0,
                "draw": 0
            }

        if decision == 0:
            data['player'][user1]['draw'] += 1
            data['player'][user2]['draw'] += 1
        elif decision == 2:
            data['player'][user1]['wins'] += 1
            data['player'][user2]['losses'] += 1
        else:
            data['player'][user1]['losses'] += 1
            data['player'][user2]['wins'] += 1

        with open(f"data/{name}", "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def write_session_file(cls, session_file, player_name, map_value_file, board_values):
        session_file.write(f"\tCurrent Player: {player_name}\n")
        session_file.write("\n\tCurrent State Of Board :\n")
        session_file.write("\t     |     |\n")
        session_file.write("\t  {}  |  {}  |  {}\n".format(map_value_file.get(
            board_values[0]), map_value_file.get(board_values[1]), map_value_file.get(board_values[2])))
        session_file.write('\t_____|_____|_____\n')
        session_file.write("\t     |     |\n")
        session_file.write("\t  {}  |  {}  |  {}\n".format(map_value_file.get(
            board_values[3]), map_value_file.get(board_values[4]), map_value_file.get(board_values[5])))
        session_file.write('\t_____|_____|_____\n')
        session_file.write("\t     |     |\n")
        session_file.write("\t  {}  |  {}  |  {}\n".format(map_value_file.get(
            board_values[6]), map_value_file.get(board_values[7]), map_value_file.get(board_values[8])))
        session_file.write("\t     |     |\n")
        session_file.write("\n")

    @classmethod
    def clear(cls):
        # For windows
        if os.name == 'nt':
            os.system('cls')

        # For mac and linux(os name is posix)
        else:
            os.system('clear')
