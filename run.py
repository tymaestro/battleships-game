""" Import randint from random module """

from random import randint


def create_board():
    """
    Create board
    """
    board = [["-" for x in range(6)] for y in range(6)]
    return board


player_board = create_board()
computer_board = create_board()


def print_board(board):
    """
    print_board function prints board and adds a pipe
    between each hyphen for clarity
    """
    for row in board:
        print(" | ".join(row))


def welcome(player):
    """
    welcome message for players
    """
    print(f"Welcome to Battleships {player}!")


def ship_placement(board):
    """
    Generate random ship locations
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        board[ship_row][ship_column] = "X"


def player_guess():
    """
    Player guesses
    """
    try:
        row = int(input("Please enter a row number: "))
        while row < 0 or row > 5:
            print("Oops, please choose a row between 0 and 5!")
            row = int(input("Please enter a row number: "))
        column = int(input("Please enter a column number: "))
        while column < 0 or column > 5:
            print("Oops, please choose a column between 0 and 5!")
            column = int(input("Please enter a column number: "))
    except ValueError:
        print("Please enter a valid number!")
        row = int(input("Please enter a row number: "))
    print(f"You chose the co-ordinates ({row}, {column})")
    return int(row), int(column)


def guess_check():
    """
    Function to validate player guesses
    """
    row, column = player_guess()
    if computer_board[row][column] == "#":
        print("Oops, you've already guessed those co-ordinates!")
    elif player_board[row][column] == "X":
        print("Congratulations, it's a direct hit!")
        computer_board[row][column] = "X"
    else:
        print("Sorry, you missed this time.\nPlease try again.")
        computer_board[row][column] = "#"


def increment_score(board):
    """
    Function to increment the score by 1 each time a ship is hit
    """
    score = 0
    for row in board:
        for column in row:
            if column == "X":
                score += 1
    print(f"You've hit {score} out of 5 battleships")
    return score


def start_game():
    """
    Start game function which calls the ship_placement function
    asks for name input, and calls welcome function
    """
    ship_placement(player_board)
    name = input("Ahoy Matey!\nPlease enter your name to continue: ")
    welcome(name)


def main():
    """
    This is the main function for starting the game
    """
    start_game()
    score = 5
    while score < 6:
        print("Please choose co-ordinates between 0 and 5")
        # print("\n\nPlayer Board\n")
        # print_board(player_board)
        print("\n\nComputer Board\n")
        print_board(computer_board)
        print("\n")
        guess_check()
        if increment_score(computer_board) == 5:
            print("Congratulations! You sunk all the Battleships!")
            break


if __name__ == "__main__":
    main()
