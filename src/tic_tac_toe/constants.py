from prompt_toolkit.styles import Style
from rich.console import Console


title = 'Tic Tac Toe'


game_mode_options = ["1", "2"]


symbol_options = ["1", "2"]


color = {
    "x": "green",
    "o": "yellow",
    "text": "white",
}

text_color = {
    "input_text": "bold green"
}

style = Style.from_dict({
    'dialog':             'bg:#b7bcbd',
    'dialog frame.label': 'bg:#ffffff #5af542',
    'dialog.body':        'bg:#000000 #00ff00',
})

console = Console()

player_symbol = {
    1: "X",
    2: "O"
}
