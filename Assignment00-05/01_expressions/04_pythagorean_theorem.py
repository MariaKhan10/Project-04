# mypy: ignore-errors

import math

def main():
    ab : float = float(input("Enter the length of AB : "))
    ac : float = float(input("Enter the length of AC : "))
    bc : float = math.sqrt(ab**2 + ac**2)
    print("The Length of BC (Hypotenuse) of Traingle is " , str(bc))

if __name__ == "__main__":
    main()    