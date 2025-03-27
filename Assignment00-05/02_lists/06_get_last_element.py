# mypy: ignore-errors

def get_last_element(last): 
    print(last[-1])


def get_last():
    last = [] 
    elem = input("Please enter an element of the list or press enter to stop. ") 
    while elem != "": 
        last.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ") 
    return last

def main():
     last = get_last() 
     get_last_element(last)

if __name__ == '__main__':
     main()