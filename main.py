import numpy as np
import pygame
from math import floor
pygame.font.init()

rows, columns = 3, 3
square = 200
width = int(square * columns)
height = int(square * rows + square/2)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.SysFont('comicsans', 100)

def create_board():
    board = np.zeros((rows, columns))
    return board

def winning_move(board, piece, pos):
    # Horizontal winner
    for row in range(len(board)):
        for column in range(len(board)-2):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece:
                pos['start_pos'] = (10, row * square + square)
                pos['end_pos'] = (width-10, row * square + square)
                return True
    
    # Vertical winner
    for row in range(len(board)-2):
        for column in range(len(board)):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece:
                pos['start_pos'] = (column * square + square/2, square/2 + 10)
                pos['end_pos'] = (column * square + square/2, height-10)
                return True
    
    # Positively sloped diagonals
    for row in range(len(board)-2):
        for column in range(len(board)-2):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece:
                pos['start_pos'] = (column * square + 20, row * square + 20 + square/2)
                pos['end_pos'] = ((column+2) * square + square -20, (row+2) * square + square -20 + square/2)
                return True
    
    # Negatively sloped diagonals
    for row in range(2, len(board)):
        for column in range(len(board)-2):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece:
                pos['start_pos'] = (column * square + 20, row * square + square -20 + square/2)
                pos['end_pos'] = ((column+2) * square + square -20, (row-2) * square + 20 + square/2)
                return True

def check_draw(board):    
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                return False
    return True

def is_valid_position(board, row, column):
    return board[row][column] == 0

def draw_grid(board):
    for row in range(len(board)-1):
        # Horizontal lines
        pygame.draw.line(win, (128,128,128), (0, square + row * square + square/2), (width, square + row * square + square/2), 5)
        for column in range(len(board)-1):
            # Vertical lines
            pygame.draw.line(win, (128,128,128), (square + row * square, square/2), (square + row * square, height), 5)

def draw_board(board):
    for row in range(len(board)):
        for column in range(len(board)):
            pygame.draw.rect(win, (0,0,0), (column * square, row * square + square/2, square, square))

    for row in range(len(board)):
        for column in range(len(board)):
            x = column * square + square/2
            y = row * square + square
            if board[row][column] == 1:
                pygame.draw.line(win, (0,0,255), (x-70, y-70), (x+70, y+70), 25)
                pygame.draw.line(win, (0,0,255), (x-70, y+70), (x+70, y-70), 25)
            elif board[row][column] == 2:
                pygame.draw.circle(win, (255,0,0), (x, y), 80)
                pygame.draw.circle(win, (0,0,0), (x, y), 60)

def draw_window(board):
    draw_board(board)
    draw_grid(board)
    pygame.display.update()


def main():
    board = create_board()
    turn = 0
    pos = {}
    run = True
    draw = False

    pygame.draw.rect(win, (0,0,255), (0,0, width, square/2))
    player = font.render('Player 1', 1, (0,0,0))
    win.blit(player, (width/2 - player.get_width()/2, square/4 - player.get_height()/2))
    draw_window(board)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                x, y = event.pos
                row = int(floor((y-square/2)/square))
                column = int(floor(x/square))
                if turn == 0:
                    pygame.draw.rect(win, (255,0,0), (0,0, width, square/2))
                    player = font.render('Player 2', 1, (0,0,0))
                    win.blit(player, (width/2 - player.get_width()/2, square/4 - player.get_height()/2))
                    if is_valid_position(board, row, column):
                        board[row][column] = 1

                        if winning_move(board, 1, pos):
                            draw_board(board)
                            text = font.render('Player 1 Wins!', 1, (255,255,255))
                            color = (0,0,255)
                            run = False
                        elif check_draw(board):
                            run = False
                            draw = True
                else:
                    pygame.draw.rect(win, (0,0,255), (0,0, width, square/2))
                    player = font.render('Player 1', 1, (0,0,0))
                    win.blit(player, (width/2 - player.get_width()/2, square/4 - player.get_height()/2))
                    if is_valid_position(board, row, column):
                        board[row][column] = 2

                        if winning_move(board, 2, pos):
                            draw_board(board)
                            text = font.render('Player 2 Wins!', 1, (255,255,255))
                            color = (255,0,0)
                            run = False
                        elif check_draw(board):
                            run = False
                            draw = True
        
                draw_window(board)
                turn += 1
                turn %= 2

                if not run:
                    if draw:
                        text = font.render('Draw!', 1, (255,255,255))
                    else:
                        pygame.draw.line(win, color, (pos['start_pos'][0], pos['start_pos'][1]), (pos['end_pos'][0], pos['end_pos'][1]), 15)
                    win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
                    pygame.display.update()
                    pygame.time.wait(2000)

def first_screen():
    run = True

    while run:
        win.fill((0,0,0))
        text = font.render('Click to Play', 1, (255,255,255))
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        pygame.display.update()

first_screen()