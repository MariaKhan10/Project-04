def main():
    for i in range(10):
        if isodd(i):
            print(i, "Odd")
        else:
            print(i, "Even")   

def isodd(value: int):
    remainder = value % 2   
    return remainder == 1

if __name__ == '__main__':
    main()
       