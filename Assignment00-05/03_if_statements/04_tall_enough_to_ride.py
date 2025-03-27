Min_Height = 40

def main():
    while True:
        height_input = input("How Tall are You? (Press Enter to stop) ")
        
        if height_input == "":  
            print("Exiting the program. Have a great day!")
            break

        try:
            height = float(height_input) 
            if height >= Min_Height:
                print("You are tall enough to ride!")
            else:
                print("You are not tall enough to ride, maybe next year!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
