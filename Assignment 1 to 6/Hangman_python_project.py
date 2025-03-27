import random

def choose_word():
    words = ['python', 'developer', 'hangman', 'programming', 'computer', 'software', 'algorithm', 'debugging', 'variable', 'function', 'loop', 'syntax', 'database', 'frontend', 'backend']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Wrong guess!")

        if set(word).issubset(guessed_letters):
            print("\nCongratulations! You guessed the word correctly: ", word)
            break
    else:
        print("\nGame Over! The word was: ", word)

if __name__ == "__main__":
    hangman()
