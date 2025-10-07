from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Grid
from textual.widgets import Button, Static, Header, Footer

COLS, ROWS = 6, 7

class Cell (Static)
    def set_token(self, t: str):
        self.update(t if t != " " else " ")
        self.remove_class("x")
        self.remove_class("o")
        self.remove_class("empty")
        self.add_class("x" if t == "X" else "o" if t == "O" else "empty")

class Connect4App(App):
    CSS_PATH = "connect4.tcss"
    BINDINGS = [
        ("r", "reset", "Reset board"),
        ("1", "drop(0)", "Drop 1"),
        ("2", "drop(1)", "Drop 2"),
        ("3", "drop(2)", "Drop 3"),
        ("4", "drop(3)", "Drop 4"),
        ("5", "drop(4)", "Drop 5"),
        ("6", "drop(5)", "Drop 6"),
        ("7", "drop(6)", "Drop 7"),
    ]