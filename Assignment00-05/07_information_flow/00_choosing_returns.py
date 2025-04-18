adult_age : int = 18

def is_adult(age:int):
    if age >= adult_age:
        return True
    
    return False

def main():
    age = int(input("How old is this person ? : "))
    print(is_adult(age))

if __name__ == "__main__":
    main()    




       
