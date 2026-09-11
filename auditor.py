inventory = 0
fr_entries = 0;

while True:
    stock = input("\nEnter Stock Quantity: ")
    if stock.isdigit():
        inventory = inventory + int(stock)
        print(inventory)
    elif stock == "quit":
        print("\nTotal Units Processed: ", inventory);
        print("Number of Failed/Rejected Entries:", fr_entries);
        print("\n")
        break;
    else:
        print("Not a number\n")
        fr_entries = fr_entries + 1;

    if inventory >= 500:
        print("\nInventory exceeds 500 quantity\n")
        break;