# mypy: ignore-errors

def main():
    userinput1 : float = float(input("Enter Length of First side of Triangle : "))
    userinput2 : float = float(input("Enter Length of Second side of Triangle : "))
    userinput3 : float = float(input("Enter Length of Third side of Triangle : "))

    result = str(userinput1 + userinput2 + userinput3)
    print(f"The Perimeter of Triangle is : {result}")

if __name__ == "__main__":
    main()  