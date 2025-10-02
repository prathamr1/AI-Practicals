def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True

# Utility to print board
def print_board(board):
    print("\nSolution:")
    for row in board:
        print(" ".join('Q' if col == 1 else '.' for col in row))
    print()

# Recursive Backtracking Solver with optional Branch and Bound
def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

# Main function
def n_queens_csp(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print(f"Total Solutions for {n}-Queens: {len(solutions)}")

# Run the solver
if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N (e.g., 4, 8): "))
        if n < 1:
            print("N must be at least 1.")
        else:
            n_queens_csp(n)
    except ValueError:
        print("Please enter a valid integer.")
