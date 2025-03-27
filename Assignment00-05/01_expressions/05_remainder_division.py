# mypy: ignore-errors

def main():
    num1 : int = int(input("Enter First Number to be Divided : "))
    num2 : int = int(input("Enter Second Number to Divide By : "))
    result = num1 // num2
    remainder = num1 % num2
    print("The Result of the Division is ", result ,"with a remainder of ", remainder )

if __name__ == "__main__":
    main()    