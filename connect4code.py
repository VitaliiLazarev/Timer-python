from diagonals import extract_four_element_diagonals


board = (7, 6)
cols, rows = board
the_board = []


def reset_board():
    for i in range(rows):
        the_board.append([])
        for j in range(cols):
            the_board[i].append(" ")


def drop_token(user_token, column):
    inserted = False
     
    for row in range(rows):
        if the_board[row][column-1] == " ":
            the_board[row][column-1] = user_token
            return True
    return False


def display_board():
    for row in reversed(the_board):
        print(row)


def do_we_have_a_win(player_token, size=4):
    looking_for = player_token*size
    # Checks for a horizontal win.
    for i in range(6):
        if looking_for in "".join(the_board[i]):
            return True
    # Checks for a vertical win.
    for column_id in range(7):
        values = []
        for i in range(6):
            values.append(the_board[i][column_id])
        if looking_for in "".join(values):
            return True
    # Checks for a win on any of the diagonals.
    fours = extract_four_element_diagonals(the_board)
    four_strings = ["".join(d) for d in fours]
    if looking_for in four_strings:
        return True
    # If we get here, there is no winning combination.
    return False


    
