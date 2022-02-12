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

letters_conversion = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

def create_ships(board):
    """
    Computer randomly generates 5 ships 
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, len(board) - 1)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = player_ship_loc()
        board[ship_row][ship_column] = "X"

def player_ship_loc():
    """
    Player chooses where to place their 5 ships
    """
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_conversion[column]
