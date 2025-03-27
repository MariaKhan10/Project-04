# mypy: ignore-errors


def main():
    print("Welcome to Addition program of 2 numbers")
    num1 : str = input("Enter Your First Number : ")
    num1 : int = int(num1)
    num2 : str = input("Enter Your Second Number : ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The Result is :",num1 , "+" , num2 , "=" , int(total))


if __name__ == "__main__":
    main()

