# Function to display the board---- display_board(board)
# Function for taking input-------- player_input()
# Function to assign the position---- place_marker(board, marker, position)
# function that takes in a board and a mark (X or O)-- win_check(board,mark)
# function that uses the random module to randomly decide which player goes first-- choose_first()
# function that returns a boolean indicating whether a space on the board is freely available-- space_check(board, position)
# function that checks if the board is full and returns a boolean value. True if full, False otherwise-- full_board_check(board)

# function that asks for a player's next position (as a number 1-9) and then uses the function
#  from step 6 to check if it's a free position-- player_choice(board)

# function that asks the player if they want to play again and returns a boolean True if they do want to play again.
# --  def replay():
    

    


# TODO: Function to display the board
def display_board(board):
    a1 = board[1]
    a2 = board[2]
    a3 = board[3]
    a4 = board[4]
    a5 = board[5]
    a6 = board[6]
    a7 = board[7]
    a8 = board[8]
    a9 = board[9]
    print("  |   | ")
    print(f"{a1} | {a2} | {a3} ")
    print("  |   | ")
    print('----------')
    print("  |   | ")
    print(f"{a4} | {a5} | {a6} ")
    print("  |   | ")
    print('----------')
    print("  |   | ")
    print(f"{a7} | {a8} | {a9} ")
    print("  |   | ")


# TODO: Function for taking input 
def player_input():
    while True:
        player_entry = int(input("Player 1: Enter 1 for X and 2 for O: "))
        if player_entry == 2 or player_entry ==1:
            break
    if player_entry == 1:
        p_input = ('X','O')
    else:
        p_input = ('O','X')
    return p_input



# TODO: Function to assign the position 
def place_marker(board, marker, position):
    board[position]=marker


# TODO: function that takes in a board and a mark (X or O)
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# TODO: function that uses the random module to randomly decide which player goes first.
def choose_first():
    import random
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# TODO: function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

# TODO: function that checks if the board is full and returns a boolean value. True if full, False otherwise
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# TODO: function that asks for a player's next position (as a number 1-9) and then uses the function
#  from step 6 to check if it's a free position

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

# TODO: function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

