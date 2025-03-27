AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please Type the following Affirmation : ", AFFIRMATION)
    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("Thats not the Affirmation")
        print("Please Type the following Affirmation : ", AFFIRMATION)
        user_feedback = input()

    print("Thats Right..!! Good Keep it up")   



if __name__ == '__main__':
    main()     