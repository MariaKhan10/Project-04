PROMPT : str = "What do you want ? "
JOKE : str = "A sandwich tried to get a reservation at a restaurant, but the waiter said they don’t serve food there."
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT)
    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print(SORRY)   

if __name__ == '__main__':
    main()


