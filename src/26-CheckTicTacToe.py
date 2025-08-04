import numpy as np

def row_win(game_table):
    for row in game_table:
        if 0 in row:
            pass
        elif sum(row) == 3:
            return 1
        elif sum(row) == 6:
            return 2
        
    return None

def column_win(game_table):
#use the same method as row, but transpose the list first using numpy.transpose()
    tp_game_table = np.transpose(game_table)
    for col in tp_game_table:
        if 0 in col:
            pass
        elif sum(col) == 3:
            return 1
        elif sum(col) == 6:
            return 2
        
    return None
        
def diagonal_win(game_table):
    lr = [game_table[i][i] for i in range(3)]
    rl = [game_table[i][2-i] for i in range(3)]

    if sum(lr) == 3 and 0 not in lr:
        return 1
    elif sum(lr) == 6 and 0 not in lr:
        return 2
    elif sum(rl) == 3 and 0 not in rl:
        return 1
    elif sum(rl) == 6 and 0 not in rl:
        return 2
    
    return None

def check_winner(tictactoe):
    winner_check = row_win(tictactoe)
    if winner_check is None:
        winner_check = column_win(tictactoe)
    if winner_check is None:
        winner_check = diagonal_win(tictactoe)
    
    if winner_check is None:
        return "The game is a draw."
    else:
        return f"The winner is Player {winner_check}"

if __name__ == "__main__":
# Test case: Player 1 wins by filling the top row
    tictactoe1 = [
        [0, 2, 0],
        [2, 2, 2],
        [2, 0, 0]
    ]

    # Test case: Player 2 wins by filling the first column
    tictactoe2 = [
        [2, 1, 1],
        [2, 1, 0],
        [0, 1, 0]
    ]

    # Test case: Player 1 wins by filling the left-to-right diagonal
    tictactoe3 = [
        [2, 0, 2],
        [0, 2, 2],
        [2, 0, 2]
    ]

    # Test case: Player 2 wins by filling the right-to-left diagonal
    tictactoe4 = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 0, 0]
    ]

    # Test case: No winner (Draw)
    tictactoe5 = [
        [1, 2, 1],
        [2, 1, 2],
        [2, 1, 2]
    ]

print("Test Case 1 Result:", check_winner(tictactoe1))  # Expected: The winner is Player 1
print("Test Case 2 Result:", check_winner(tictactoe2))  # Expected: The winner is Player 2
print("Test Case 3 Result:", check_winner(tictactoe3))  # Expected: The winner is Player 1
print("Test Case 4 Result:", check_winner(tictactoe4))  # Expected: The winner is Player 2
print("Test Case 5 Result:", check_winner(tictactoe5))  # Expected: The game is a draw.            
            