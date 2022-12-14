

class Utils:
    classmethod

    def get_key(self, dict, val):
        for key, value in dict.items():
            if val == value:
                return key
