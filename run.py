from random import randint

CHOOSE_BOARD = [[" "] * 8 for x in range(8)]
PLAYER_BOARD = [[" "] * 8 for i in range(8)]
SHIP_LENGTHS = [2, 3, 3, 4, 5]

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

def place_ship(board):
    for ship_length in SHIP_LENGTHS:
        while True:
            if board == CHOOSE_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if fit_ship_check(ship_length, row, column, orientation):


def fit_ship_check(SHIP_LENGTHS, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTHS > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTHS > 8:
            return False
        else:
            return True


def create_ships(board):
    """
    Computer randomly generates 5 ships 
    """
    for ship in range(5):
        ship_row, ship_column = (randint(0, 7), randint(0, 7))
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


def hit_count(board):
    """
    Checks if all the ships have been sunk
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    create_ships(CHOOSE_BOARD)
    turns = 10
    while turns > 0:
        print('Guess the battleship co-ordinates')
        print_board(PLAYER_BOARD)
        row, column = player_ship_loc()
        if PLAYER_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif CHOOSE_BOARD[row][column] == "X":
            print("Great Hit")
            PLAYER_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("Ah just saltwater")
            PLAYER_BOARD[row][column] = "-"   
            turns -= 1     
        if hit_count(PLAYER_BOARD) == 5:
            print("Aboslutely, fantastic we got them all")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns") 
