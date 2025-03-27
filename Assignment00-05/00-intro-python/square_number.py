# mypy: ignore-errors

def main():
    squared_number : float = float(input("Enter Number to Find it's Square : ")) 
    result = str(squared_number ** 2 )
    print(f"The square of {squared_number} is : {result}")

if __name__ == "__main__":
    main()    






  