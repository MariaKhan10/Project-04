import random

def play():
    user = input("Whats your choice ? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a Tie"
    
    if is_win(user, computer):
        return "You won"
    
    return "You Lost"


def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player  == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())    
