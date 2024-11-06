def is_safe(board, row, col):
    """
    Check if it's safe to place a queen on the board at the given row and column.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    """
    Solve the N-Queens problem using backtracking.
    
    Parameters:
    n (int): The number of queens to place on the board.
    
    Returns:
    list: The final configuration of the board with the queens placed.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    def backtrack(col):
        if col == n:
            return True
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                
                if backtrack(col + 1):
                    return True
                
                board[i][col] = 0
        
        return False
    
    if backtrack(0):
        return board
    
    return []

# Get user input for the number of queens
n = int(input("Enter the number of queens: "))
print(solve_n_queens(n))
