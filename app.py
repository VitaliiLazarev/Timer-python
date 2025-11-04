from flask import Flask, render_template
from connect4_logic import (
    the_board,
    reset_board,
    drop_token,
    check_win,
    is_draw,
    COLS,
    ROWS,
)

app = Flask(__name__)

current_player = "X"
game_over = False
last_message = "Player X's turn"

@app.route("/")
def index():
    """ Init page load """
    global current_player, game_over, last_message
    reset_board()
    current_player = "X"
    game_over = False
    last_message = "Player X's turn"
    return render_template(
        "index.html",
        board = the_board,
        player = current_player,
        message = last_message,
        game_over = game_over,
        cols = COLS,
        rows = ROWS,
    )

@app.route("/drop/<int:col>", methods=["POST"])
def drop(col: int):
    """ Handle move in column 'col' (0 - start) """
    global current_player, game_over, last_message

    if not game_over:
        if drop_token(current_player, col):
            # Check for win
            if check_win(current_player):
                game_over = True
                last_message = f"Player {current_player} wins! Play again?"
            #Check for draw
            elif is_draw():
                game_over = True
                last_message = "It's a draw! Play again?"
            else:
                # Switch player
                current_player = "O" if current_player == "X" else "X"
                last_message = f"Player {current_player}'s turn"
        else:
            last_message = "That column is full. Try another one."

    return render_template(
        "board.html",
        board = the_board,
        player = current_player,
        message = last_message,
        game_over = game_over,
        cols = COLS,
        rows = ROWS,
    )

@app.post("/reset")
def reset():
    """ Reset the board and start a new game """
    global current_player, game_over, last_message
    reset_board()
    current_player = "X"
    game_over = False
    last_message = "New game! Player X starts"
    return render_template(
        "board.html",
        board = the_board,
        player = current_player,
        message = last_message,
        game_over = game_over,
        cols = COLS,
        rows = ROWS,
    )

if __name__ == "__main__":
    app.run(debug = True)





    

























                