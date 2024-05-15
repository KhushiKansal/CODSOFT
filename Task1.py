# Ai tic tac toe 

import numpy as np
import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to evaluate the current board state
def evaluate_board(board):
    if check_winner(board, "X"):
        return 10
    elif check_winner(board, "O"):
        return -10
    else:
        return 0

# Function to find all possible next moves
def get_possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate_board(board)

    if score == 10 or score == -10:
        return score - depth, None

    if is_board_full(board):
        return 0, None

    if is_maximizing:
        best_score = -np.inf
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "X"
            score, _ = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = " "
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = np.inf
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "O"
            score, _ = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = " "
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move

# Function for AI move
def ai_move(board):
    _, move = minimax(board, 0, True, -np.inf, np.inf)
    return move

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_board_full(board):
        # Player move
        while True:
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "O"
                break
            else:
                print("Invalid move. Try again.")

        print_board(board)

        # Check if player wins
        if check_winner(board, "O"):
            print("You win!")
            return

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            return

        # AI move
        print("AI is thinking...")
        row, col = ai_move(board)
        board[row][col] = "X"
        print_board(board)

        # Check if AI wins
        if check_winner(board, "X"):
            print("AI wins!")
            return

# Start the game
play_game()