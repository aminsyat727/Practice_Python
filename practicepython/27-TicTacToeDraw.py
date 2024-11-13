import pandas as pd


def p1_move(board):
    row, col = map(int, input("Please state the coordinate you want to place your mark: " ).split())
    if row > 3 or col > 3:
        print("Invalid coordinate, please select in between 3x3 coordinates: ")
        row, col = map(int, input("Please state the coordinate you want to place your mark: " ).split())
    else:
        pass

    if board[row-1][col-1] == 0:
        board[row-1][col-1] = 'X'
    elif board[row-1][col-1] != 0:
        print("Invalid coordinate, please choose another coordinate!")
        p1_move(board)
    
    return board


def p2_move(board):
    row, col = map(int, input("Please state the coordinate you want to place your mark: " ).split())
    if row > 3 or col > 3:
        print("Invalid coordinate, please select in between 3x3 coordinates: ")
        row, col = map(int, input("Please state the coordinate you want to place your mark: " ).split())
    else:
        pass

    if board[row-1][col-1] == 0:
        board[row-1][col-1] = 'O'
    elif board[row-1][col-1] != 0:
        print("Invalid coordinate, please choose another coordinate!")
        p2_move(board)
    
    return board

if __name__ =="__main__":

    default_board = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
    round = 0
    while round <= 3:
        print(p1_move(default_board))
        print(p2_move(default_board))
        round+=1
    
    print(p1_move(default_board))
    print("Game ends! no more valid moves")

