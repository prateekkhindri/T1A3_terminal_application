from rich.highlighter import Highlighter


class RainbowHighlighter(Highlighter):
    def highlight(self, text, color=None):
        for index in range(len(text)):
            text.stylize(f"color(212)", index, index + 1)


rainbow = RainbowHighlighter()
