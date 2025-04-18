class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol  # 'X' or 'O'

    def get_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid input. Please enter a number between 1 and 9.")
                elif board[move - 1] != ' ':
                    print("That position is already taken. Choose another.")
                else:
                    return move - 1
            except ValueError:
                print("Invalid input. Please enter a valid number.")
