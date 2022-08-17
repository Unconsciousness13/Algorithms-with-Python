def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def set_queen(board):
    pass

def remove_queen(board):
    pass

def put_queens(row,board):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row,col):
            set_queen(row,col,board)
            put_queens(row +1 , board)
            remove_queen(row,col,board)

n = 8
board = []
[board.append(['-'] * n) for _ in range (8)]



put_queens(0,board)