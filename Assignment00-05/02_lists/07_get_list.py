# mypy: ignore-errors

def main():
    list1 = []

    value = input("Enter a Value ")
    while value:
        list1.append(value)
        value = input("Enter a Value ")

    print("Here is your List",list1)    


if __name__ == '__main__':
    main()