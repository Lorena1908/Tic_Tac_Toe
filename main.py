import numpy as np

rows, columns = 3, 3

def create_board():
    # board = [[0 for _ in range(columns)] for _ in range(rows)]
    board = np.zeros((rows, columns))
    return board

def make_tuple(string):
    return tuple(map(int, string.split(',')))

def winning_move(board, piece):
    # Horizontal winner
    for row in range(len(board)):
        for column in range(len(board)-2):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece:
                return True
    
    # Vertical winner
    for row in range(len(board)-2):
        for column in range(len(board)):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece:
                return True
    
    # Positively sloped diagonals
    for row in range(len(board)-2):
        for column in range(len(board)-2):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece:
                return True
    
    # Negatively sloped diagonals
    for row in range(2, len(board)):
        for column in range(len(board)-2):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece:
                return True

board = create_board()

turn = 0
print(board)
run = True
while run:
    if turn == 0:
        print("Player 1's turn")
        x, y = make_tuple(input('Enter a position: '))
        board[y][x] = 1

        if winning_move(board, 1):
            print('Player 1 wins!')
            run = False
    else:
        print("Player 2's turn")
        x, y = make_tuple(input('Enter a position: '))
        board[y][x] = 2

        if winning_move(board, 2):
            print('Player 2 wins!')
            run = False
    turn += 1
    turn %= 2
    print(board)