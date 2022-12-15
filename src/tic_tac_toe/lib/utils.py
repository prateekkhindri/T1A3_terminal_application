import os
import json
import termcolor


class Utils:
    @classmethod
    def get_key(self, dict, val):
        for key, value in dict.items():
            if val == value:
                return key

    @classmethod
    def load_json(self, name, data=None):
        if not os.path.exists("data/"):
            os.mkdir("data/")
        if not os.path.exists(os.path.join("data/", name)):
            f = open(os.path.join("data/", name), "w")
            json.dump(data, f, indent=4)
            f.close()

        f = open(os.path.join("data/", name))
        return json.load(f)

    @classmethod
    def save_json(self, name, data, decision, key, player):
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
