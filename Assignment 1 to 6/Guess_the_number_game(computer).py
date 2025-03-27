import random

def guess():
    random_number = random.randint(1, 10)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and 10: "))
        if guess < random_number:
            print("Your Guess is too Low")
        elif guess > random_number:
             print("Your Guess is too High")
    print("Congrats you guessed the right number thats,", random_number)   

guess()          
