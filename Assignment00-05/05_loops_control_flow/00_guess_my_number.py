import random

def main():
    random_number = random.randint(1,10)
    while True:
        user_guess = int(input("Guess a Number between 1 and 10 : "))
        if user_guess == random_number:
            print("Congrats !! You guessed the right number thats : ", random_number)
            break
        if user_guess > random_number:
            print("Your guess is too high")
        if user_guess < random_number:
            print("Your guess is too low")
           


if __name__ == '__main__':
    main()

