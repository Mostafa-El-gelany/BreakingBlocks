import random


def count_colors(board, sz=10):
    red = 0
    blue = 0
    for i in range(sz):
        for j in range(sz):
            if board[i][j] == 1:
                red += 1
            elif board[i][j] == 2:
                blue += 1
    return red, blue


def randomize_board(sz=10):
    board = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        for j in range(sz):
            board[i][j] = random.randint(1, 2)
    return board


def print_list(board, sz=10):
    for i in range(sz):
        for j in range(sz):
            print(board[i][j], end='')
        print(' ')
    print('-------------------------------------')
