# mypy: ignore-errors
import random

Num_sides : int = 6

def main():
    random.seed(1)
    dice1 : int = random.randint(1,Num_sides)
    dice2 : int = random.randint(1,Num_sides)
    total : int = dice1 + dice2
    print("dice1",dice1)
    print("dice2",dice2)
    print("total",total)

if __name__ == "__main__":
    main()