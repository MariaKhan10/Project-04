# mypy: ignore-errors

import random
Num_sides = 6


def roll_dice():
    dice1 : int = random.randint(1, Num_sides)
    dice2 : int = random.randint(1, Num_sides)
    total : int = dice1 + dice2
    print(total)

def main():
    dice1 : int = 10
    print(f"dice1 in main() start as {dice1}")
    roll_dice()    
    roll_dice()    
    roll_dice()   
    print(f"dice1 in main() {dice1}") 


if __name__ == "__main__":
    main()    