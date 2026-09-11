inventory = 0

while True:
    stock = input("\nEnter Stock Quantity: ")
    if stock.isdigit():
        inventory = inventory + int(stock)
        print(inventory)
    elif stock == "quit":
        print("\nTotal Units Processed: ", inventory);
        break;
    else:
        print("Not a valid number\n")

    if inventory >= 500:
        print("\nInventory exceeds 500 quantity\n")
        break;