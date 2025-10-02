import math

# Initialize board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(b):
    for row in b:
        print('|'.join(row))
        print('-' * 5)

# Check if any moves are left
def is_moves_left(b):
    return any(cell == ' ' for row in b for cell in row)

# Evaluate the board
def evaluate(b):
    for i in range(3):
        # Rows
        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return 10 if b[i][0] == 'X' else -10
        # Columns
        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return 10 if b[0][i] == 'X' else -10
    # Diagonals
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return 10 if b[0][0] == 'X' else -10
    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return 10 if b[0][2] == 'X' else -10
    return 0

# Minimax with Alpha-Beta Pruning
def minimax(b, depth, is_max, alpha, beta):
    score = evaluate(b)

    # Terminal state
    if score != 0 or not is_moves_left(b):
        return score

    if is_max:  # AI's turn
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = 'X'
                    eval_val = minimax(b, depth + 1, False, alpha, beta)
                    b[i][j] = ' '
                    max_eval = max(max_eval, eval_val)
                    alpha = max(alpha, eval_val)
                    if beta <= alpha:
                        break
        return max_eval
    else:  # Human's turn
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = 'O'
                    eval_val = minimax(b, depth + 1, True, alpha, beta)
                    b[i][j] = ' '
                    min_eval = min(min_eval, eval_val)
                    beta = min(beta, eval_val)
                    if beta <= alpha:
                        break
        return min_eval

# Find best move for AI
def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'X'
                move_val = minimax(b, 0, False, -math.inf, math.inf)
                b[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Play the game
def play():
    print("You are O, AI is X. Let's play!")
    while True:
        print_board(board)
        if evaluate(board) != 0 or not is_moves_left(board):
            break

        # Human move
        try:
            row = int(input("Enter your move row (0–2): "))
            col = int(input("Enter your move col (0–2): "))
        except ValueError:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        # AI move
        if is_moves_left(board) and evaluate(board) == 0:
            ai_move = find_best_move(board)
            board[ai_move[0]][ai_move[1]] = 'X'

    # Final state
    print_board(board)
    final_score = evaluate(board)
    if final_score == 10:
        print("AI Wins!")
    elif final_score == -10:
        print("You Win!")
    else:
        print("It's a Draw!")

# Run the game
if __name__ == "__main__":
    play()
