# mypy: ignore-errors
C: int = 299792458

def main():
    mass_in_kg : float = float(input("Enter Kilos of mass : "))
    energy_in_joules : float = mass_in_kg * (C ** 2)
    print("e = mc\u00B2")
    print(mass_in_kg , "kg")
    print(C , "m/s")
    print(energy_in_joules , "energy_in_joules")

if __name__ == "__main__":
    main()    

