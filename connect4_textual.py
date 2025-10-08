from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Grid
from textual.widgets import Button, Static, Header, Footer

COLS, ROWS = 6, 7

class Cell (Static):
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
    
    def __init__(self):
        super().__init__()
        # Matrix of cell
        self.board = [[" "] * COLS for _ in range(ROWS)]
        self.turn = "X"
        self.cells: list[list[Cell]] = [[None]*COLS for _ in range(ROWS)]
    
    # Build HUD of the game
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Vertical(id="root"):
            with Horizontal(id="controls"):
                for c in range(COLS):
                    yield Button(str(c+1), id=f"col-{c}", variant = "primary")
            with Grid(id="board"):
                for r in range(ROWS-1, -1, -1):
                    for c in range(COLS):
                        cell = Cell(" ", classes="cell empty", id=f"cell-{r}-{c}")
                        self.cells[r][c] = cell
                        yield cell
        yield Footer()
    
    # Game logic
    def drop_token(self, col:int) -> bool:
        if not (0 <= col < COLS):
            return False
        # find the first empty cell
        for r in range(ROWS):
            if self.board[r][col] == " ":
                self.board[r][col] = self.turn
                self.cells[r][col].set_token(self.turn)
                return True
            return False
    
    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"
        self.sub_title = f"Turn: {self.turn}"
    
    def action_drop(self, col: int):
        if self.drop_token(col):
            if self.check_win(self.turn):
                self.sub_title = f"{self.turn} wins! (R to reset)"
                for b in self.query(Button):
                    b.disabled = True
            else:
                self.switch_turn()
    
    def action_reset(self):
        self.board = [[" "] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c].set_token(" ")
            self.turn = "X"
            self.sub_title = f"Turn: {self.turn}"
            for b in self.query(Button):
                b.disabled = False
    
    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id and event.button.id.startswith("col-"):
            col = int(event.button.id.split("-")[1])
            self.action_drop(col)
    
    
if __name__ == "__main__":
        Connect4App().run()