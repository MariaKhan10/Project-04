# mypy: ignore-errors


def read_phone_book():
    phonebook = {}
    while True:
        name = input("Enter Name : ")
        if name == "":
            break
        number = input("Enter Number : ")
        phonebook[name] = number

    return phonebook




def print_phone_book(phonebook):
    for name in phonebook: 
        print(str(name),str(phonebook[name]))



def lookup_phone_book(phonebook):
    while True:
        name = input("Enter name to lookup :")
        if name == "":
            break
        if name not in phonebook:
            print(name , "is not in the phonebook")        
        else:
            print(phonebook[name])    


def main():
    phonebook = read_phone_book()
    print_phone_book(phonebook)
    lookup_phone_book(phonebook)


if __name__ == '__main__':
    main()