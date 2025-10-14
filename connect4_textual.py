from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Grid
from textual.widgets import Button, Static, Header, Footer

COLS, ROWS = 7, 6

class Cell (Static):
    def set_token(self, t: str):
        self.update(t if t != " " else " ")
        self.remove_class("x")
        self.remove_class("o")
        self.remove_class("empty")
        self.add_class("x" if t == "X" else "o" if t == "O" else "empty")

    async def on_click(self, event):
        if "available" in self.classes and self.id:
            _, r, c = self.id.split("-") 
            await self.app.action_drop(int(c))
        
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
            with Grid(id="board"):
                for r in range(ROWS - 1, -1, -1):
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
    
    async def action_drop(self, col: int):
        if self.drop_token(col):
            self.update_available_targets()
            if self.check_win(self.turn):
                self.sub_title = f"{self.turn} wins! (R to reset)"
                self.clear_available_targets()
            else:
                self.switch_turn()
                self.update_available_targets()

                
    def action_reset(self):
        self.board = [[" "] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c].set_token(" ")
        self.turn = "X"
        self.sub_title = f"Turn: {self.turn}"
        for b in self.query(Button):
            b.disabled = False
        self.update_available_targets()
    
    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id and event.button.id.startswith("col-"):
            col = int(event.button.id.split("-")[1])
            self.action_drop(col)

    def clear_available_targets(self):
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c].remove_class("available")

    def update_available_targets(self):
        self.clear_available_targets()
        for c in range(COLS):
            for r in range(ROWS):
                if self.board[r][c] == " ":
                    self.cells[r][c].add_class("available")
                    break

    def check_win(self, t: str, streak: int = 4) -> bool:
        # horizontal
        for r in range(ROWS):
            if t * streak in "".join(self.board[r]):
                return True
        # vertical
        for c in range(COLS):
            if t*streak in "".join(self.board[r][c] for r in range(ROWS)):
                return True
        # diagonal \
        for r in range(ROWS-3):
            for c in range(COLS - 3):
                if all(self.board[r + i][c + i] == t for i in range(4)):
                    return True
        # diagonal /
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(self.board[r-i][c+i] == t for i in range(4)):
                    return True
                        
    async def on_mount(self) -> None:
        self.update_available_targets()


    
if __name__ == "__main__":
        Connect4App().run()