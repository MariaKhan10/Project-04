# mypy: ignore-errors

def main():
    fruits = {
        "apple":100,
        "banana" : 150,
        "cherry" : 200,
        "Kiwi" : 300,
        "Strawberry" : 500
    }

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many "  + fruit_name +   " do you want to buy : "))
        total_cost += (price * amount_bought)

    print("Your Total cost is "+ str(total_cost) + " Rupees")


if __name__ == '__main__':
    main()




