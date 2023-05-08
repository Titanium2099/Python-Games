import numpy as np
from colorama import init, Fore, Style

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#def print_board(board):
#    print(np.flip(board, 0))
def print_board(board):
    # Flip the board vertically to start from the bottom
    flipped_board = np.flip(board, 0)

    # Print the column indices
    print("  ", end="")
    for i in range(COLUMN_COUNT):
        print(Fore.BLUE + f" {i}  " + Style.RESET_ALL, end="")
    print()

    # Print the rows
    for r in range(ROW_COUNT):
        print(Fore.BLUE + " +" + "----+" * (COLUMN_COUNT - 1) + "----+" + Style.RESET_ALL)#print the top line
        #print(Fore.BLUE + f"{ROW_COUNT - r - 1}" + Style.RESET_ALL, end="") #print the row index
        for c in range(COLUMN_COUNT):
            piece = flipped_board[r][c]
            if piece == 0:
                #print(" |   ", end="")
                print(Fore.BLUE + " |   " + Style.RESET_ALL, end="")
            elif piece == 1:
                print(Fore.BLUE + " |" + Fore.RED + " X " + Style.RESET_ALL, end="")
            elif piece == 2:
                print(Fore.BLUE + " |" + Fore.YELLOW + " 0 " + Style.RESET_ALL, end="")
        print(Fore.BLUE + " |" + Style.RESET_ALL)

    # Print the bottom line
    print(Fore.BLUE + " +" + "----+" * (COLUMN_COUNT - 1) + "----+" + Style.RESET_ALL)
    #print("  " + "   ".join(["-" * 3] * COLUMN_COUNT))
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_game_over(board):
    print_board(board)
    print("Game Over!")

def connect_4():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        # Player 1 input
        if turn == 0:
            print("Player 1's turn")
            col = int(input("Make your selection (1-7): "))
            col -= 1
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                if winning_move(board, 1):
                    draw_game_over(board)
                    print("Player 1 wins!")
                    game_over = True

        # Player 2 input
        else:
            print("Player 2's turn")
            col = int(input("Make your selection (1-7): "))
            col -= 1
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                if winning_move(board, 2):
                    draw_game_over(board)
                    print("Player 2 wins!")
                    game_over = True

        print_board(board)

        # Switch turn
        turn += 1
        turn %= 2

        # Check for tie
        if np.count_nonzero(board == 0) == 0:
            draw_game_over(board)
            print("It's a tie!")
            game_over = True

connect_4()

