from connect4code import *

reset_board()
display_board()
player = "X"
while True:
    print()
    print("Player", player, "is up next.")
    selection = input("Enter an number from 1 to 7: ")
    selection = int(selection)
    drop_token(player, selection)
    print()
    display_board()
    winner = do_we_have_a_win(player)
    if winner:
        print()
        print("Congrats! Player", player, "wins!!!!")
        print()
        break
    if player == "X":
        player = "O"
    else:
        player = "X"

