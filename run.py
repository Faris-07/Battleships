CHOOSE_BOARD = [[" "] * 8 for x in range(8)]
PLAYER_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):
    """
    Creates the battleship board
    """
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#print_board(PLAYER_BOARD)
