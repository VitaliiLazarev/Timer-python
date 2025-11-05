from flask import Flask, render_template
import connect4_logic as game

app = Flask(__name__)

current_player = "X"
game_over = False
last_message = "Player X's turn"

@app.route("/")
def index():
    """ Init page load """
    global current_player, game_over, last_message
    game.reset_board()
    current_player = "X"
    game_over = False
    last_message = "Player X's turn"
    
    return render_template(
        "index.html",
        board = game.the_board,
        player = current_player,
        message = last_message,
        game_over = game_over,
        cols = game.COLS,
        rows = game.ROWS,
    )

@app.route("/drop/<int:col>", methods=["POST"])
def drop(col: int):
    """ Handle move in column 'col' (0 - start) """
    global current_player, game_over, last_message

    if not game_over:
        if game.drop_token(current_player, col):
            # Check for win
            if game.check_win(current_player):
                game_over = True
                last_message = f"Player {current_player} wins! Play again?"
            #Check for draw
            elif game.is_draw():
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
        board = game.the_board,
        player = current_player,
        message = last_message,
        game_over = game_over,
        cols = game.COLS,
        rows = game.ROWS,
    )

@app.post("/reset")
def reset():
    """ Reset the board and start a new game """
    global current_player, game_over, last_message
    game.reset_board()
    current_player = "X"
    game_over = False
    last_message = "New game! Player X starts"
    
    return render_template(
        "board.html",
        board = game.the_board,
        player = current_player,
        message = last_message,
        game_over = game_over,
        cols = game.COLS,
        rows = game.ROWS,
    )

if __name__ == "__main__":
    app.run(debug = True)





    

























                