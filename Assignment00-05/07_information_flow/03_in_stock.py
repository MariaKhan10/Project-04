def main():
    fruit : str = input("Enter a Fruit : ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This Fruit is not in stock")
    else:
        print("This Fruit is in stock , Here is how many: ")
        print(stock)    



def num_in_stock(fruit):
    if fruit == "banana":
        return 4
    if fruit == "apple":
        return 6
    if fruit == "cherry":
        return 100
    else:
        return 0
    
if __name__ == "__main__":
    main()    