# mypy: ignore-errors

inches_per_foot : int = 12

def main():
    feet : float = float(input("Enter number in Feet :"))
    inches = feet * inches_per_foot
    print(f"There are {inches} inches per {feet} foot" )

if __name__ == "__main__":
    main()    