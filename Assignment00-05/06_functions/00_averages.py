def main():
    int1:float = float(input("Enter First Number : "))
    int2: float  = float(input("Enter Second Number : "))
    sum = float(int1 + int2)
    avg = sum/2
    print("The Average of",int1 ,"and", int2 , "is", ":",  avg)

if __name__ == "__main__":
    main()   




# Other Way

def average(a:float,b:float):
    sum = a + b
    return sum/2

def main():
    avg1 = average(30,70)
    print(avg1)

if __name__ == "__main__":
    main() 