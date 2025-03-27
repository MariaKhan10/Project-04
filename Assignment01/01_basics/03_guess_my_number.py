import random

def main():
    random_num = random.randint(1,10)
    while True:
        user_input = int(input("Guess a number between 1 and 10 : "))
        if user_input == random_num:
            print("Congrats you guessed the right number thats ", random_num)
            break
        if user_input < random_num:
            print("Your guess is too low")
        if user_input > random_num:
            print("Your guess is too High")    

if __name__ == "__main__":
    main()         

    