from random import randint

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

def create_ships(board):
    """
    Computer randomly generates 5 ships 
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, len(board) - 1)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = #player_ship_location()
        board[ship_row][ship_column] = "X"