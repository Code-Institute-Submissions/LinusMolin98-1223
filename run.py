import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

def place_ship(board, ship_size):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board) - ship_size)
        else:
            row = random.randint(0, len(board) - ship_size)
            col = random.randint(0, len(board) - 1)

        ship_coordinates = []

        for i in range(ship_size):
            if orientation == 'horizontal':
                ship_coordinates.append((row, col + i))
            else:
                ship_coordinates.append((row + i, col))

        # Check if the chosen coordinates are valid
        valid = all(board[row][col] == 'O' for row, col in ship_coordinates)
        if valid:
            for row, col in ship_coordinates:
                board[row][col] = 'S'
            break
def player_turn(board):
    while True:
        try:
            guess_row = int(input("Guess Row (0 to {}): ".format(len(board) - 1)))
            guess_col = int(input("Guess Col (0 to {}): ".format(len(board) - 1)))
            if 0 <= guess_row < len(board) and 0 <= guess_col < len(board):
                return guess_row, guess_col
            else:
                print("Invalid input. Please enter valid row and column numbers.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")        