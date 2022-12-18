from lib.utils.utils import Utils


def test_get_key():
    map_value_file = {1: 'X', 2: 'O'}
    assert Utils.get_key(map_value_file, 'X') == 1


def test_get_key2():
    map_value_file = {1: 'X', 2: 'O'}
    assert Utils.get_key(map_value_file, 'O') == 2
