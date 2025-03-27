# mypy: ignore-errors

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    user_age = int(input("How old are you ?"))
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in PETURKSBOUIPO where the voting age is ", str(PETURKSBOUIPO_AGE))
    else:
        print("You can not vote in PETURKSBOUIPO where the voting age is ", PETURKSBOUIPO_AGE) 
    if user_age >= STANLAU_AGE:
        print("You can vote in STANLAU_AGE where the voting age is ", str(STANLAU_AGE))
    else:
        print("You can not vote in STANLAU_AGE where the voting age is ", STANLAU_AGE) 
    if user_age >= MAYENGUA_AGE:
        print("You can vote in MAYENGUA_AGE where the voting age is ", str(MAYENGUA_AGE))
    else:
        print("You can not vote in MAYENGUA_AGE where the voting age is ", MAYENGUA_AGE) 
                   


if __name__ == '__main__':
    main()







    