def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print("Yesterday, I saw a mysterious " + word + " sitting on my desk.")
    elif part_of_speech == 1:
        print("Whenever I’m stressed, I just want to " + word + " all day.")
    elif part_of_speech == 2:
        print("That dress looks absolutely " + word + " on you!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")



def main():
    word :  str = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
