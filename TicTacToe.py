def print_board(board): #print board
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_win(board, player): #check if player has won
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

def check_if_string_has_only_numbers(string): #check if string is an integer
    for char in string:
        if not char.isdigit():
            return False
    return True

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0] 
    while True: #game loop
        print_board(board) #print board
        row = input("Enter row (1-3): ") #ask for row
        #check if it is a valid row and if it is an integer
        while not check_if_string_has_only_numbers(row) or int(row) < 1 or int(row) > 3: #check if it is a valid row
            print('Invalid row') #print error message
            row = input("Enter row (1-3): ") #ask for row again
        row = int(row) - 1 #subtract 1 to account for 0 indexing
        col = input("Enter column (1-3): ") #ask for column
        #check if it is a valid column and if it is an integer
        while not check_if_string_has_only_numbers(col) or int(col) < 1 or int(col) > 3: #check if it is a valid column
            print('Invalid column')  #print error message
            col = input("Enter column (1-3): ") #ask for column again
        col = int(col) - 1 #subtract 1 to account for 0 indexing
        if board[row][col] == " ":#check if space is taken  
            board[row][col] = current_player #place piece
            if check_win(board, current_player):#check if win
                print_board(board) #print board
                print(current_player + " wins!") #print winner
                break #end game
            if all(" " not in row for row in board): #check if tie
                print_board(board) #print board
                print("Tie!") #print tie
                break #end game
            current_player = players[(players.index(current_player) + 1) % 2] #switch players
        else: #space is taken
            print("That space is taken. Try again.") #print error message

tic_tac_toe() #start game
