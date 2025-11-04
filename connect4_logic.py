# Logic from connect4_textual without UI part

COLS,ROWS = 7,6
the_board = [[" "] * COLS for _ in range(ROWS)]

def reset_board():
    """Reset the board to empty spaces"""
    global the_board
    the_board = [[" "] * COLS for _ in range(ROWS)]

def drop_token(token: str, col: int) -> bool:
    """ Drop token ('X' or 'O') into the column (0-6) """
    if not (0 <= col < COLS):
        return False

    for r in range(ROWS):
        if the_board[r][col] == " ":
            the_board[r][col] = token
            return True
    return False

def check_win(t: str, streak: int = 4) -> bool:
    """ Check if player "t" has a winning line """
    # horizontal
    for r in range(ROWS):
        if t * streak in "".join(the_board[r]):
            return True

    # vertical
    for c in range(COLS):
        if t * streak in "".join(the_board[r][c] for r in range(ROWS)):
            return True

    # diagonal /
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(the_board[r + i][c + i] == t for i in range(streak)):
                return True

    # diagonal \
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(the_board[r - i][c + i] == t for i in range(streak)):
                return True

    return False
    
def is_draw() -> bool:
    """ True if the board is full and there is no winner """
    return all(cell != " " for row in the_board for cell in row)