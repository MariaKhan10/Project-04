from player import Player

def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board, symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == symbol for i in condition) for condition in win_conditions)

def is_draw(board):
    return all(cell != ' ' for cell in board)

def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!\n")
    player1 = Player(input("Enter name for Player 1 (X): "), 'X')
    player2 = Player(input("Enter name for Player 2 (O): "), 'O')
    current_player = player1

    while True:
        display_board(board)
        move = current_player.get_move(board)
        board[move] = current_player.symbol

        if check_winner(board, current_player.symbol):
            display_board(board)
            print(f"Congratulations {current_player.name}! You have won the game.")
            break
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    play_game()
