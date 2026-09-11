inventory = 0

while True:
    stock = input("\nEnter Stock Quantity: ")
    if stock.isdigit():
        inventory = inventory + int(stock)
        print(inventory)
    elif stock == "quit":
        break;