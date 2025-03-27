# mypy: ignore-errors
Sentence_Start : str = "Python is my favorite programming language because it is "

def main():
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    print(Sentence_Start + " " + adjective + " " + noun + " " + verb)

if __name__ == '__main__':
    main()    