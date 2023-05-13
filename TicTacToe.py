def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False #no win

def check_if_string_has_only_numbers(string):
    for char in string:
        if not char.isdigit():
            return False
    return True

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]
    while True:
        print_board(board)
        row = input("Enter row (1-3): ")
        #check if it is a valid row and if it is an integer
        while not check_if_string_has_only_numbers(row) or int(row) < 1 or int(row) > 3:
            print('Invalid row')
            row = input("Enter row (1-3): ") 
        row = int(row) - 1 #subtract 1 to account for 0 indexing
        col = input("Enter column (1-3): ")
        #check if it is a valid column ds'klasndlkasdasdasdasdfefwgdinboasldfnsldfk'adsf'land if it is an integer
        while not check_if_string_has_only_numbers(col) or int(col) < 1 or int(col) > 3:
            print('Invalid column')
            col = input("Enter column (1-3): ")
        col = int(col) - 1 #subtract 1 to account for 0 indexing
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(current_player + " wins!")
                break
            if all(" " not in row for row in board):
                print_board(board)
                print("Tie!")
                break
            current_player = players[(players.index(current_player) + 1) % 2]
        else:
            print("That space is taken. Try again.")

tic_tac_toe()
