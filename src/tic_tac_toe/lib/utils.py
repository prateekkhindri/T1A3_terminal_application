import os
import json


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
